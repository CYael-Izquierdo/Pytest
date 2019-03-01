import pytest
from pytest import Item


def pytest_sessionfinish(session, exitstatus):
    kill_appium_process()


def kill_appium_process():
    if hasattr(pytest, 'appium_data'):
        pytest.appium_data['appium_subprocess'][2].kill()
        pytest.appium_data['appium_subprocess'][2].terminate()
        pytest.appium_data['appium_subprocess'] = None
