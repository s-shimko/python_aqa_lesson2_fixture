# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact_page(Contact(firstname="firstname", middlename="middlename",
                                         lastname="lastname", nickname="nickname",
                                         title="title", company="company", address="address",
                                         home="home", mobile="mobile", work="work",
                                         fax="fax", email="email", homepage="homepage",
                                         address2="address2", phone2="phone2", notes="notes"))
    app.logout()

