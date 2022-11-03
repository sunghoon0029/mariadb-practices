from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def conn():
    db = connect(
        user='bookmall',
        password='bookmall',
        host='127.0.0.1',
        port=3306,
        db='bookmall',
        charset='utf8')
    return db

# -----------------------------------------------------

def findall():
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

<<<<<<< HEAD
        sql = 'select b.member_name, b.email, a.address, a.price from orders a , member b where a.member_no = b.member_no'
=======
        sql = 'select a.orders_no, b.member_name, b.email, a.price, a.address from orders a , member b where a.member_no = b.member_no'
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')

# -----------------------------------------------------

<<<<<<< HEAD
def insert(price, address):
=======
def insert(price, address, memberno):
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
    try:
        db = conn()

        cursor = db.cursor()

<<<<<<< HEAD
        sql = 'insert into orders values(null, %s, %s)'
        count = cursor.execute(sql, (price, address))
=======
        sql = 'insert into cartegory values(null, %s, %s, %s)'
        count = cursor.execute(sql, (price, address, memberno))
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
<<<<<<< HEAD
        print(f'에러: {e}')
=======
        print(f'에러: {e}')
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
