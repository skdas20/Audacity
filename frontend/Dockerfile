FROM node:18-alpine

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* /app/

RUN npm install --legacy-peer-deps --silent

COPY frontend /app

EXPOSE 3000

CMD ["npm", "run", "dev"]
