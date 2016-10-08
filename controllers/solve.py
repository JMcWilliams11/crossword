from flask import *
import requests
import bs4

solve = Blueprint('solve', __name__, template_folder='templates')

@solve.route('/solve', methods=['POST'])
def solve_route():
    #puzzleUrl = new york times crossword puzzle url
    puzzleUrl = request.form['url']
    req = requests.get(puzzleUrl)
    if req.status_code == requests.codes.ok:

    else :
        goodUrl = False
        options = {
            'goodUrl': goodUrl
        }

    #change this
    result = 'null'
    options = {
        'result': result
    }
    return render_template("solve.html", **options)