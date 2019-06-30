
from flask import Flask, flash, jsonify, render_template, request
import webbrowser
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
@app.route('/')
def hello():
    # return "this webpage is working"
    return render_template('index.html')

@app.route('/handle_data', methods=['POST'])
def my_form_post():
    body = request.form['body']
    title= request.form['title']

    return f'Title:{title} and Body: {body}'

@app.route("/getvalue/<title>/<body>")
def data(title, body):
    """Display all data from the collection."""
    # return f'T :{title} and B : {body}'
    return f'T --- {title} and B --- {body}'

# @app.route('/handle_data' ,methods = ['POST', 'GET'])    
# def handle_data():
#     # if request.method == 'POST':
#     #     title = request.form.get('title')
#     #     body = request.form.get('body')
#     #     return title
#     # else:
#     #     return "hello"
#     # return title
#     title = request.form.get('title')
#     body = request.form.get('body')
#     return title
       
    #    from cypher import encode 
#     # encode(title,body)
        
        
        
        # result = request.form
        # return render_template("result.html",result = result)
    #  return render_template('index.html')

# First try, keeps giving an error that I call variable before defined
# @app.route('/handle_data' ,methods = ['POST', 'GET'])    
# def handle_data():
#     if request.method == 'POST':
#         body = request.form['body']
#         # title = request.form['title']
#         return body
        
    
#     # return "this works"
#     # return title
#     # from cypher import encode 
#     # encode(title,body)
    
if __name__ == '__main__':
    app.run(debug=True)
