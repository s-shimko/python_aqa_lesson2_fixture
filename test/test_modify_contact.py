from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                       lastname="lastname", nickname="nickname",
                       title="title", company="company", address="address",
                       home="home", mobile="mobile", work="work",
                       fax="fax", email="email", homepage="homepage",
                       address2="address2", phone2="phone2", notes="notes")))
    app.contact.modify_first_contact(Contact(firstname="_edited", middlename="_edited",
                                             lastname="_edited", nickname="_edited",
                                             title="_edited", company="_edited", address="_edited",
                                             home="_edited", mobile="mobile", work="work",
                                             fax="_edited", email="_edited", homepage="_edited",
                                             address2="_edited", phone2="_edited", notes="_edited"))
