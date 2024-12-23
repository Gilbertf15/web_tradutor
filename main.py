from flask import Flask
from views import *


class Flaskapp:
   def __init__(self):
      self.app = Flask(__name__)
      self._registro_bluepoint()

   def _registro_bluepoint(self):
      self.app.register_blueprint(main_rotas)

   def run(self, host='127.0.0.1', port=5000, debug=False):
      self.app.run(host=host, port=port, debug=debug)

app = Flaskapp()
if __name__ == '__main__':
   app.run(debug=True)