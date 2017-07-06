"""
Constants, utility functions, etc..
"""

__author__ = 'Justin Venezuela (jven@mit.edu), Max Nelson (maxnelso@mit.edu)'

from google.appengine.ext.webapp import template
import os

TEMPLATE_DIR = 'templates'

def render_template(template_name, params = {}):
  template_path = os.path.join(os.path.dirname(__file__), 'templates')
  template_file = os.path.join(template_path, template_name)
  return template.render(template_file, params)
