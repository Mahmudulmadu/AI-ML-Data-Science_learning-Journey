from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='assests', static_url_path='/assests')

@app.route('/')
def hello_world():
    # name = request.args.get('name', default='Anonymous')
    # subject = request.args.get('subject', default='Anything')      
    # return render_template('index.html', name=name, subject=subject)

    data = {
        "Message": "Hello, World!",
    }
    return jsonify(data)    

@app.route('/login' , methods=['GET', 'POST'])
def login():
   if request.method == "POST":
       name = request.form["username"]
       password = request.form['password']

       friends = ["Alice", "Bob", "Charlie"]
       header = "<header><h1>Welcome to the Flask App</h1></header>"
       return render_template('welcome.html', name=name, friends=friends, header=header)
   else:
         return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)