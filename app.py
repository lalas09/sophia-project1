from flask import Flask, render_template, flash, redirect, url_for, request
from forms import TextForm
from config import Config
from interactive_english_dic import translate

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=["GET", "POST"])
#@app.route('/index')
def home():
	form = TextForm()
	displayed_results = request.args.getlist("results") or ""
	print("displayed_results", displayed_results)
	if form.validate_on_submit():
		print("form_data", form.text.data)
		results = translate(form.text.data)
		print("results", results)
		return redirect(url_for("home", results = results))
	else:
		print("This did not work, please mnake sure your text is at least one character long")
	return render_template("home.html", form = form, results = displayed_results)

@app.route('/about/')
def about():
	return render_template("about.html")

if __name__=="__main__":
	app.run(debug=True)

#go to the right directory
#py -m venv env
#env\Scripts\activate
#pip install flask
#set FLASK_APP=app.py (or whatevER the file name is)
#flask run

#*if that doesn't work - do python app.py (or whatever the file name is)









