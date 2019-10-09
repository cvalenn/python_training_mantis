# -*- coding: utf-8 -*-


def test_login(app):
    assert app.session.get_logged_user() == "administrator"