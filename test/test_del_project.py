# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.create(Project(name="name123"))
    old_projects = app.project.get_project_list()
    random_project = random.choice(old_projects)
    app.project.delete_project_by_name(random_project.name)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.remove(random_project)
    assert old_projects == new_projects