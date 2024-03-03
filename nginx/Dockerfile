FROM nginx:latest

# Удаляем стандартный конфигурационный файл nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем шаблон конфигурационного файла и entrypoint скрипт
COPY server.conf_tpl /etc/nginx/conf.d/server.conf_tpl
COPY entrypoint.sh /entrypoint.sh

# Делаем entrypoint скрипт исполняемым
RUN chmod +x /entrypoint.sh

# Указываем порты, на которых будет работать Nginx и SSL
EXPOSE 443

# Устанавливаем рабочую директорию
WORKDIR /etc/nginx

# Устанавливаем entrypoint скрипт
ENTRYPOINT ["/entrypoint.sh"]

# Запускаем Nginx в foreground режиме
CMD ["nginx", "-g", "daemon off;"]
