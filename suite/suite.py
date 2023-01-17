###################################################################################################
##  DESCRIPTION:
##      This is the functional suite file with automated tests for Login Page
##
##  RUN TESTS:
##              all             => python3 -m pytest -v login_suite.py
##
##                              Copyright @prezent.ai 2021.
###################################################################################################
import pytest
from seleniumbase import BaseCase
# from base.pz_decorators import # uiDecorator
# from actions import LoginActions
from actions.action import LoginActions


class TestLogin(BaseCase):



    @pytest.mark.high
    def test_001_C763_logout(pzsb):
        LoginActions().do_login(pzsb, username='amod-uat.noreply@abbvie.com', password='7b6907195ed41d261bd9')
        LoginActions().do_logout(pzsb)

    @pytest.mark.highest
    def test_002_C764_terms_of_service(self):
        LoginActions().verify_link(self, 'Terms of Service')

    @pytest.mark.highest
    def test_003_C765_privacy_policy(self):
        LoginActions().verify_link(self, 'Privacy Policy')

    def tearDown(self):
        print('---> tearDown')
        super(TestLogin, self).tearDown()

    @classmethod
    def tearDownClass(self):
        print('---> tearDownClass')
        super(TestLogin, self).tearDownClass()
