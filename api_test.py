#api_test.py

import requests

# The endpoint you're going to post to
url = 'http://localhost:5000/convert'

# The path to the PDF file you want to convert
file_path = '/workspaces/EY_PDF2Image-Service/invoices/BADENOCH&CLARK 51 16.02.18_EUR.pdf'

# The actual POST request
with open(file_path, 'rb') as pdf_file:
    files = {'pdf': (pdf_file.name, pdf_file, 'application/pdf')}
    response = requests.post(url, files=files)

# Save the received image to a file, if the request was successful
if response.status_code == 200:
    with open('/workspaces/EY_PDF2Image-Service/output/image_from_api.jpg', 'wb') as f:
        f.write(response.content)
    print("Image saved successfully")
else:
    print(f"Failed to convert PDF. Status code: {response.status_code}, Response: {response.text}")