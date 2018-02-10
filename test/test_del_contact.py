from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                       lastname="lastname", nickname="nickname",
                       title="title", company="company", address="address",
                       home="home", mobile="mobile", work="work",
                       fax="fax", email="email", homepage="homepage",
                       address2="address2", phone2="phone2", notes="notes")))
    app.contact.delete_first_contact()
