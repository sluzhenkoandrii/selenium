from selenium.webdriver.common.by import By
from common_and_waits.common import config, wait_visibility


def navigate_to_dashboard_by_id(selenium, dashboard_id: str) -> None:
    """Navigate to dashboard by ID and wait until edit dash menu will be visible"""

    selenium.get(f'{config["xircl"]}/visualV2/dashboard/{dashboard_id}')
    wait_visibility(selenium, By.ID, 'save-edit')
