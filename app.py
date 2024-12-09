from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    option = request.form.get('option')
    other_option = request.form.get('other_option')
    
    # Use the "Other" input if selected
    selected_option = other_option if option == 'Other' else option

    message = request.form.get('message')
    return render_template(
        'result.html', 
        name=name, 
        email=email, 
        selected_option=selected_option, 
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)