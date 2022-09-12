
FROM python:slim

RUN useradd auto-signer

WORKDIR /home/auto-signer

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY auto_signer.py main.py print.png sign.png config.py boot.sh wsgi.py ./
RUN chmod a+x boot.sh

ENV FLASK_APP auto-signer.py

RUN chown -R auto-signer:auto-signer ./
USER auto-signer

EXPOSE 5002
ENTRYPOINT ["./boot.sh"]