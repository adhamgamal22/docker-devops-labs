FROM alpine:3.19

WORKDIR /app

COPY app.sh .

RUN chmod +x app.sh

HEALTHCHECK --interval=5s --timeout=3s --retries=2 \
  CMD test -f /tmp/healthy || exit 1

CMD ["./app.sh"]