FROM python:2.7-alpine

MAINTAINER SOFTWAY4IoT Project "softway4iot@gmail.com"

ARG AGENT_PORT=9091
ENV SW4IOT_AGENT_PORT=$AGENT_PORT

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE $SW4IOT_AGENT_PORT

ENTRYPOINT ["python"]

CMD ["app/main.py"]