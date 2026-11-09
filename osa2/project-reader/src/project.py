class Project:
    def __init__(self, name, description, dependencies, dev_dependencies,
                 license_name="-", authors=None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license_name = license_name
        self.authors = authors or []

    def __str__(self):
        lines = [
            f"Name: {self.name}",
            f"Description: {self.description or '-'}",
            f"License: {self.license_name}",
            "", "Authors:",
        ]
        lines.extend(f"- {name}" for name in self.authors)
        lines.extend(["", "Dependencies:"])
        lines.extend(f"- {name}" for name in self.dependencies)
        lines.extend(["", "Development dependencies:"])
        lines.extend(f"- {name}" for name in self.dev_dependencies)
        return "\n".join(lines)
