FROM nginx:alpine

WORKDIR /app

ARG VERSION=v1

RUN echo "<h1>Application Version: ${VERSION}</h1>" > /usr/share/nginx/html/index.html

EXPOSE 80