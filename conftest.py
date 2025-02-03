from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from common_and_waits.common import wait_visibility, config


def pytest_addoption(parser):
    """Add `--headless` CLI option."""
    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--headless',  # pylint: disable=protected-access
                     action='store_true',
                     help='enable headless mode for supported browsers.')


@pytest.fixture
def headless(request):
    """Return `True` on headless mode, `False` otherwise."""
    return request.config.getoption('headless')


@pytest.fixture
def chrome_options(chrome_options, headless):  # pylint: disable=redefined-outer-name
    """Set up headless Chrome if `--headless` is specified."""
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if headless:
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--disable-features=InsecureDownloadWarnings")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument('--allow-insecure-localhost')
        chrome_options.headless = True
    return chrome_options


@pytest.fixture
def selenium(selenium, headless, voc_login, test_failed_check):  # pylint: disable=redefined-outer-name
    """Override the pytest-selenium fixture for 4k resolution."""
    if headless:
        selenium.set_window_size(3840, 2160)
        selenium.set_window_position(0, 0)
    else:
        selenium.maximize_window()
    return selenium


@pytest.fixture()
def voc_login(selenium, test_failed_check):
    """Decorator for all actions starting with going to Web UI and logging in."""
    selenium.get(config['xircl'])
    wait_visibility(selenium, By.ID, 'username').send_keys(config['username'])
    wait_visibility(selenium, By.ID, 'password').send_keys(config['password'])
    wait_visibility(selenium, By.ID, '_submit').click()


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # pylint: disable=redefined-outer-name
    """execute all other hooks to obtain the report object"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


# check if a test has failed
@pytest.fixture(scope="function")
def test_failed_check(request, selenium):  # pylint: disable=redefined-outer-name
    """get failed tests"""
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            selenium = request.node.funcargs['selenium']
            take_screenshot(selenium, request.node.nodeid)
            print("executing test failed", request.node.nodeid)


# make a screenshot with a name of the test, date and time
def take_screenshot(selenium, nodeid):
    # pylint: disable=redefined-outer-name
    """make and save screenshot"""
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}' \
                f'.png'.replace("/", "_").replace("::", "__")
    selenium.save_screenshot('Screenshots/' + file_name)


# @pytest.fixture()
# def restore_and_clean_dbs(selenium, headless):  # pylint: disable=redefined-outer-name,unused-argument
#     mongo_drop(mongo_xircl_dump_files)
#     mongo_restore(mongo_xircl_dump_files)
#     insert_to_mysql_db(mysql_xircl_tables_list, 'xircl')  # second parameter is a name of db
#
#
# @pytest.fixture()
# def mongo_drop_and_restore(selenium, headless):  # pylint: disable=redefined-outer-name,unused-argument
#     mongo_drop(mongo_xircl_dump_files)
#     mongo_restore(mongo_xircl_dump_files)
