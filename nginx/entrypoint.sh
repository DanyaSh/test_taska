#!/bin/bash

# Заменяем переменные окружения в шаблоне и сохраняем результат
envsubst '$PROXY_PASS $DOMEN $WEBHOOK_PATH $SSL_KEY $SSL_CERT' < /etc/nginx/conf.d/server.conf_tpl > /etc/nginx/conf.d/server.conf

# Запускаем nginx в foreground режиме
exec nginx -g 'daemon off;'

