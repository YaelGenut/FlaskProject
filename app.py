from flask import Flask, redirect, url_for

app = Flask(__name__)

# -------------- routes ---------------

@app.route('/')

# ------------- pages functions ------------

# home page
@app.route('/home_page')
def home_page_func():
        return 'Welcome to the Home Page!'

# products page
@app.route('/products')
def products_func():
    return 'Welcome to products page'


# ------------- redirect functions ------------

# redirect about page
@app.route('/about')
def about_func():
    return redirect('/products')

# redirect about page
@app.route('/catalogs')
def catalog_func():
    return redirect(url_for('products_func'))

if __name__ == '__main__':
    app.run()
