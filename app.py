

from flask import Flask , render_template , request , redirect , url_for
from forms import MyForm, ContactForm
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your_secret_key'

messages = []

@app.route('/' , methods=['GET'])
def home():
  return render_template('home.html')

@app.route('/form' , methods = ['GET' , 'POST'])
def form():
  form = MyForm()
  if form.validate_on_submit():
    name = form.name.data
    return f"Hello ,{name}!  Form submitted successfully."
  return render_template('form.html' , form = form)

@app.route('/contact' , methods=['GET' ,'POST'])
def contact():
  form = ContactForm()
  if request.method == 'POST' and form.validate_on_submit():
    name = form.name.data
    email = form.email.data
    message = form.message.data

    messages.append((name , email , message))
    return redirect(url_for('messages_page'))
  return render_template('contact.html' , form = form)

@app.route('/messages')
def messages_page():
  return render_template('messages.html' , messages = messages)

if __name__ == '__main__':
  app.run(debug = True)