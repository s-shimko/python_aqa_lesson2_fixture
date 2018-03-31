from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     pass

# print("=======================================")
#
# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass # db.destroy()

# try:
#     l = db.get_contacts_not_in_group(Group(id='90'))
#     for item in l:
#         print(item.name)
#     print(len(l))
# finally:
#     pass  # db.destroy()

# try:
#     l = db.get_all_contacts_in_group()
#     for item in l:
#         print(item.id)
#     print(len(l))
# finally:
#     pass  # db.destroy()