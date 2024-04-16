#docker-compose build --no-cache

FROM node:18.20.1-alpine as stage-1
RUN mkdir /project
WORKDIR /project
COPY package.json yarn.lock /project/
RUN yarn global add @angular/cli
COPY . /project
RUN yarn 
# EXPOSE 8080
# CMD yarn start --port 8080

#TODO : Nginx portforward
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=stage-1 /project/dist/frontend-v2/browser .

ENTRYPOINT [ "nginx", "-g", "daemon off;"]