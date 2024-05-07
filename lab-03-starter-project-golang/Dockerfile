FROM golang:latest AS builder

COPY go.mod go.sum ./
RUN go mod download

WORKDIR /app
COPY . /app

RUN CGO_ENABLED=0 GOOS=linux go build -o build/fizzbuzz

FROM scratch

COPY --from=builder /app/build/fizzbuzz /

COPY --from=builder /app/templates/index.html /templates/

EXPOSE 8080

CMD ["/fizzbuzz", "serve"]