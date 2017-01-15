from flask import views, render_template


class MemeForm(views.MethodView):
  def get(self):
    return render_template('index.html')