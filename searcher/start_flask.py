from flask import Flask

from port.adapter.resource.home import HomeResource
from port.adapter.resource.search import SearchResource

APP = Flask(__name__, static_folder="templates/static")
APP.config['JSON_AS_ASCII'] = False

APP.register_blueprint(HomeResource)
APP.register_blueprint(SearchResource)

if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
