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

        sql = 'select a.category_no, b.book_name, b.price, a.category_name from category a , book b where a.category_no = b.book_no'

        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')

# -----------------------------------------------------

def insert(book_name, price, cartegory_no):
    try:
        db = conn()

        cursor = db.cursor()

        sql = 'insert into book values(null, %s, %s, %s)'
        count = cursor.execute(sql, (book_name, price, cartegory_no))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'에러: {e}')
