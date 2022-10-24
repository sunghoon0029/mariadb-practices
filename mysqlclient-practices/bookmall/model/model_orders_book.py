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

        sql = 'select a.book_no, a.book_name, b.price from book a , orders_book b where a.book_no = b.book_no'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')

# -----------------------------------------------------

def insert(book_no, price):
    try:
        db = conn()

        cursor = db.cursor()

        sql = 'insert into orders values(null, %s, %s)'
        count = cursor.execute(sql, (book_no, price))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'에러: {e}')