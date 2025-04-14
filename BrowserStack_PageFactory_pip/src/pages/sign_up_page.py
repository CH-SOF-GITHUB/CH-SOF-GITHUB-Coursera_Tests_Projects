from seleniumpagefactory import PageFactory


class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'full_name': ('ID', 'user_full_name'),
        'buisness_email': ('ID', 'user_email login'),
        'password': ('ID', 'user_password'),
        'tnc': ('ID', 'tnc_checkbox'),
        'sign_up': ('ID', 'user_submit'),
        'accept_all': ('ID', 'accept-cookie-notification')
    }

    def enter_full_name(self):
        self.full_name.set_text("Test User")
        print("Full name entered")

    def enter_buisness_email(self):
        self.buisness_email.set_text("Test User")