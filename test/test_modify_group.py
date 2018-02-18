from model.group import Group

def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="modified_group")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="test_group"))
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(header="test_header"))
#     app.group.modify_first_group(Group(header="modified_header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
