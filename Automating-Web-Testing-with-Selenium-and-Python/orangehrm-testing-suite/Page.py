from PageObjectModels import PageFactory


class PageBase(PageFactory):
    def __init__(self, driver):
        super().__init__(driver)


class LoginPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.openPage("https://opensource-demo.orangehrmlive.com")


class PasswordResetPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.openPage("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
