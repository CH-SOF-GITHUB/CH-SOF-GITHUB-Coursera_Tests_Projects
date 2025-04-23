from selenium.webdriver.common.by import By


class LoginPageLocators:
    panel_login_locator = (By.CLASS_NAME, 'orangehrm-login-title')
    username_locator = (By.NAME, 'username')
    password_locator = (By.NAME, 'password')
    login_btn_locator = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    alert_content_error_locator = (By.CLASS_NAME, 'oxd-alert-content--error')


class DashboardPageLocators:
    dashboard_text_locator = (By.CLASS_NAME, 'oxd-topbar-header-breadcrumb-module')


class ResetPasswordPageLocators:
    reset_password_button_locator = (By.CLASS_NAME, 'orangehrm-forgot-password-button--reset')
    cancel_reset_pwd_button_locator = (By.CLASS_NAME, 'orangehrm-forgot-password-button--cancel')
