from time import sleep

from model.contact import Contact
import random

def test_modify_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                                    lastname="lastname", nickname="nickname",
                                    title="title", company="company", address="address",
                                    homephone="home", mobilephone="mobile", workphone="work",
                                    fax="fax", email="email", homepage="homepage",
                                    address2="address2", secondaryphone="phone2", notes="notes")))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    modified_contact = Contact(firstname="firstname_edited", middlename="_edited",
                      lastname="lastname_edited", nickname="_edited",
                      title="_edited", company="_edited", address="_edited",
                      homephone="_edited", mobilephone="mobile", workphone="work",
                      fax="_edited", email="_edited", email2="_edited", email3="_edited",
                      homepage="_edited",
                      address2="_edited", secondaryphone="_edited", notes="_edited")
    app.contact.modify_contact_by_id(contact.id, modified_contact)
    app.contact.open_contact_list_page()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(modified_contact)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
