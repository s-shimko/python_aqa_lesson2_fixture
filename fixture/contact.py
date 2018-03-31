from model.contact import Contact
import re
from selenium.webdriver.support.ui import Select

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

        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)

        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)

        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)

        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)

        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)

        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)

        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)

        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)

        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)

        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondaryphone)

        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath(".//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_modified_contact_by_index(index)
        self.fill_forms(contact)
        wd.find_element_by_xpath("(.//input[@name='update'])[1]").click()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_modified_contact_by_id(id)
        self.fill_forms(contact)
        wd.find_element_by_xpath("(.//input[@name='update'])[1]").click()
        self.contact_cache = None

    def select_modified_contact_by_index(self, index):
        wd = self.app.wd
        elements = wd.find_elements_by_xpath(".//img[@title='Edit']")
        elements[index].click()

    def select_modified_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

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
                cells = el.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                id = el.find_element_by_name("selected[]").get_attribute("value")
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_list_page()
        self.select_modified_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       address=address,
                       email=email, email2=email2, email3=email3)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_list_page()
        el = wd.find_elements_by_name("entry")[index]
        cell = el.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group(self, contact_id, group_name):
        wd = self.app.wd
        self.open_contact_list_page()
        self.set_checkbox_contact_by_id(contact_id)
        self.select_group_by_name(group_name)
        wd.find_element_by_name("add").click()

    def set_checkbox_contact_by_id(self, contact_id):
        wd = self.app.wd
        wd.find_element_by_id("%s" % contact_id).click()

    def select_group_by_name(self, group_name):
        wd = self.app.wd
        Select(wd.find_element_by_xpath(".//select[@name='to_group']")).select_by_visible_text(group_name)

    def delete_contact_from_group(self, contact_id, group_name):
        wd = self.app.wd
        self.choose_group_where_contacts(group_name)
        self.set_checkbox_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()

    def choose_group_where_contacts(self, group_name):
        wd = self.app.wd
        Select(wd.find_element_by_xpath(".//select[@name='group']")).select_by_visible_text(group_name)
