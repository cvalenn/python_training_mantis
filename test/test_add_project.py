# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project(app, data_project):
    project = data_project
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_list_projects(username, password)
    app.project.create(project)
    new_projects = app.soap.get_list_projects(username, password)
    assert len(old_projects) + 1 == app.project.count()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)