#main.py

from flask import Flask, request, send_file
from pdf2image import convert_from_path
import io
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_image():
    # Check if the request contains 'pdf' as a file
    if 'pdf' not in request.files:
        return "No pdf file found in the request", 400

    pdf_file = request.files['pdf']
    
    if pdf_file.filename == '':
        return "No selected file", 400

    # Save the file to a temporary file
    temp_pdf = "/tmp/temp_file.pdf"  # Temporary file
    pdf_file.save(temp_pdf)

    try:
        # Now we can use the path to the temporary file instead of the FileStorage object
        images = convert_from_path(temp_pdf)
        # Convert to bytes array
        img_byte_arr = io.BytesIO()
        images[0].save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)
        
        return send_file(img_byte_arr, mimetype='image/jpeg')
    except Exception as e:
        return str(e), 500
    finally:
        # Clean up the temporary file
        os.remove(temp_pdf)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
