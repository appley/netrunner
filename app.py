from flask import render_template, request, jsonify, Flask, url_for, redirect
import netrunner_request

app = Flask(__name__)

@app.route('/')
def index():
    images = netrunner_request.get_card_IDs(netrunner_request.getCards(netrunner_request.netrunnerdb_URL))
    return render_template('index.html', images=images)

@app.route('/data_and_destiny')
def data_and_destiny():
    images = netrunner_request.get_data_and_destiny(netrunner_request.getCards(netrunner_request.netrunnerdb_URL))
    return render_template('data_and_destiny.html', images=images)


@app.route('/universe_of_tomorrow')
def universe_of_tomorrow():
    images = netrunner_request.get_universe_of_tomorrow(netrunner_request.getCards(netrunner_request.netrunnerdb_URL))
    return render_template('universe_of_tomorrow.html', images=images)



if __name__ == "__main__":

    app.run(debug=True)
