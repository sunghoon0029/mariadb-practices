from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

<<<<<<< HEAD

=======
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
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
        sql = 'select cartegory_no, cartegory_name from cartegory'
=======
        sql = 'select cartegory_no, cartegory_name from cartegory order by cartegory_no asc'
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')
<<<<<<< HEAD


# -----------------------------------------------------

def insert(cartegory_name):
=======
        
# -----------------------------------------------------

def insert(cartegoryname):
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
    try:
        db = conn()

        cursor = db.cursor()

        sql = 'insert into cartegory values(null, %s)'
<<<<<<< HEAD
        count = cursor.execute(sql, (cartegory_name,))
=======
        count = cursor.execute(sql, (cartegoryname, ))
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
