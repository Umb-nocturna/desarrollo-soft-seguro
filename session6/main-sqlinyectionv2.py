import os
import mysql.connector
from datetime import date
from functools import wraps
from flask import Flask, jsonify, request
import json


app = Flask(__name__)

def products_select_safe(category = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    mycursor = mydb.cursor()
    table_name = 'products'
    mycursor.execute("SELECT * FROM %s WHERE category = %%s AND released = 1" % table_name,[category])
    myresult = mycursor.fetchall()
    return myresult

def products_select(category = ""):
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM products WHERE category = "'+category+'" AND released = 1'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def products_select_sp(category = ""):
    """Function return all products from mysql."""
    mydb = mysql.connector.connect(
        host="containers-us-west-101.railway.app",
        user="root",
        password="6G74WClR1fVadVdFKqFX",
        database="railway",
        port=7171
    )
    args = (category,)
    cursor = mydb.cursor()
    cursor.callproc('sp_products_by_category', args)
    for result in cursor.stored_results():
        product = result.fetchall()
    json_products = json.dumps(product)
    return json_products

@app.route('/')
def index():
    return jsonify({"hello": "SQL inyection test"}) 

@app.route('/products', methods=['GET'])
#https://insecure-website.com/products?category=Gifts
def products_get():
    args = request.args
    s_category = args.get("category")
    if(s_category):
       #respuesta = products_select(s_category) 
       respuesta = products_select_safe(s_category)
       
       return jsonify({"msg":"success","products":respuesta})
    else:
        return jsonify({"status":"error","msg":"parametro no permitido"})
        
@app.route('/v2/products', methods=['GET'])
#https://insecure-website.com/products?category=Gifts
def products_v2get():
    args = request.args
    s_category = args.get("category")
    if(s_category):
       respuesta = products_select_sp(s_category) 
       return jsonify({"msg":"success","products":respuesta})
    else:
        return jsonify({"status":"error","msg":"parametro no permitido"})


"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 