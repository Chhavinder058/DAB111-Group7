from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path(r"C:\Users\chhav\OneDrive - St. Clair College\DAB111 - python\Flask")
db_name = "customer_shopping.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    shopping = cursor.execute("SELECT * FROM consumer_shopping").fetchall()
    con.close()

    return render_template("data_table.html", shopping = shopping )

if __name__=="__main__":
    app.run(debug=True)
