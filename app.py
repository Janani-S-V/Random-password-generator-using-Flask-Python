from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)
def generate_password(length, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    characters = ''  
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    if not characters:
        return "Error: No character types selected"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_uppercase = 'include_uppercase' in request.form
        include_lowercase = 'include_lowercase' in request.form
        include_digits = 'include_digits' in request.form
        include_special = 'include_special' in request.form
        generated_password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_special)
        return render_template('index.html', password=generated_password)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
