FROM alpine:3.10

LABEL \
  name="csf-client" \
  version="1.0Beta" \
  github="https://github.com/armourbird/csf"

RUN \
  sed -i 's/http\:\/\/dl-cdn.alpinelinux.org/https\:\/\/alpine.global.ssl.fastly.net/g' /etc/apk/repositories && \
  apk add --no-cache \
    iproute2 \
    docker \
    curl \
    ca-certificates \
    dumb-init && \
  rm -rf /usr/bin/docker?*

COPY ./*.sh /usr/local/bin/
COPY ./tests/*.sh /usr/local/bin/tests/

HEALTHCHECK CMD exit 0

WORKDIR /usr/local/bin

ENTRYPOINT [ "/usr/bin/dumb-init", "run-bash.sh" ]
CMD [""]
