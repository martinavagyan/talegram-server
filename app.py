from flask import Flask, render_template,request, send_file
app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getstory') # this is a job for GET, not POST
def plot_csv():
    return app.send_static_file('docs/AmazingStory/story.tale')


if __name__ == "__main__":
	app.run()