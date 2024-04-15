FROM node:18.20.1-alpine
RUN mkdir /project
WORKDIR /project
COPY package.json yarn.lock /project/
RUN yarn 
COPY . /project
EXPOSE 4200
CMD ng serve --host 0.0.0.0 --port 4200