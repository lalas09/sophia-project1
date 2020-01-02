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
	displayed_message = request.args.get("message") or ""
	message = ""
	results = []
	print("displayed_results", displayed_results)
	if form.validate_on_submit():
		print("form_data", form.text.data)
		form_results = translate(form.text.data)
		if type(form_results) is list:
			results = form_results
		else:
		    message = form_results
		print("form_results", form_results)
		return redirect(url_for("home", results = results, message = message))
	else:
		return render_template("home.html", form = form, results = displayed_results, message = displayed_message)
		print("This did not work")
	#	return redirect(url_for("home"))
	#	print("This did not work, please make sure your text is at least one character long")
	return render_template("home.html", form = form, results = displayed_results, message = displayed_message)

@app.route('/faq/')
def faq():
	return render_template("faq.html")

@app.route('/profile/')
def profile():
	return render_template("profile.html")

if __name__=="__main__":
	app.run(host='0.0.0.0',debug=True)

#go to the right directory
#py -m venv env
#env\Scripts\activate
#pip install flask
#set FLASK_APP=app.py (or whatevER the file name is)
#flask run

#*if that doesn't work - do python app.py (or whatever the file name is)



#ssh root@ (ip address)
#enter password









