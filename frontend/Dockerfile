FROM node:18.20.1 as builder
RUN mkdir /project
WORKDIR /project
COPY package.json yarn.lock ./
RUN yarn add -g @angular/cli
RUN yarn install
COPY . .
RUN yarn build
EXPOSE 4200
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
