from flask import render_template, request, jsonify, Flask, url_for, redirect
import netrunner_request

app = Flask(__name__)

@app.route('/')
def index():
    images = netrunner_request.get_data_and_destiny_triples(netrunner_request.getCards(netrunner_request.netrunnerdb_URL))
    return render_template('index.html', images=images)

@app.route('/data_and_destiny')
def data_and_destiny():
    return render_tempate('data_and_destiny.html')


@app.route('/universe_of_tomorrow')
def universe_of_tomorrow():
    return render_tempate('universe_of_tomorrow.html')



if __name__ == "__main__":

    app.run(debug=True)
