"""
Request router for maxnelso site.
"""

from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app
from src.common import render_template

class HomeHandler(RequestHandler):
  def get(self):
    return self.response.out.write(render_template('home.html'))

application = WSGIApplication([('/', HomeHandler)], debug=True)

if __name__ == '__main__':
  run_wsgi_app(application)
