from typing import Any

from selenium_project.Visual_project.visual_ui.pages.common_pages.gadget_page import GadgetEntities


class Assert:
    """Class with assertion methods for validating elements in chart."""

    @classmethod
    def validate(cls, actual: Any, expected: Any, description: str) -> None:
        """Common validation method for comparing actual vs expected result."""
        assert actual == expected, f"Expected {description}: {expected}, but got: {actual}"

    @classmethod
    def validate_y_axis_ticks(cls, selenium, expected_ticks):
        cls.validate(
            GadgetEntities(selenium).get_ticks_list_by_y_axis(),
            expected_ticks,
            "Y axis ticks"
        )

    @classmethod
    def validate_x_axis_ticks(cls, selenium, expected_ticks):
        cls.validate(
            GadgetEntities(selenium).get_ticks_list_by_x_axis(),
            expected_ticks,
            "X axis ticks"
        )

    @classmethod
    def validate_legends(cls, selenium, expected_legends):
        cls.validate(
            GadgetEntities(selenium).get_legends_list(),
            expected_legends,
            "legends"
        )

    @classmethod
    def validate_legends_count(cls, selenium, expected_legends_count):
        cls.validate(
            GadgetEntities(selenium).get_chart_legends_count(),
            expected_legends_count,
            "legends count"
        )

    @classmethod
    def validate_bars_count(cls, selenium, expected_count):
        cls.validate(
            GadgetEntities(selenium).get_chart_bar_count(),
            expected_count,
            "bars count"
        )

    @classmethod
    def validate_chart_records_value(cls, selenium, expected_records_value):
        cls.validate(
            GadgetEntities(selenium).get_chart_records_value(),
            expected_records_value,
            "chart records value"
        )

    @classmethod
    def validate_bar_tooltip_data(cls, selenium, expected_tooltip_data):
        cls.validate(
            GadgetEntities(selenium).get_tooltip_from_bars(),
            expected_tooltip_data,
            "bars tooltip data"
        )

    @classmethod
    def validate_segment_score_value(cls, selenium, expected_score_value):
        cls.validate(
            GadgetEntities(selenium).get_segment_score_value(),
            expected_score_value,
            "segment score value"
        )
