#!/bin/bash

CURL=$(which curl)
CURL_OPT="-sSLI"

FLASK_IPADDR=
FLASK_PORT=$(cat settings/flask.ini | grep "FLASK_PORT" | cut -d = -f 2)

ENDPOINT=( ""
           "__health"
           "__count"
           "__notfound"
)

for EP in "${ENDPOINT[@]}"
do
  ${CURL} ${CURL_OPT} http://localhost:${FLASK_PORT}/${EP} -o /dev/null -w '%{http_code}\n'
done
