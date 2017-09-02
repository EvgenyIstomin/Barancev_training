

class EmailHelper:

    def __init__(self, app):
        self.app = app

    def create_new_mail(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Написать").click()
        self.fill_out_mail_address("istomin-e@yandex.ru")
        self.fill_out_tema("test")

    def fill_out_mail_address(self, email_address):
        wd = self.app.wd
        wd.find_element_by_name("to").click()
        wd.find_element_by_name("to").send_keys(email_address)

    def fill_out_tema(self, tema):
        wd = self.app.wd
        wd.find_element_by_name("subj").click()
        wd.find_element_by_name("subj").clear()
        wd.find_element_by_name("subj").send_keys(tema)
        wd.find_element_by_id("nb-21").click()

    def delete_first_email(self):
        wd = self.app.wd
        wd.get("https://mail.yandex.ru/#inbox")
        # select first email
        wd.find_element_by_css_selector("span._nb-checkbox-flag._nb-checkbox-normal-flag").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@class='mail-Layout-Content']//span[.='Удалить']").click()