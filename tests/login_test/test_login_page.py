import pytest

from app.pom.pages.logged_in_successfully_page import LoggedInSuccessfullyPage
from app.pom.pages.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login  # Marks are similar to tags
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.expected_url == logged_in_page.current_url, "Actual URL is not the same as expected"
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"
