FROM node:12-alpine as builder
WORKDIR /app
COPY package*.json /app
RUN npm install
COPY . /app
RUN npm run build

FROM nginx:alpine
# ----------------------------------

# Clean nginx
RUN rm -rf /usr/share/nginx/html/*

# Copy dist
COPY --from=builder /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/default.conf

WORKDIR /usr/share/nginx/html

# Permission
RUN chown root /usr/share/nginx/html/*
RUN chmod 755 /usr/share/nginx/html/*

# Expose port
EXPOSE 4200

# Start
CMD ["nginx", "-g", "daemon off;"]