from flask import Flask, render_template, request

app = Flask(__name__)

messages = []  # temporary storage

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    messages.append({
        "name": name,
        "email": email,
        "message": message
    })

    print(messages)  # shows in terminal

    return "Message received!"

if __name__ == '__main__':
    app.run(debug=True)