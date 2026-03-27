from flask import Blueprint, jsonify, send_file, session
from captcha.image import ImageCaptcha
import random
import string
import os

text_captcha_bp = Blueprint("text_captcha", __name__)

# Function to generate random text for CAPTCHA
def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# API Endpoint to generate text CAPTCHA
@text_captcha_bp.route('/generate_text_captcha', methods=['GET'])
def generate_text_captcha():
    captcha_text = generate_captcha_text()
    image = ImageCaptcha(width=280, height=90)
    image_path = f"static/{captcha_text}.png"
    image.write(captcha_text, image_path)

    session['captcha_text'] = captcha_text  # Store in session

    return jsonify({
        "captcha_text": captcha_text,  # (For debugging, remove in production)
        "captcha_url": f"/static/{captcha_text}.png"
    })

# API Endpoint to verify text CAPTCHA
@text_captcha_bp.route('/verify_text_captcha/<user_input>', methods=['GET'])
def verify_text_captcha(user_input):
    if user_input == session.get('captcha_text'):
        return jsonify({"message": "✅ CAPTCHA Verified!"}), 200
    return jsonify({"message": "❌ Incorrect CAPTCHA"}), 400
