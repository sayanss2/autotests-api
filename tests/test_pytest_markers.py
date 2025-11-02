import pytest

"""
@pytest.mark.authentication
class TestUserAuthentication:
    
    @pytest.mark.critical
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    @pytest.mark.smoke
    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.critical
def test_critical_login():
    pass


@pytest.mark.api
class TestUserInterface:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.regression
    def test_forgot_password(self):
        pass

    @pytest.mark.smoke
    def test_signup(self):
        pass
"""

@pytest.mark.skip(reason="Для тестового запуска")
@pytest.mark.smoke
class TestLogin:
    @pytest.mark.smoke
    def test_valid_login(self):
        pass

    @pytest.mark.regression
    def test_invalid_login(self):
        pass

@pytest.mark.skip(reason="Для тестового запуска")
@pytest.mark.regression
class TestRegistration:
    @pytest.mark.regression
    def test_valid_registration(self):
        pass

    @pytest.mark.smoke
    def test_invalid_registration(self):
        pass

@pytest.mark.skip(reason="Для тестового запуска")
@pytest.mark.smoke
@pytest.mark.regression
class TestCheckout:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_checkout(self):
        pass

    def test_invalid_checkout(self):
        pass

@pytest.mark.skip(reason="Для тестового запуска")
def test_search():
    pass