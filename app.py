from flask import Flask, render_template, flash
from flask import url_for
from flask import request
import pandas as pd
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    name = "na"
    mobile = request.form.get("phone")
    if request.method == "POST":
        df = pd.read_csv("guest_list.csv")
        name = df.loc[df["Phone"]==int(mobile),"Name"]
        name_vF = name.to_string(index=False)
        if name_vF != "Series([], )":
            table = df.loc[df["Phone"]==int(mobile),"Table"]
            table_vF = table.to_string(index=False)
            message = "Name: "+name_vF+"<br /> Table: "+table_vF
            return message
        else:
            errormsg = "Your mobile number is not in our database. <br> <br> Please go back to the previous page and try again. <br> <br> If it still does not work, please feel free to reach out to our reception or any of the groomsmen and bridesmaid. <br> <br> Thank you for your understanding."
            return errormsg
    else:
        image = [i for i in os.listdir('static/images') if i.endswith('.jpg')][0]
        return render_template("home.html", user_image = image)

# @app.route("/search", methods=["GET","POST"])
# def result():
#     mobile = request.form.get("phone")
#     # record = pd.read_csv("guest_list")
#     # name = (record["Phone"]==mobile)
#     return "Table number:"+mobile
