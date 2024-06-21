from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template for the user input form
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Multiply by 10</title>
</head>
<body>
    <h2>Enter a Number to Multiply by 10</h2>
    <form method="post">
        <input type="number" name="number" required>
        <button type="submit">Multiply</button>
    </form>
    {% if result %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def multiply():
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            result = number * 10
            return render_template_string(HTML, result=result)
        except ValueError:
            return render_template_string(HTML, result="Invalid input, please enter a valid number.")
    else:
        # Just render the form when the method is GET
        return render_template_string(HTML, result=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)