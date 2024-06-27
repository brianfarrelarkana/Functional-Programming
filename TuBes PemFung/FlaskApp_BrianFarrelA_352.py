from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def connection():
    conn = None
    try:
        conn = pymysql.connect(
            host = 'sql12.freesqldatabase.com',
            database = 'sql12677767',
            user = 'sql12677767',
            password = 'Af9MmddLEm',
            cursorclass = pymysql.cursors.DictCursor,
        )
    except pymysql.Error as e:
        print(e)
    return conn

@app.route("/ImplantOrgans", methods=["GET", "POST", "PUT", "DELETE"])
def implantOrgans():
    conn = connection()
    cursor = conn.cursor()
    
    if request.method == "GET":
        cursor.execute("SELECT * FROM ImplantOrgans")
        ImplantOrgans = [
            dict(
                serialNum = row["serialNum"],
                implantName = row["implantName"],
                placement = row["placement"],
                effect = row["effect"],
                price = row["price"],
            )
            for row in cursor.fetchall()
        ]
        if ImplantOrgans is not None:
            return jsonify(ImplantOrgans)
        
    if request.method == "POST":
        serialNum = request.form["serialNum"]
        add_implantName = request.form["implantName"]
        add_placement = request.form["placement"]
        add_effect = request.form["effect"]
        add_price = request.form["price"]

        add_data = """INSERT INTO ImplantOrgans (serialNum, implantName, placement, effect, price) VALUES (%s, %s, %s, %s, %s)"""
        
        cursor = cursor.execute(add_data,(serialNum, add_implantName, add_placement, add_effect, add_price))
        conn.commit()
        
        return "Data Add Successfull"
    
    if request.method == "PUT":
        serialNum = request.form["serialNum"]
        update_implantName = request.form["implantName"]
        update_placement = request.form["placement"]
        update_effect = request.form["effect"]
        update_price = request.form["price"]

        update_data = """UPDATE ImplantOrgans SET implantName=%s, placement=%s, effect=%s, price=%s WHERE serialNum=%s"""
        
        cursor = cursor.execute(update_data,(serialNum, update_implantName, update_placement, update_effect, update_price))
        conn.commit()
        
        return "Data Update Successfull"
    
    if request.method == "DELETE":
        serialNum = request.form["serialNum"]
        
        delete_data = """DELETE FROM ImplantOrgans WHERE serialNum=%s"""

        cursor = cursor.execute(delete_data,(serialNum))
        conn.commit()

        return "Data Delete Successfull"
    
if __name__ == "__main__":
    app.run()