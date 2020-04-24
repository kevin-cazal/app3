from flask import Flask, render_template
import pymysql
from sys import exit
import config
from time import sleep

app = Flask(__name__)

try:
    db = pymysql.connect(host=config.db_host, user=config.db_user, password=config.db_passwd, database=config.db_name, port=config.db_port)
except pymysql.Error as e:
    print(e)
    exit(84)

@app.route("/")
def list_articles():
    try:
        cursor = db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT title, content FROM Articles")
        res = cursor.fetchall()
        return(render_template("index.j2", parent_dict=res))
    except pymysql.Error as e:
        print("Error during request")
        return "Error"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
