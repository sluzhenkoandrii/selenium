from typing import Tuple

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common_and_waits.common import (wait_visibility, wait_elements_visibility, wait_to_be_clickable,
                                     wait_invisibility)


class GadgetModuleSelectors:
    """Selectors for gadget module elements."""
    EDIT_GADGET_BUTTON = (By.CSS_SELECTOR, 'div[class="react-grid-layout"] button:nth-child(2)')
    MODAL_HEADER = (By.CSS_SELECTOR, '.modal-header')
    SELECT_DATA = (By.CSS_SELECTOR, '.Select-value__title')
    OPTIONS = (By.CSS_SELECTOR, '.Select-options__title')
    COLUMN_INPUT = (By.CSS_SELECTOR, '.vochub-select-control.multiselect')
    RETURNED_COLUMNS = (By.CSS_SELECTOR, '.component-option_label')
    MATH_FUNC_INPUT = (By.XPATH, '//div[contains(text(),"Select Math function")]')
    RETURNED_MATH_FUNCTIONS = (By.CSS_SELECTOR, '.vochub-select-control__option')
    GADGET_SAVE_BUTTON = (By.XPATH, '//button[@class="btn btn-primary"]')
    LOADING_SPINNER = (By.CSS_SELECTOR, ".loader")


class GadgetModule:
    """Class for gadget configuring."""

    def __init__(self, selenium: WebDriver) -> None:
        """Initialize the class with Selenium WebDriver instance."""
        self.selenium = selenium

    def click_on_edit_gadget_button(self) -> None:
        """Click on 'Edit Gadget' button and wait for modal."""
        wait_to_be_clickable(self.selenium, *GadgetModuleSelectors.EDIT_GADGET_BUTTON).click()
        wait_visibility(self.selenium, *GadgetModuleSelectors.MODAL_HEADER)

    def _select_option(self,
                       input_selector: Tuple[str, str],
                       options_selector: Tuple[str, str],
                       value: str
                       ) -> None:
        """Common method to select option from dropdown."""
        select_input = wait_visibility(self.selenium, *input_selector)
        ActionChains(self.selenium).click(select_input).send_keys(value).perform()

        options = wait_elements_visibility(self.selenium, *options_selector)
        for option in options:
            if option.text == value:
                ActionChains(self.selenium).move_to_element(option).click().perform()
                return
        raise Exception(f"Option '{value}' not found")

    def select_source(self, source_title: str) -> None:
        """Select source from dropdown."""
        self._select_option(GadgetModuleSelectors.SELECT_DATA,
                            GadgetModuleSelectors.OPTIONS, source_title)

    def select_fact(self, fact_column_list: list[str]) -> None:
        """Select multiple fact columns from dropdown."""
        for fact_column in fact_column_list:
            self._select_option(GadgetModuleSelectors.COLUMN_INPUT,
                                GadgetModuleSelectors.RETURNED_COLUMNS, fact_column)

    def select_group_by(self, which_group_by_input: str, group_column: str) -> None:
        """Select 'Group By' column."""
        group_by_input = wait_visibility(
            self.selenium, By.XPATH, f"//div[text() = '{which_group_by_input}']")

        ActionChains(self.selenium).click(group_by_input).send_keys(group_column).perform()
        self._select_option(GadgetModuleSelectors.RETURNED_COLUMNS,
                            GadgetModuleSelectors.RETURNED_COLUMNS, group_column)

    def select_math_function(self, math_function: str) -> None:
        """Select math function from the dropdown."""
        self._select_option(GadgetModuleSelectors.MATH_FUNC_INPUT,
                            GadgetModuleSelectors.RETURNED_MATH_FUNCTIONS, math_function)

    def select_chart_type(self, chart_type: str) -> None:
        """Select chart type and wait for loading spinner to disappear."""
        wait_visibility(self.selenium, By.CSS_SELECTOR, chart_type).click()
        wait_invisibility(self.selenium, *GadgetModuleSelectors.LOADING_SPINNER)

    def click_on_save_gadget(self) -> None:
        """Click on 'Save Gadget' button and wait for loading spinner to disappear."""
        wait_to_be_clickable(self.selenium, *GadgetModuleSelectors.GADGET_SAVE_BUTTON).click()
        wait_invisibility(self.selenium, *GadgetModuleSelectors.LOADING_SPINNER)

