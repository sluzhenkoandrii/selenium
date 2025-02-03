from typing import Any

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from common_and_waits.common import wait_visibility, wait_elements_visibility


class AssertLineChart:
    """Class containing assertion methods for validating line chart elements."""

    @classmethod
    def validate(cls, actual: Any, expected: Any, description: str) -> None:
        """Universal validation method for comparing actual vs expected data."""
        assert actual == expected, f"Expected {description}: {expected}, but got: {actual}"

    @classmethod
    def validate_line_chart_point_tooltip_data(cls, selenium, expected_tooltip_data):
        cls.validate(
            LineChartGadgetEntities.get_tooltip_from_points(selenium),
            expected_tooltip_data,
            "point tooltip data"
        )

    @classmethod
    def validate_line_chart_with_grouping_point_tooltip_data(cls, selenium, expected_tooltip_data):
        cls.validate(
            LineChartGadgetEntities.get_tooltip_from_points_of_chart_with_grouping(selenium),
            expected_tooltip_data,
            "point tooltip data for chart with grouping"
        )

    @classmethod
    def validate_line_chart_points_count(cls, selenium, expected_points_count):
        cls.validate(
            LineChartGadgetEntities.get_chart_points_count(selenium),
            expected_points_count,
            "line chart points count"
        )

    @classmethod
    def validate_line_chart_with_grouping_points_count(cls, selenium, expected_points_count):
        cls.validate(
            LineChartGadgetEntities.get_chart_points_count_for_chart_with_grouping(selenium),
            expected_points_count,
            "line chart points count for chart with grouping"
        )

    @classmethod
    def validate_lines_count(cls, selenium, expected_lines_count):
        cls.validate(
            LineChartGadgetEntities.get_chart_lines_count(selenium),
            expected_lines_count,
            "lines count"
        )


class LineChartSelectors:
    """Selectors for line chart elements."""
    TOOLTIP = (By.CSS_SELECTOR, '.popover_chart_tooltip')
    LINES = (By.CSS_SELECTOR, '.lineGroup:has(circle)')
    POINTS = (By.CSS_SELECTOR, '.lineGroup')
    GROUPED_POINTS = (By.CSS_SELECTOR, '.circle')


class LineChartGadgetEntities:
    """Class for interacting with line chart elements."""

    def __init__(self, selenium: WebDriver) -> None:
        self.selenium = selenium

    def _get_tooltip_from_elements(self, selector: tuple[str, str]) -> list[str]:
        """Common method to get tooltip data from chart elements."""
        elements = wait_elements_visibility(self.selenium, *selector)
        tooltips = []

        for element in elements:
            ActionChains(self.selenium).move_to_element(element).perform()
            tooltips.append(wait_visibility(self.selenium, *LineChartSelectors.TOOLTIP).text)

        return tooltips

    def get_tooltip_from_points(self) -> list[str]:
        """Get tooltip data from points in line chart."""
        return self._get_tooltip_from_elements(LineChartSelectors.POINTS)

    def get_tooltip_from_points_of_chart_with_grouping(self) -> list[str]:
        """Get tooltip data from points in a grouped line chart."""
        return self._get_tooltip_from_elements(LineChartSelectors.GROUPED_POINTS)

    def get_chart_lines_count(self) -> int:
        """Return the number of lines in chart."""
        return len(wait_elements_visibility(self.selenium, *LineChartSelectors.LINES))

    def get_chart_points_count(self) -> int:
        """Return the number of points in line chart."""
        return len(wait_elements_visibility(self.selenium, *LineChartSelectors.POINTS))

    def get_chart_points_count_for_chart_with_grouping(self) -> int:
        """Return the number of points in grouped line chart."""
        return len(wait_elements_visibility(self.selenium, *LineChartSelectors.GROUPED_POINTS))

