FROM node:17-alpine

WORKDIR /app

# which port
EXPOSE 3000

COPY package.json package-lock.json ./

RUN npm install 

COPY . ./

# executable name, parameter 
CMD ["npm", "start"]