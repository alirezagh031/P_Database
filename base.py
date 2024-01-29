import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)



@app.route("/rent")
def rent():
    return render_template('rent.html')


@app.route("/mortgage")
def mortgage():
    return render_template('mortgage.html')


@app.route("/login")
def ad():
    return render_template('login.html')


@app.route("/index")
def index():
    return render_template('index.html')



@app.route("/buy-home")
def buy():
    return render_template('buy-home.html')


@app.route("/agency")
def agency():
    return render_template('agency.html')


@app.route("/")
def login_page():
    return render_template('login.html')





app.run(host='0.0.0.0', debug=True)
# -----------------------------------HomeAdvertise-------------------------------------------------------

# cur.execute('''create table if not exists Home_ad(id_advertising int(7) primary key,
#     price float(12,5) not null default 0,
#     meterage int(10) not null,
#     house_type varchar(15) not null ,
#     room_number int(2) not null default 0,
#     house_age int(2) not null,
#     provience varchar(15) not null,
#     city varchar(15) not null);
#     ''')
#
# cur.execute('''create table if not exists Home_fac(id int,
#             facility_one varchar(15) default null,
#             facility_two varchar(15) default null,
#             facility_three varchar(15) default null,
#             facility_four varchar(15) default null,
#             facility_five varchar(15) default null,
#             facility_six varchar(15) default null,
#             facility_seven varchar(15) default null,
#             facility_eight varchar(15) default null,
#             facility_nine varchar(15) default null,
#             facility_ten varchar(15) default null,
#             facility_eleven varchar(15) default null,
#             facility_twelve varchar(15) default null,
#             foreign key(id) references Home_ad(id_advertising));
#             ''')

# -------------------------------customer-------------------------------------------------------------

# cur.execute('''create table if not exists customer(id_customer int(10) primary key auto_increment ,
#                 name varchar(10) not null,
#                 family_name varchar(10) not null,
#                 gender varchar(6) not null,
#                 phone_number int not null ,
#                 birth_date date not null,
#                 address varchar(40) not null,
#                 email varchar(15) not null,
#                 password varchar(15) not null,
#                 check(LENGTH( password )between 8 and 15)
#                 );''')
# ------------------------------agency---------------------------------------------------------------
# cur.execute('''create table if not exists agency(id_agency int(10) primary key auto_increment,
#             name varchar(10) not null,
#             address varchar(40) not null,
#             province varchar(20) not null,
#             manager_id int,
#             phone_number int (14) not null,
#             foreign key(manager_id) references manager(id_manager));
#             ''')
#
#
# cur.execute('''create table if not exists manager(id_manager int(10) primary key,
#                 name varchar(10) not null,
#                 family_name varchar(10) not null,
#                 phone_number int(11) not null,
#                 address varchar(40) not null,
#                 password varchar(15) not null,
#                 check(length( password )between 8 and 15)
#                 );''')
