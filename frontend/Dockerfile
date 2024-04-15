# Stage 1: Build the Angular application
FROM node:18.20.1 as build
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install
COPY . .
RUN yarn run build

# Stage 2: Serve the application with Nginx
FROM nginx:1.19.2-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 4200
CMD ["nginx", "-g", "daemon off;"]