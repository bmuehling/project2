FROM node:24-alpine

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./

RUN npm ci

COPY . ./

RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "start"]

