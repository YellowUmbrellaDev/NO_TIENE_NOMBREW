FROM alpine:latest
RUN apk add --no-cache webhook git docker-cli curl
CMD ["-hooks=/etc/webhook/hooks.json", "-verbose", "-template"]
ENTRYPOINT ["/usr/bin/webhook"]
