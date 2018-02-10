from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(Group(name="modified_group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test_header"))
    app.group.modify_first_group(Group(header="modified_header"))
