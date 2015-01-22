from flask import Flask, url_for, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def api_root():
    if request.method == 'POST':
        movie_name=request.form['movie_name'].strip().replace(" ","+")
        url = "http://www.omdbapi.com/?t={0}&y=&plot=short&r=json".format(movie_name)
        omdb_request = requests.get(url)
        omdb_result = omdb_request.json()
        return render_template("index.html", movie_name=movie_name, omdb_request=omdb_result)
    return render_template("index.html")

def urlFormat(moviename):
    return ''


if __name__ == '__main__':
    app.run(debug = True)

