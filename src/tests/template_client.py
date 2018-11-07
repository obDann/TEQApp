import sys
sys.path.append("../temhelp")
from template_handler import TemplateHandler

class TemplateClient():
    
    def __init__(self):
        self._templates = {}
        
    def add_template(self, template_name, TemplateHandler):
        self._templates[template_name] = TemplateHandler
        
    def get_template(self, template_name):
        return self._templates[template_name]