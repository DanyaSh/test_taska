FROM nginx:latest

# Удалите стандартную конфигурацию Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем шаблон конфигурационного файла Nginx
COPY server.conf_tpl /etc/nginx/conf.d/server.conf

# Указываем порты, на которых будет работать Nginx и SSL
EXPOSE 443
EXPOSE 9191

# Указание рабочей директории
WORKDIR /etc/nginx

# Запускаем команду для запуска Nginx
CMD ["nginx", "-g", "daemon off;"]