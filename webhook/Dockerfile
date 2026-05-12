FROM alpine:latest
RUN apk add --no-cache webhook git curl openssh-client
# Añadir la huella de GitHub para que SSH no pida confirmación interactiva
RUN mkdir -p /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts
COPY hooks.json /etc/webhook/hooks.json
COPY deploy.sh /etc/webhook/deploy.sh
RUN chmod +x /etc/webhook/deploy.sh
CMD ["-hooks=/etc/webhook/hooks.json", "-verbose", "-template"]
ENTRYPOINT ["/usr/bin/webhook"]