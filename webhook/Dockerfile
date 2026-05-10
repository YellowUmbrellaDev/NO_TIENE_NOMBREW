FROM alpine:latest
RUN apk add --no-cache webhook git docker-cli curl
COPY hooks.json /etc/webhook/hooks.json
COPY deploy.sh /etc/webhook/deploy.sh
RUN chmod +x /etc/webhook/deploy.sh
CMD ["-hooks=/etc/webhook/hooks.json", "-verbose", "-template"]
ENTRYPOINT ["/usr/bin/webhook"]
