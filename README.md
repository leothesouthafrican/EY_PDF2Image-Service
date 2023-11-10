# PDF to Image Microservice

This microservice is responsible for converting PDF files to images.

## How It Works

The service listens for HTTP POST requests with a PDF file attached. Upon receiving a PDF, it converts the PDF into an image and responds with the image in JPEG format.

## Usage

To convert a PDF to an image, make a POST request to the `/convert` endpoint with the PDF file attached.

### Example:

```bash
curl -X POST -F 'pdf=@/path/to/your/document.pdf' http://localhost:5001/convert --output output.jpg
```

## Building and Running with Docker

To build and run the microservice using Docker, follow these steps:

1. Ensure Docker is installed on your system. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop).

2. Build the Docker image by running the following command in your terminal:

```bash
docker build -t pdf-to-image-microservice .
docker run -p 5001:5001 pdf-to-image-microservice