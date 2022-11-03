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

<<<<<<< HEAD

=======
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
# -----------------------------------------------------

def findall():
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

<<<<<<< HEAD
        sql = 'select a.category_no, b.book_name, b.price, a.category_name from category a , book b where a.category_no = b.book_no'
=======
        sql = 'select a.category_no, b.book_name, b.price, a.category_name from category a , book b where a.category_no =b.category_no'
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')
<<<<<<< HEAD


=======
        
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
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
<<<<<<< HEAD
        print(f'에러: {e}')
=======
        print(f'에러: {e}')
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
