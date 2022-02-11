FROM node:10.4.3
WORKDIR /usr/src/app
COPY package*.json ./
ADD package.json /usr/src/app/package.json
RUN npm install
RUN npm install react-scripts@1.1.0 -g
COPY . .
EXPOSE 3000
CMD ["npm ","start"];
# ----------------------------------

FROM nginx:1.19.0
COPY build/ /usr/share/nginx/html