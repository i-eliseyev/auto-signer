from PIL import Image
from PIL.PngImagePlugin import PngImageFile


def sign(image: PngImageFile):
    sign_fixed_width = 150
    prin_fixed_width = 200
    sign = Image.open('sign.png')
    width_percent_sign = (sign_fixed_width / float(sign.size[0]))
    height_size_sign = int((float(sign.size[0]) * float(width_percent_sign)))
    _print = Image.open('print.png')
    width_percent_print = (prin_fixed_width / float(_print.size[0]))
    height_size_print = int((float(_print.size[0]) * float(width_percent_print)))

    sign = sign.resize((sign_fixed_width, height_size_sign))
    _print = _print.resize((prin_fixed_width, height_size_print))
    image.paste(sign, (250, 1190),  sign)
    image.paste(_print, (400, 1190), _print)
    image.filename = image.filename[:-3] + 'pdf'
    return image