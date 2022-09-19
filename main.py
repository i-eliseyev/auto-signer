from PIL import Image
import pytesseract

from app.routes import SignData


def sign(sign_data: SignData) -> tuple:
    image = sign_data.image
    original_filename = sign_data.original_filename

    target = 'Бобылев'
    data = pytesseract.image_to_data(
        image,
        output_type=pytesseract.Output.DICT,
        lang='rus',
    )
    word_occurences = [i for i, word in enumerate(data["text"]) if word == target]
    if len(word_occurences) != 1:
        occ = word_occurences[-1]
    else:
        occ = word_occurences[0]
    l = data["left"][occ]
    t = data["top"][occ]

    print_x = l + 380
    sign_x = l + 30
    print_y = t - 250
    sign_y = t - 200

    print_fixed_width = 280
    sign = Image.open('sign.png')
    _print = Image.open('print.png')
    width_percent_print = (print_fixed_width / float(_print.size[0]))
    height_size_print = int((float(_print.size[0]) * float(width_percent_print)))

    sign = sign.resize((320, 150))
    _print = _print.resize((print_fixed_width, height_size_print))
    image.paste(sign, (sign_x, sign_y),  sign)
    image.paste(_print, (print_x, print_y), _print)
    image.filename = original_filename

    return image, original_filename
