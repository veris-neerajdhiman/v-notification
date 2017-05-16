FROM django

WORKDIR /v-notify

ADD ./requirements/base.txt /v-notify/requirements/base.txt


RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt

ADD . /v-notify
