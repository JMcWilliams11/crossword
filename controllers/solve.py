from flask import *
import requests
import bs4

solve = Blueprint('solve', __name__, template_folder='templates')

@solve.route('/solve', methods=['POST'])
def solve_route():
    #puzzleUrl = new york times crossword puzzle url
    puzzleUrl = request.form['url']
    req = requests.get(puzzleUrl)
    if req.status_code == requests.codes.ok :
        puzzleSoup = bs4.BeautifulSoup(req.text)
        grid = puzzleSoup.select('.flex-row')
        cluelist = puzzleSoup.select('.clue-list-wrapper')
        options = {
            'result': grid
        }
        print grid

    else :
        options = {
            'goodUrl': False
        }
        return render_template("index.html", **options)

    return render_template("solve.html", **options)