from dataclasses import dataclass
from typing import List


@dataclass
class LineChartTestData:
    dashboard_id: str
    source_title: str
    fact_column: List[str]
    math_function: str
    chart_type: str
    exp_tooltip_data: List[str]
    exp_y_axis_ticks: List[str]
    exp_x_axis_ticks: List[str]
    exp_legends_list: List[str]
    exp_legends_count: int
    exp_points_count: int
    exp_records_value: str


line_chart_without_grouping_data = (
    LineChartTestData(
        dashboard_id='6479b54dc56a97165253d673',
        source_title='Test survey',
        fact_column=['[CHOICE]'],
        math_function='Count',
        chart_type='.line_chart',
        exp_tooltip_data=[
            'Name: 0\nPercentage: 33.3333%\nCount: 5',
            'Name: 10\nPercentage: 40%\nCount: 6',
            'Name: 100\nPercentage: 20%\nCount: 3',
            'Name: No value\nPercentage: 6.6667%\nCount: 1'
        ],
        exp_y_axis_ticks=['1', '2', '3', '4', '5', '6'],
        exp_x_axis_ticks=['No value', '0', '10', '100'],
        exp_legends_list=['0', '10', '100', 'No value'],
        exp_legends_count=4,
        exp_points_count=4,
        exp_records_value='Records: 15'
    ),
    LineChartTestData(
        dashboard_id='6479b54dc56a97165253d673',
        source_title='Test upload',
        fact_column=['[CONFIGURABLE]'],
        math_function='Median',
        chart_type='.line_chart',
        exp_tooltip_data=[
            'Name: 0\nPercentage: 33.3333%\nCount: 5',
            'Name: 10\nPercentage: 40%\nCount: 6',
            'Name: 100\nPercentage: 20%\nCount: 3',
            'Name: No value\nPercentage: 6.6667%\nCount: 1'
        ],
        exp_y_axis_ticks=['12', '23', '34', '45', '56', '67'],
        exp_x_axis_ticks=['Record', 'test', '10', '100'],
        exp_legends_list=['0', '10', '100', 'No value'],
        exp_legends_count=4,
        exp_points_count=4,
        exp_records_value='Records: 435'
    )
)
