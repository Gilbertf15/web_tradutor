from flask import Flask
from views import *


class Flaskapp:
   def __init__(self, name):
      self.app = Flask(name)
      self._registro_bluepoint()

   def _registro_bluepoint(self):
      self.app.register_blueprint(main_rotas)

   def run(self, host='127.0.0.1', port=5000, debug=False):
      self.app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
   global app
   app = Flaskapp(__name__)
   app.run(debug=True)