from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password, url):
        client = Client(url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_projects(self, username, password, url):
        client = Client(url + "/api/soap/mantisconnect.php?wsdl")
        try:
            list = []
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for p in projects:
                list.append(Project(name=p.name, id=p.id))
            return list
        except WebFault:
            return None