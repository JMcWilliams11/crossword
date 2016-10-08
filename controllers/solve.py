from flask import *

solve = Blueprint('solve', __name__, template_folder='templates')

@solve.route('/solve', methods=['POST'])
def solve_route():

    #change this
    result = 'null'
    options = {
        'result': result
    }
    return render_template("solve.html", **options)