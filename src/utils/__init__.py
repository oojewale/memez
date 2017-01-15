import os
import uuid

from PIL import Image, ImageDraw, ImageFont


def make_image_mash(title, image):
  """
    Overlay text on image
  """
  base = Image.open(image).convert('RGBA')
  txt = Image.new('RGBA', base.size, (255, 255, 255, 0))
  fnt = ImageFont.truetype(os.path.join(
    '/Users/mattwal/Documents/olaide/workspace/python/flask_projects/me-mes/src',
    'fonts/arial.ttf'),
     40)
  image_draw = ImageDraw.Draw(txt)
  image_draw.text((10, 10), title, fill=(255,255,225,255), font=fnt)
  out = Image.alpha_composite(base, txt)
  fname = '{}.png'.format(uuid.uuid1())
  fpath = os.path.join(
    '/Users/mattwal/Documents/olaide/workspace/python/flask_projects/me-mes/src',
    'tmp',
    fname)
  out.save(fpath)
  return fname