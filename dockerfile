FROM alpine:latest

ADD IF.txt home/data/
ADD Limerick.txt home/data/
ADD application.py /home
RUN mkdir -p /home/output/

RUN apk update && \
    apk add --no-cache python3


CMD ["/home/application.py"]
ENTRYPOINT ["python3"]