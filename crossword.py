from flask import Flask, render_template, session
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.main)

#### Global Constants
# UPLOAD_FOLDER = '/static/images/images'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    app.run()