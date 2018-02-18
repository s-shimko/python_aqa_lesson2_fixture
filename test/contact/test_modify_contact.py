from model.contact import Contact

def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname_edited", middlename="_edited",
                                             lastname="lastname_edited", nickname="_edited",
                                             title="_edited", company="_edited", address="_edited",
                                             home="_edited", mobile="mobile", work="work",
                                             fax="_edited", email="_edited", homepage="_edited",
                                             address2="_edited", phone2="_edited", notes="_edited")

    # contact = Contact(firstname="firstname_edited", lastname="lastname_edited")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                       lastname="lastname", nickname="nickname",
                       title="title", company="company", address="address",
                       home="home", mobile="mobile", work="work",
                       fax="fax", email="email", homepage="homepage",
                       address2="address2", phone2="phone2", notes="notes")))
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
