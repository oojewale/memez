from flask import views, render_template, request
from utils import make_image_mash


class MemeGenerator(views.MethodView):
  def post(self):
    title = request.form.get('title')
    image = request.files.get('image')
    meme = make_image_mash(title, image)
    return render_template('index.html', meme=meme)