from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common_and_waits.common import wait_elements_visibility, wait_visibility


class GadgetSelectors:
    """All CSS selectors for the Gadget module."""
    LEGENDS_TEXT = '.filterLabelButton > span'
    Y_AXIS_TICKS = '.yAxis > .tick'
    X_AXIS_TICKS = '.xAxis > .tick'
    CHART_BARS = '.bar'
    CHART_RECORDS_LABEL = '[class*="recordsLabel"]'
    CHART_LEGENDS = '.filterLabelButton'
    TOOLTIP = '.popover_chart_tooltip'
    SEGMENT_SCORE = '.barScore'


class GadgetEntities:
    def __init__(self, selenium):
        self.selenium = selenium

    def get_legends_list(self):
        """Returns a list of legend names."""
        return [legend.text for legend in
                wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.LEGENDS_TEXT)]

    def get_ticks_list_by_y_axis(self):
        """Returns a list of Y-axis tick values."""
        return [tick.text for tick in
                wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.Y_AXIS_TICKS)]

    def get_ticks_list_by_x_axis(self):
        """Returns a list of X-axis tick values."""
        return [tick.text for tick in
                wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.X_AXIS_TICKS)]

    def get_chart_bar_count(self):
        """Returns number of records visualized in the chart."""
        return len(wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.CHART_BARS))

    def get_chart_records_value(self):
        """Returns value of the chart's record label."""
        return wait_visibility(self, By.CSS_SELECTOR, GadgetSelectors.CHART_RECORDS_LABEL).text

    def get_chart_legends_count(self):
        """Returns number of legends in the chart."""
        return len(wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.CHART_LEGENDS))

    def get_tooltip_from_bars(self):
        """Returns a list of tooltip texts from all bars."""
        bars = wait_elements_visibility(self, By.CSS_SELECTOR, GadgetSelectors.CHART_BARS)
        tooltips = []

        for bar in bars:
            ActionChains(self.selenium).move_to_element(bar).perform()
            tooltips.append(wait_visibility(self.selenium, By.CSS_SELECTOR, GadgetSelectors.TOOLTIP).text)

        return tooltips

    def get_segment_score_value(self):
        """Returns a list of segment scores from bars."""
        return [score.text for score in
                wait_elements_visibility(self.selenium, By.CSS_SELECTOR, GadgetSelectors.SEGMENT_SCORE)]
