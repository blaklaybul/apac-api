from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api

# Initialize DB extension, but without configuring
# it with an app instance
db = SQLAlchemy()
flask_bcrypt = Bcrypt()
api = Api()

def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        app.config.from_object(config)

    db.init_app(app)
    flask_bcrypt.init_app(app)

    # bind resources to api object BEFORE we Initialize
    # if not, routes will not exists on flask app object
    from .resources.startups import SingleStartup, ListStartups
    from .resource.industries import ListIndustries
    api.add_resource(ListStartups, '/startups')
    api.add_resource(SingleStartup, '/startup/<string:startup_id>')
    api.add_resource(ListIndustries, '/industries')

    api.init_app(app)

    return app
