import pytest

from selenium_project.Visual_project.visual_ui.pages.common_pages.asserts_page import Assert
from selenium_project.Visual_project.visual_ui.pages.visual_dashboard_page.dashbord_page import (
    navigate_to_dashboard_by_id)
from selenium_project.Visual_project.visual_ui.pages.common_pages.gadget_conf_page import GadgetModule
from selenium_project.Visual_project.visual_ui.pages.visual_gadget_page.line_chart.line_chart_asserts_page import (
    AssertLineChart
)
from selenium_project.Visual_project.visual_ui.pages.visual_gadget_page.line_chart.line_chart_page import (
    line_chart_without_grouping_data, LineChartTestData
)


@pytest.mark.order(1)
@pytest.mark.parametrize("test_data", line_chart_without_grouping_data)
def test_line_chart_without_grouping(selenium, mongo_drop_and_restore, test_data: LineChartTestData):
    # mongo_drop_and_restore is not implemented in demo version

    gadget_module = GadgetModule(selenium)

    # chart configuration block
    navigate_to_dashboard_by_id(selenium, test_data.dashboard_id)
    gadget_module.click_on_edit_gadget_button()
    gadget_module.select_chart_type(test_data.chart_type)
    gadget_module.select_source(test_data.source_title)
    gadget_module.select_fact(test_data.fact_column)
    gadget_module.select_math_function(test_data.math_function)
    gadget_module.click_on_save_gadget()

    # validation clock
    Assert.validate_y_axis_ticks(selenium, test_data.exp_y_axis_ticks)
    Assert.validate_x_axis_ticks(selenium, test_data.exp_x_axis_ticks)
    Assert.validate_legends(selenium, test_data.exp_legends_list)
    Assert.validate_legends_count(selenium, test_data.exp_legends_count)
    Assert.validate_chart_records_value(selenium, test_data.exp_records_value)
    AssertLineChart.validate_line_chart_point_tooltip_data(selenium, test_data.exp_tooltip_data)
    AssertLineChart.validate_line_chart_points_count(selenium, test_data.exp_points_count)
