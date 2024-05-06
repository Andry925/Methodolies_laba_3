FROM golang:latest

COPY go.mod go.sum ./
RUN go mod download

WORKDIR /app
COPY . /app

RUN go build -o build/fizzbuzz

EXPOSE 8080
CMD ["./build/fizzbuzz", "serve"]