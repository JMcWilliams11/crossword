from flask import *

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def main_route():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

