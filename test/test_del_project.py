# -*- coding: utf-8 -*-
from model.project import Project
import random


def test_del_project(app):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    url = app.config['web']['baseUrl']
    if len(app.soap.get_list_projects(username, password, url)) == 0:
        app.project.create(Project(name="name123"))
    old_projects = app.soap.get_list_projects(username, password, url)
    random_project = random.choice(old_projects)
    app.project.delete_project_by_name(random_project.name)
    assert len(old_projects) - 1 == app.project.count()
    new_projects = app.soap.get_list_projects(username, password, url)
    old_projects.remove(random_project)
    assert old_projects == new_projects