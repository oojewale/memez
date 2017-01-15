from views import MemeForm, MemeGenerator
from flask import send_from_directory


def send_memes(path):
  return send_from_directory('tmp', path)

def setup_routes(app):
  app.add_url_rule('/', view_func=MemeForm.as_view('index'))
  app.add_url_rule('/create', view_func=MemeGenerator.as_view('create'))
  app.add_url_rule('/meme/<path:path>', view_func=send_memes)
