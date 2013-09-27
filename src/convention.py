# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
import sys
import os

#Put lib on path, once Google App Engine does not allow doing it directly
import tmpl

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import webapp2
from zen import router
from zen.router import PathNotFound

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))


def _extract_values(handler, param, default_value=''):
    values = handler.request.get_all(param)
    if param.endswith('[]'):
        return param[:-2], values if values else []
    else:
        if not values: return param, default_value
        if len(values) == 1: return param, values[0]
        return param, values


class BaseHandler(webapp2.RequestHandler):
    fcn, params, kwargs = None, None, None

    def get(self):
        self.make_convetion()

    def post(self):
        self.make_convetion()

    def make_convetion(self):
        kwargs = dict(_extract_values(self, a) for a in self.request.arguments())

        def write_tmpl(template_name, values={}):
            self.response.write(tmpl.render(template_name, values))

        convention_params = {'_req': self.request,
                             '_resp': self.response,
                             '_handler': self,
                             '_write_tmpl': write_tmpl
        }
        convention_params['_dependencies'] = convention_params
        try:
            fcn, params = router.to_handler(self.request.path, convention_params, **kwargs)
            fcn(*params, **kwargs)

        except PathNotFound:
            self.response.status_code = 404
            logging.error('Path not Found: ' + self.request.path)
        except Exception, e:
            self.response.status_code = 400
            logging.exception(e)


app = webapp2.WSGIApplication([('/.*', BaseHandler)], debug=False)

