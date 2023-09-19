from flask import Flask, render_template
from flask import request
from markupsafe import escape
import datetime
# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application

app = Flask(__name__)

'''
    """ < form action="" method="get" >
                < label for ="id" > Username: < / label >
                < input type="text" name="id" id = "id" > < br >
                <label for="password"> Password:</label>
                <input type="password" name="password", id ="password"><br><br>
                <input type="submit" value="Convert">
            </form>"""                
                
                
                
                '''
# ...
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/products/')
def products():
    products = ['This is the first product.',
                'This is the second product.',
                'This is the third product.',
                'This is the fourth product.'
                ]

    return render_template('products.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)

