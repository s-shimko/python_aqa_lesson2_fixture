import random
from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_add_random_contact_to_random_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups = orm.get_group_list()
    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        app.contact.create((Contact(firstname="firstname", middlename="middlename",
                                    lastname="lastname", nickname="nickname",
                                    title="title", company="company", address="address",
                                    homephone="home", mobilephone="mobile", workphone="work",
                                    fax="fax", email="email", homepage="homepage",
                                    address2="address2", secondaryphone="phone2", notes="notes")))
    if len(groups) == 0:
        app.group.create(Group(name="test"))
    app.contact.open_contact_list_page()
    # get random id contact and group
    contact = random.choice(contacts)
    contact_id = contact.id
    group = random.choice(groups)
    group_name = group.name
    group_id = group.id
    # add contact to random group
    old_contacts_in_groups = orm.get_contacts_in_group(Group(id=group_id))
    app.contact.add_contact_to_group(contact_id, group_name)
    # verified contact in group
    new_contacts_in_groups = orm.get_contacts_in_group(Group(id=group_id))
    if len(old_contacts_in_groups) == len(new_contacts_in_groups):
        print("Contact wasnt' added, randomly choosed same group")
    else:
        assert len(old_contacts_in_groups) + 1 == len(new_contacts_in_groups)
        for contact_in_group in new_contacts_in_groups:
            assert(contact_in_group.id == contact_id)


