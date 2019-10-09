from model.project import Project
import urllib.parse as urlparse


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        # submit contact creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_partial_link_text('name'):
                text = element.text
                parsed = urlparse.urlparse(wd.find_element_by_link_text(text).get_attribute("href"))
                id = urlparse.parse_qs(parsed.query)["project_id"][0]
                self.project_cache.append(Project(name=text, id=str(id)))
        return list(self.project_cache)

    def open_projects_page(self):
        wd = self.app.wd
        if not (self.app.base_url.endswith("/manage_overview_page.php") and len(wd.find_elements_by_partial_link_text('name')) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_name(name)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text(name).click()

    def count(self):
        wd = self.app.wd
        self.open_projects_page()
        return len(wd.find_elements_by_partial_link_text('name'))


