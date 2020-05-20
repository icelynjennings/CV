FROM golang:alpine

RUN apk add git curl

RUN go get github.com/gorilla/mux

WORKDIR /go/src/app
COPY . .

EXPOSE 8000

CMD ["go", "run", "dwarves.go"]
