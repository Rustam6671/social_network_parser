FROM nginx:1.19.5-alpine
RUN mkdir -p /home/www
ENV APP_HOME=/home/www
RUN addgroup -S www && adduser -S www -G www
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d