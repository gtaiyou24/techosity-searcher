FROM python:3.9

MAINTAINER gtaiyou24 gtaiyou24@gmail.com

ENV TZ=Asia/Tokyo

ARG project_dir=/app/
COPY . $project_dir
WORKDIR $project_dir

RUN pip install --upgrade pip && pip install -r requirements.txt

#ENTRYPOINT ["python", "start_flask.py"]