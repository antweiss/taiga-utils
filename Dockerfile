from python:alpine
RUN apk -U --no-cache add bash build-base ca-certificates
RUN pip install python-taiga
RUN adduser -D bundle
USER bundle
WORKDIR /home/bundle
COPY . /home/bundle
