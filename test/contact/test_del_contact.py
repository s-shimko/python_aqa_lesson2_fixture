from model.contact import Contact

def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                       lastname="lastname", nickname="nickname",
                       title="title", company="company", address="address",
                       home="home", mobile="mobile", work="work",
                       fax="fax", email="email", homepage="homepage",
                       address2="address2", phone2="phone2", notes="notes")))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
