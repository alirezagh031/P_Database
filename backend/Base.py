import Flask
import mysql.connector

app = Flask(__name__)

con = mysql.connector.connect(host='localhost', user='root', password='1234',database='test')