from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=['POST', "GET"])
def index():
    exp = 0
    if request.method =='POST':
        task_content = request.form['content']
        exp = eval(task_content)
        # exp = task_content
    return render_template('index.html', exp=exp)
