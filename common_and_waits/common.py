"""VocHub automated tests with Selenium: common functions and constants."""

from datetime import datetime
from os import path, getenv
import yaml
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    invisibility_of_element_located as invisible,
    text_to_be_present_in_element as text_present, visibility_of_element_located as visible, element_to_be_clickable,
    presence_of_element_located
)

TIMEOUT = 60  # Selenium timeout to wait() for elements to appear.


def env(var):
    """Return the value for a specified env. variable, exit if not found."""
    if value := getenv(var):
        return value
    raise SystemExit('env variable ' + var + ' not defined')


if cluster := getenv('CLUSTER'):
    with open('enterprises/' + cluster + '.yml', encoding='utf-8') as file:
        config = yaml.safe_load(file)
else:
    config = {
        'enterprise': env('ENTERPRISE'),
        'xircl': env('XIRCL'),
        'fbapi': env('FBAPI'),
        'survey': env('SURVEY'),
        'astra': env('ASTRA'),
        'sso': env('SSO'),
        'smstest': env('SMSTEST'),
        'username': env('USERNAME'),
        'password': env('PASSWORD'),
        'access_code': env('ACCESS_CODE'),
        'sso_api_appname': env('SSO_API_APPNAME'),
        'sso_api_secret': env('SSO_API_SECRET'),
        'sms_gateway_name': env('SMS_GATEWAY_NAME'),
        'sms_sender_name': env('SMS_SENDER_NAME'),
        'sms_phone_number': env('SMS_PHONE_NUMBER'),
        'sender_email': env('SENDER_EMAIL'),
        'mysql_host': env('MYSQL_HOST'),
        'mysql_port': env('MYSQL_PORT'),
        'mysql_user': env('MYSQL_USER'),
        'mysql_pass': env('MYSQL_PASS'),
        'mongo_uri': env('MONGO_URI'),
        'vocact_case_alert': env('VOCACT_CASEALERT_URL'),
        'vocact_case_alert_token': env('VOCACT_CASEALERT_TOKEN'),
        'bounce_email_address': env('BOUNCE_MAIL_ADDRESS')
    }


def wait_visibility(selenium, by, selector):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to become visible and return it."""
    WebDriverWait(selenium, timeout=TIMEOUT, ignored_exceptions=[
        ElementNotVisibleException, ElementNotSelectableException]).until(visible((by, selector)))
    return selenium.find_element(by, selector)


def wait_elements_visibility(selenium, by, selector):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to become visible and return it."""
    WebDriverWait(selenium, timeout=TIMEOUT).until(visible((by, selector)))
    return selenium.find_elements(by, selector)


def wait_presents(selenium, by, selector):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to become visible and return it."""
    WebDriverWait(selenium, timeout=TIMEOUT).until(presence_of_element_located((by, selector)))
    return selenium.find_element(by, selector)


def wait_to_be_clickable(selenium, by, selector):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to become visible and return it."""
    WebDriverWait(selenium, timeout=TIMEOUT).until(element_to_be_clickable((by, selector)))
    return selenium.find_element(by, selector)


def wait_invisibility(selenium, by, selector):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to become invisible."""
    WebDriverWait(selenium, timeout=TIMEOUT).until(invisible((by, selector)))


def wait_matching_text(selenium, by, selector, text, timeout):  # pylint: disable=invalid-name
    """Wait for the DOM element specified to match specific text."""
    WebDriverWait(selenium, timeout=timeout).until(text_present((by, selector), text))


def get_jwt_token():
    """Get and return JWT token."""
    response = FbApiTest(
        config['access_code'], config['fbapi'], config['sso'], config['sso_api_appname'],
        config['sso_api_secret'])
    return response.jwt


def get_downloads_path(headless, project, path_to_etalon_file):
    """
    Returns a relative or absolute path to the directory when downloaded files are stored.

    Final slash included. Might be just empty string for current directory.
    """
    if headless and path_to_etalon_file == '':
        return ''
    if path_to_etalon_file and project == 'Store':
        return 'project/Store/store_ui/data/'
    elif path_to_etalon_file and project == 'Mine':
        return 'project/Mine/mine_ui/data/'
    return path.expanduser('~') + path.sep + 'Downloads' + path.sep


def generate_title():
    """Returns string: Autotest Sandsiv + current date and time."""
    # We replace dashes and dots here as archiving to ZIP changes those symbols.
    return 'Autotest Sandsiv ' + str(datetime.now()).replace(':', "_").replace('.', "_")
