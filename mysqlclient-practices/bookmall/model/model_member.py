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
        sql = 'select member_no, member_name, tel, email, password from member'
=======
        sql = 'select member_name, tel, email, password from member'
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
def insert(member_name, tel, email, password):
=======
def insert(membername, tel, email, password):
>>>>>>> 25f91cee2a90434ed9f96cf45d808c861d3c1be6
    try:
        db = conn()

        cursor = db.cursor()

<<<<<<< HEAD
        sql = 'insert into member values(null, %s, %s, %s, %s)'
        count = cursor.execute(sql, (member_name, tel, email, password))
=======
        sql = 'insert into cartegory values(null, %s, %s, %s, %s)'
        count = cursor.execute(sql, (membername, tel, email, password))
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
