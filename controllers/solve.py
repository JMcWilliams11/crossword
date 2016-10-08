from flask import *
import requests
import bs4
import validators

solve = Blueprint('solve', __name__, template_folder='templates')

@solve.route('/solve', methods=['POST'])
def solve_route():
    #puzzleUrl = new york times crossword puzzle url
    puzzleUrl = request.form['url']
    if validators.url(puzzleUrl) :
        req = requests.get(puzzleUrl)
    else :
        options = {
            'goodUrl': False
        }
        return render_template("index.html", **options)
    if req.status_code == requests.codes.ok :
        puzzleSoup = bs4.BeautifulSoup(req.text)
        grid = puzzleSoup.select('.flex-row')
        clueLists = puzzleSoup.select('.clue-list-wrapper')
        options = {
            'result': grid
        }

    else :
        options = {
            'goodUrl': False
        }
        return render_template("index.html", **options)

    return render_template("solve.html", **options)