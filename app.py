from flask import Flask,render_template,request


app= Flask(__name__)
@app.route("/")
def index():
    return render_template("hellohello1.html")
@app.route("/ff", methods=["POST"])
def form():
    num1= request.form["num1"]
    num2= request.form["num2"]
    total=int(num1)+int(num2)
    return render_template("hellohello1.html",total=total)
if __name__=="__main__":
    app.run()