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
        sql = 'select b.book_name , a.quantity , b.price from cart a , book b, member c where a.book_no = b.book_no and a.member_no = c.member_no'
=======
        sql = 'select b.book_name , a.quantity , b.price from cart a , book b where a.cart_no = b.book_no
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')

# -----------------------------------------------------

def insert(quantity):
    try:
        db = conn()

        cursor = db.cursor()

<<<<<<< HEAD
        sql = 'insert into cart values(null, %s)'
=======
        sql = 'insert into cartegory values(null, %s)'
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
        count = cursor.execute(sql, (quantity, ))

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
