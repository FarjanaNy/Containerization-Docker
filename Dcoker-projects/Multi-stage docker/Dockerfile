# Builder stage (uses official Go image)
FROM golang:1.20 AS build
WORKDIR /projectscr

# If you're using Go modules, copy go.mod first (cache deps)
COPY go.mod go.sum ./
RUN go mod download

# Copy app source
COPY . /projectscr

# Build static binary
ENV CGO_ENABLED=0
RUN go build -o /app .

# Final stage — minimal
FROM scratch
COPY --from=build /app /app
ENTRYPOINT ["/app"]
