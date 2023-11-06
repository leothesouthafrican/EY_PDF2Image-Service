# PDF to Image Microservice

This microservice is responsible for converting PDF files to images.

## How It Works

The service listens for HTTP POST requests with a PDF file attached. Upon receiving a PDF, it converts the PDF into an image and responds with the image in JPEG format.

## Usage

To convert a PDF to an image, make a POST request to the `/convert` endpoint with the PDF file attached.

### Example:

```bash
curl -X POST -F 'pdf=@/path/to/your/document.pdf' http://localhost:4000/convert --output output.jpg