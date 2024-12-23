from flask import Flask
from views import *


class Flaskapp:
   def __init__(self):
      self.app = Flask(__name__)
      self._registro_bluepoint()

   def _registro_bluepoint(self):
      self.app.register_blueprint(main_rotas)



app = Flaskapp().app

app.run(debug=True)