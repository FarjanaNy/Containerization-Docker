# BASE IMAGE
#This is a single stage, but alias is set to show how multistage works (will become clear in multi-stage project)

FROM ubuntu AS build

RUN apt-get update && apt-get install -y golang-go

ENV GO111MODULE=off
WORKDIR /myproject
COPY . /myproject

RUN CGO_ENABLED=0 go build -o /app .

ENTRYPOINT ["/app"]
