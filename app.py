import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from flask import Flask, render_template, request,redirect,url_for
from sklearn.model_selection import train_test_split
app = Flask(__name__)
data=load_breast_cancer()
data=load_breast_cancer()
df=pd.DataFrame(data['data'][:,:5],columns=data['feature_names'][:5])
X=df
y=data['target']
model=LogisticRegression()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

model.fit(X_train,y_train)





@app.route("/",methods=["GET", "POST"])
def hello_world():
    if request.method=="POST":
        mean_radius=request.form.get("d1") 
        mean_texture=request.form.get("d2") 
        mean_perimeter =request.form.get("d3") 
        mean_area  =request.form.get("d4") 
        mean_smoothness=request.form.get("d5")
        a=[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness]
        # b = np.array(a, dtype=float) #  convert using numpy
        

        c = [float(i) for i in a] 
        print (c)
        pred=model.predict([c])
        print(pred[0]) 
        print(type(pred.item()))
        if pred.item()==0:
            return redirect(url_for("result1"))
        elif pred.item()==1:

            return redirect(url_for("result2"))

        else:
            render_template("result.html",result="invalid input")




    return render_template("index.html")
@app.route("/result1")
def result1():
    return render_template("result.html",result="Contact a doctor imediatly")

@app.route("/result2")
def result2():
    return render_template("result.html",result="you are fine")

if __name__ == "__main__":
    app.run(debug=True)
