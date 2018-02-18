from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.open_add_contact_page()
        self.fill_forms(contact)
        self.return_contact_page()
        self.contact_cache = None

    def fill_forms(self, contact):
        wd = self.app.wd

        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)

        wd.find_element_by_name("middlename").send_keys(contact.middlename)

        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
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
        if not (wd.current_url.endswith("/edit.php") and wd.find_elements_by_name("submit") > 0):
            wd.find_element_by_link_text("add new").click()

    def open_contact_list_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/ingex.php") and wd.find_elements_by_name("add") > 0):
            wd.find_element_by_xpath(".//a[@href='./']").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_modified_contact_by_index(index)
        self.fill_forms(contact)
        wd.find_element_by_xpath("(.//input[@name='update'])[1]").click()
        self.contact_cache = None

    def select_modified_contact_by_index(self, index):
        wd = self.app.wd
        elements = wd.find_elements_by_xpath(".//img[@title='Edit']")
        elements[index].click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list_page()
        return len(wd.find_elements_by_name("entry"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list_page()
            self.contact_cache = []
            for el in wd.find_elements_by_name("entry"):
                id = el.find_element_by_name("selected[]").get_attribute("value")
                lname = el.find_element_by_xpath("(td)[2]").text
                fname = el.find_element_by_xpath("(td)[3]").text
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id))
        return list(self.contact_cache)
