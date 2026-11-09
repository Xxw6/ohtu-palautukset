import re
from urllib import request
import tomli
from project import Project


def dependency_name(requirement):
    return re.match(r"[A-Za-z0-9_.-]+", requirement).group(0)


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        with request.urlopen(self._url) as response:
            content = response.read().decode("utf-8")
        data = tomli.loads(content)
        project = data["project"]
        dependencies = []
        if project.get("requires-python"):
            dependencies.append("python")
        dependencies.extend(
            dependency_name(item)
            for item in project.get("dependencies", [])
        )
        dev = data.get("dependency-groups", {}).get("dev", [])
        dev_dependencies = [
            dependency_name(item) for item in dev if isinstance(item, str)
        ]
        authors = [author["name"] for author in project.get("authors", [])]
        license_name = project.get("license", "-")
        if isinstance(license_name, dict):
            license_name = license_name.get("text", "-")
        return Project(
            project["name"], project.get("description", ""),
            dependencies, dev_dependencies, license_name, authors,
        )
