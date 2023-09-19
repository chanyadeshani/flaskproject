from flask import Flask, render_template
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )


'''
    """ < form action="" method="get" >
                < label for ="id" > Username: < / label >
                < input type="text" name="id" id = "id" > < br >
                <label for="password"> Password:</label>
                <input type="password" name="password", id ="password"><br><br>
                <input type="submit" value="Convert">
            </form>"""                
                
                
                
                '''
@app.route("/<int:celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    fahrenheit = float(celsius) * 9 / 5 + 32
    fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
    return str(fahrenheit)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

