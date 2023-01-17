########################################################################
## DESCRIPTION:
##      This package contains Login Page actions. These actions are
##  used in functional and scenarios test suite files.
##
##      Copyright @prezent.ai 2021.
########################################################################
import os
# from base.pz_timer import PzTimer
# from features.lib.api.pz_api_authentication import PzApiAuthentication


class LoginActions():

    def first_time_login_user(self, pzsb, username, password, sso=False):
        print('Entering username - {}'.format(username))
        prod_host_url = 'https://uatstaging.myprezent.com'
        print('Opening Signin page - {}'.format(prod_host_url))
        pzsb.open(prod_host_url + '/home/main')
        pzsb.type("#username", username)
        if pzsb.is_element_present('span:contains("Continue")'):
            print("Clicking on 'Continue' button")
            pzsb.click('span:contains("Continue")')
            print("Entering password")
            pzsb.type("#password", password)
            #pzsb.pzmain.take_screenshot(pzsb)
            print("Clicking on 'Submit' button")
            pzsb.click('#submit', timeout=10)
        pzsb.wait_for_element_present('div.section-wrapper.first-screen', timeout=20)
        print("First time login user. Welcome message below ")
        print("The welcome text is : {}".format(pzsb.find_element('div.name-wrapper').text))
        print("The highlighted text is : {}".format(pzsb.find_element('div.highlight-normal').text))
        print("The sub header text is : {}".format(pzsb.find_element('div.sub-header').text))
        print("Clicking on Let's Go button")
        #pzsb.pzmain.take_screenshot(pzsb)
        pzsb.click('#letsgo')
        pzsb.sleep(8)
        # PzApiAuthentication().update_login_user_in_test_props(pzsb, username, password)

    def do_ioc_login(self, pzsb, username=None, password=None):
        # Check if we are already logged in? Combobox search field will be present.
        if pzsb.is_element_present("div[role='combobox']"):
            print("Current url is: {}".format(pzsb.get_current_url()))
            print("Global search entry field is present. Already logged in.")
            #pzsb.pzmain.take_screenshot(pzsb)
            return True
        else:
            prod_host_url = 'https://uatstaging.myprezent.com'
            print('Opening Signin page - {}'.format(prod_host_url))
            pzsb.open(prod_host_url + '/ioc/home')
            pzsb.wait_for_element_present('#username')
        # Get from properties file if username is None
        if username is None or (password is None):
            default_test_user = pzsb.pzconfig.get_defaults()['DEFAULT_SUPER_ADMIN']
            username = default_test_user['USERNAME']
            password = default_test_user['PASSWORD']
            print("User details taken from properties file: " + username)
        print('Entering username - {} & password'.format(username))
        pzsb.type("#username", username)
        pzsb.type("#password", password)
        #pzsb.pzmain.take_screenshot(pzsb)
        pzsb.click("button.loginButton.v-btn")
        #pzsb.pzmain.take_screenshot(pzsb)
        pzsb.wait_for_element_absent("button.loginButton.v-btn")
        print("Waiting for home page to load, combobox search bar to appear.")
        pzsb.wait_for_element("div[role='combobox']", timeout=60)

    def do_ioc_logout(self, pzsb):
        print("Clicking on Logout icon")
        pzsb.click("button.headerButtons", timeout=10)
        print("Asserting username field")
        pzsb.assert_element('#username')
        print(pzsb.get_current_url())
        print("Return current url to caller")
        #pzsb.pzmain.take_screenshot(pzsb)
        return pzsb.get_current_url()

    def _wait_for_home_page_to_load(self, pzsb):
        print("Waiting for home page to load. 'global-hybrid-search' to appear.")
        pzsb.wait_for_element('input#global-hybrid-search', timeout=30)
        ## Below will ensure that the quote is shown in UI.
        pzsb.wait_for_element("//div[@class='main-section-wrapper']")
        print("Quote shown is : {}".format(
            pzsb.wait_for_element("//div[@class='main-section-wrapper']").get_attribute('style')))

    def do_login(self, pzsb, username=None, password=None):
        ## Check if we are already logged in? Global search field will be present.
        prod_host_url = 'https://uatstaging.myprezent.com'
        print('Opening Signin page - {}'.format(prod_host_url))
        pzsb.open(prod_host_url + '/home/main')
        pzsb.wait_for_element_present('#username')
        ## Get from properties file if username is None ##
        if username is None or (password is None):
            default_test_user = pzsb.pzconfig.get_defaults()['DEFAULT_TESTUSER']
            username = default_test_user['USERNAME']
            password = default_test_user['PASSWORD']
            print("User details taken from properties file: " + username)
        #pzsb.pzmain.take_screenshot(pzsb)
        print('Entering username - {}'.format(username))
        pzsb.type("#username", username)
        print("Clicking on 'Continue' button")
        pzsb.click('span:contains("Continue")')
        ### #pzsb.pzmain.pz_ui.pz_send_keys_slowly( pzsb.find_element('#username'), username)
        pzsb.wait(5)
        if pzsb.is_element_present('#password'):
            print("Entering password")
            pzsb.type("#password", password)
            try:
                pzsb.click('button.mdi-eye-off')  # Click on show password to see if correct password is entered
            except:
                print("Ignored Show password error")
            #pzsb.pzmain.take_screenshot(pzsb)
            print("Clicking on 'Submit' button")
            pzsb.click('#submit')
            self._wait_for_home_page_to_load(pzsb)
        else:
            ## Continue button was not seen... Error or SSO
            if pzsb.is_element_present('#okta-signin-username'):
                pzsb.type("#okta-signin-username", username)
                pzsb.type("#okta-signin-password", password)
                #pzsb.pzmain.take_screenshot(pzsb)
                print("Clicking on 'Submit' button")
                pzsb.click("#okta-signin-submit")
                self._wait_for_home_page_to_load(pzsb)
        print("Current url is : {}".format(pzsb.get_current_url()))
        pzsb.sleep(8)
        if pzsb.is_element_present('div._pendo-step-container-styles'):
            ## Pendo Welcome or New Feature Pendo is present. Click on close
            print("New Features Pendo is shown.")
            pzsb.wait_for_element('#pendo-guide-container', timeout=10)  ## elements got changed
            print("'{}'".format(pzsb.get_text('#pendo-guide-container')))
            # print("'{}'".format(pzsb.get_text('.bb-text._pendo-text-paragraph')))
            pzsb.click('button._pendo-close-guide')
        else:
            print("Pendo welcome for New features was not shown.")
        ## Close "Introducing Prezent with heart! pendo pop-up
        if pzsb.is_element_present('div._pendo-step-container-styles'):
            print("Prezent with heart Pendo is shown.")
            pzsb.wait_for_element('#pendo-guide-container', timeout=10)  ## elements got changed
            print("'{}'".format(pzsb.get_text('#pendo-guide-container')))
            pzsb.click('button._pendo-close-guide')
        else:
            print("Pendo prezent with heart was not shown.")
        #pzsb.pzmain.take_screenshot(pzsb)
        # PzApiAuthentication().update_login_user_in_test_props(pzsb, username, password)
        return pzsb.get_current_url()

    def do_logout(self, pzsb):
        print("Clicking on Profile icon")
        pzsb.click("div[name='profile-icon']", timeout=8)
        print("Asserting Basics tab")
        pzsb.assert_elements('#basics-tab')
        print("Clicking on SignOut button")
        pzsb.click("button[class*='edit-profile-btn log-out-button']")
        print("Asserting username field")
        pzsb.assert_element('#username')
        print(pzsb.get_current_url())
        print("Return current url to caller")
        #pzsb.pzmain.take_screenshot(pzsb)
        return pzsb.get_current_url()

    def verify_link(self, pzsb, link_text):
        prod_host_url = 'https://uatstaging.myprezent.com'
        print('Opening Signin page - {}'.format(prod_host_url))
        pzsb.open(prod_host_url)
        self.verify_link_helper(pzsb, link_text)

    def verify_link_helper(self, pzsb, link_text):
        print("Page title is: " + pzsb.get_title())
        print("Clicking on link with text: {}".format(link_text))
        pzsb.click_link(link_text)
        print("Switching to new window opened.")
        pzsb.switch_to_newest_window()
        print("Page title of new window is: " + pzsb.get_title())
        print("Verifying if the new window page title is : " + link_text)
        if link_text == 'Privacy Policy':
            pzsb.assert_title("Privacy")
        else:
            pzsb.assert_title(link_text)
        prod_current_url = pzsb.get_current_url()
        pzsb.switch_to_default_window()
        print("Page title now is: " + pzsb.get_title())
        return prod_current_url

    def do_matomo_login(self, pzsb, username=None, password=None):
        print("Open Matomo URL and Login")
        matomo_host_url = pzsb.pzconfig.get_defaults()['MATOMO_HOST']
        print('Opening Signin page - {}'.format(matomo_host_url))
        pzsb.open(matomo_host_url)
        pzsb.wait_for_element_present('#login_form_login')
        # Get from properties file if username is None
        if username is None or (password is None):
            matomo_user = pzsb.pzconfig.get_defaults()['MATOMO_USER']
            username = matomo_user['USERNAME']
            password = matomo_user['PASSWORD']
            print("User details taken from properties file: " + username)
        print('Entering username - {} & password'.format(username))
        pzsb.type("#login_form_login", username)
        pzsb.type("#login_form_password", password)
        #pzsb.pzmain.take_screenshot(pzsb)
        pzsb.click("#login_form_submit")
        #pzsb.pzmain.take_screenshot(pzsb)
        pzsb.wait_for_element_absent("#login_form_submit")
        print("Waiting for home page to load")
        pzsb.wait_for_element_present(".menuTab.active", timeout=60)


if __name__ == '__main__':
    pass

