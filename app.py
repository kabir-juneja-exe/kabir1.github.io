from flask import Flask,render_template
from routes.text_captcha import text_captcha_bp
from routes.math_captcha import math_captcha_bp
from routes.slider_captcha import slider_captcha_bp
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Register the blueprints
app.register_blueprint(text_captcha_bp)
app.register_blueprint(math_captcha_bp)
app.register_blueprint(slider_captcha_bp)

@app.route('/slider')
def slider_captcha():
    return render_template("slider_captcha.html")
@app.route("/math")
def math_captcha_page():
    return render_template("math_captcha.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

