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

        sql = 'select cart_no, quantity from cart order by cart_no asc'
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

        sql = 'insert into cartegory values(null, %s)'
        count = cursor.execute(sql, (quantity, ))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'에러: {e}')
