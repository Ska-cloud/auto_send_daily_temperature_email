from jinja2 import Environment, FileSystemLoader


class GenerateEmailTemplate:
    def __init__(self):
        file_loader = FileSystemLoader('./static')
        env = Environment(loader=file_loader)
        template = env.get_template('template.html')
        self.template = template

    def render(self, **kwargs):
        email_template = self.template.render(kwargs)

        return email_template


if __name__ == '__main__':
    generate_email_template = GenerateEmailTemplate()
    generate_email_template.render()
