import io
import os
import zipfile
from pdf2image import convert_from_bytes
from flask import render_template, request, url_for, redirect,  flash, send_file
from werkzeug.utils import secure_filename

from app import app
from main import sign

UPLOAD_EXTENSIONS = ['.pdf']


@app.route('/')
def index():
    return render_template('basic_upload_form.html')


@app.route('/', methods=['POST'])
def upload_file():
    signed_pil_obj = []
    for uploaded_file in request.files.getlist('file'):
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in UPLOAD_EXTENSIONS:
                flash("Загружаемые файлы могут иметь расширение только .pdf")
                return redirect(url_for('index'))
            raw_png_file = convert_from_bytes(uploaded_file.stream.read(), fmt='png')[0]
            filename = os.path.splitext(filename)[0] +'.png'
            raw_png_file.filename = filename
            signed_pil_obj.append(sign(raw_png_file))

    def get_file_buf(file):
        file_object = io.BytesIO()
        file.save(file_object, 'PDF')
        file_object.seek(0)
        return file_object

    list_of_tuples = [(_.filename, get_file_buf(_)) for _ in signed_pil_obj]

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_name, data in list_of_tuples:
            zip_file.writestr(file_name, data.read())
    zip_buffer.seek(0)
    zip_buffer.seek(0)
    return send_file(zip_buffer,
            mimetype ='zip',
            download_name='signed_docs.zip',
            as_attachment=True)

    # with open('test.zip', 'wb') as f:
    #     f.write(zip_buffer.getvalue())
    # return redirect(url_for('index'))
