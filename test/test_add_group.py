# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="gr_name1", header="gr_header", footer="gr_footer"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
