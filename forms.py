# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, RadioField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    #name = TextField('Name:', validators=[validators.required()])
    sentence = TextField('Sentence:', validators=[validators.required()])
    #options = RadioField('No It is:', validators=[])
    
    #email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    #password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print (form.errors)
    if request.method == 'POST':
        #name=request.form['name']
        sentence=request.form['sentence']
        ans = request.form['options']
        #password=request.form['password']
        #email=request.form['email']
        print (sentence+":"+ans)
 
        if form.validate():
            # Save the comment here.
            if(ans == 'check'):
                #sol = checkSemantics(sentence)
                flash('This sentence is ' + "positive")
            else:
                #tellSemantics(sentence, ans)
                flash('Thanks for helping in training our Artificial Intelligence ')
            

        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run()
