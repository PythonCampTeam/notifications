#!/bin/bash

# Check if rabbit and redis are up and running before starting the service.
echo ${RABBIT_HOST}
until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    echo "${RABBIT_HOST}- waiting rabbitmq from host...."
    sleep 1
    echo ${PYTHONPATH}
done

# Run the service
echo ${PYTHONPATH}
nameko run --config /notifications/config/config.yml rpc.endpoints
