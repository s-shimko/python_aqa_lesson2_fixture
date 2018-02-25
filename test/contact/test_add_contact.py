# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="middlename",
                      lastname="lastname", nickname="nickname",
                      title="title", company="company", address="address",
                      homephone="home", mobilephone="mobile", workphone="work",
                      fax="fax", email="email", email2="email2", email3="email3",
                      homepage="homepage",
                      address2="address2", secondaryphone="phone2", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

