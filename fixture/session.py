

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_yandex_email_page()
        wd.find_element_by_name("login").send_keys(username)
        wd.find_element_by_name("passwd").send_keys(password)
        wd.find_element_by_xpath("//div[@class='new-left']//button[.='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.mail-User-Name").click()
        wd.find_element_by_link_text("Выход").click()
