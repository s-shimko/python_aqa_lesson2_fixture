class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.open_add_contact_page()
        self.fill_forms(contact)
        self.return_contact_page()

    def fill_forms(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_list_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//a[@href='./']").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_list_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_list_page()
        elements = wd.find_elements_by_xpath(".//img[@title='Edit']")
        elements[0].click()
        self.fill_forms(contact)
        wd.find_element_by_xpath("(.//input[@name='update'])[1]").click()



