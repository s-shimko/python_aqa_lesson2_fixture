from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="_edited", middlename="_edited",
                       lastname="_edited", nickname="_edited",
                       title="_edited", company="_edited", address="_edited",
                       home="_edited", mobile="mobile", work="work",
                       fax="_edited", email="_edited", homepage="_edited",
                       address2="_edited", phone2="_edited", notes="_edited"))
    app.session.logout()