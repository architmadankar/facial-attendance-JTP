#docker-compose build --no-cache

FROM node:18.20.1-alpine as stage-1
RUN mkdir /project
WORKDIR /project
COPY package.json yarn.lock /project/
RUN yarn add global @angular/cli
COPY . /project
RUN yarn run build
# EXPOSE 4200
# CMD ng serve --host 0.0.0.0 --port 4200

#TODO : Nginx portforward
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=stage-1 /project/dist/frontend-v2/browser .

ENTRYPOINT [ "nginx", "-g", "daemon off;"]