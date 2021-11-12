from flask import Flask

from di import DIManager
from port.adapter.resource.blog import BlogResource
from port.adapter.resource.home import HomeResource
from port.adapter.resource.search import SearchResource

di_manager = DIManager()

APP = Flask(__name__, static_folder="templates/static")
APP.config['JSON_AS_ASCII'] = False

APP.register_blueprint(HomeResource)
APP.register_blueprint(SearchResource)
APP.register_blueprint(BlogResource)

if __name__ == "__main__":
    # API(Flask)を起動
    APP.run(host='0.0.0.0', debug=True)
