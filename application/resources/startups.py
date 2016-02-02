from flask.ext.restful import abort
from flask.ext.restful import Resource

class SingleStartup(Resource):

    def get(self, startup_id):
        """Handling GET requests."""
        pass

    def delete(self, startup_id):
        """Handling DELETE requests"""
        pass

class ListStartups(Resource):

    def get(self):
        pass

    def post(self):
        pass
