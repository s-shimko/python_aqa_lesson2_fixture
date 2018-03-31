import random
from fixture.contact import Contact
from fixture.group import Group
from fixture.orm import ORMFixture


def test_del_random_contact_from_group(app, db):
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
    # check contacts in group presence
    contacts_in_group = db.get_all_contacts_in_group()
    if len(contacts_in_group) == 0:
        # add contact in group
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
                assert (contact_in_group.id == contact_id)

    # delete random contact from group
    contacts_in_group = db.get_all_contacts_in_group()
    contact_in_group = random.choice(contacts_in_group)
    contact_id = contact_in_group.id
    group_id = contact_in_group.group_id
    # get group name
    group_name = None
    print("-------> " + str(groups))
    for g in groups:
        if str(g.id) == str(group_id):
            group_name = g.name
    if group_name == None:
        raise ValueError("Can't find group_id")
    print("-------> " + str(group_name))
    app.contact.delete_contact_from_group(contact_id, group_name)
    contacts_in_groups_after_deletion = db.get_all_contacts_in_group()
    assert len(contacts_in_group) - 1 == len(contacts_in_groups_after_deletion)
