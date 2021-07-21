from flask import Flask
from flask_restx import Api
from main.controller.search import api as search
from main.controller.auth import api as auth
from main.controller.user import api as user

app = Flask(__name__)

apis = Api(
    app,
    version='1.0',
    title="Sogang-Register API Server",
    description="Team Facade's Sogang-Register API Server!",
    terms_url="/",
    contact="sonicdx886@gmail.com",
    license="MIT"
)

apis.add_namespace(search, '/search')
apis.add_namespace(auth, '/auth')
apis.add_namespace(user, '/user')

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=80)