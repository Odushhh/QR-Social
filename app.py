from flask import Flask, render_template, request, send_file
import qrcode
import json
from io import BytesIO

app = Flask(__name__)

def create_social_qr(platform, handle):
    # Create a dictionary with the selected platform and handle
    social_data = {platform: handle}

    # Convert to JSON
    json_data = json.dumps(social_data)

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(json_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    platform = request.form.get('platform')
    handle = request.form.get('handle')
    if platform and handle:
        qr_image = create_social_qr(platform, handle)
        return send_file(qr_image, mimetype='image/png')
    else:
        return "Please select a platform and enter a handle", 400

if __name__ == '__main__':
    app.run(debug=True)