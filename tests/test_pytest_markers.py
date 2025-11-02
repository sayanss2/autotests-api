import pytest

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