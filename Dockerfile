FROM django
ADD . /v-notify

WORKDIR /v-notify

#RUN apt-get update && apt-get install -y git
RUN pip install -r ./requirements/base.txt
