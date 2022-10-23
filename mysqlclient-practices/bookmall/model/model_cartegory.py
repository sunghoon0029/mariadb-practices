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

def findall():
    try:
        db = conn()

        cursor = db.cursor(DictCursor)

        sql = 'select cartegory_no, cartegory_name from cartegory order by cartegory_no asc'
        cursor.execute(sql)

        results = cursor.fetchall()

        cursor.close()
        db.close()

        return results

    except OperationalError as e:
        print(f'에러: {e}')
        
# -----------------------------------------------------
def run_list():
    results = findall()
    
    print('<카테고리 리스트>')
    
    for index, result in enumerate(results):
        
        print(f'{index + 1} - {result["category"]}')

# -----------------------------------------------------

def insert(cartegoryname):
    try:
        db = conn()

        cursor = db.cursor()

        sql = 'insert into cartegory values(null, %s)'
        count = cursor.execute(sql, (cartegoryname, ))

        db.commit()

        cursor.close()
        db.close()

        return count == 1

    except OperationalError as e:
        print(f'에러: {e}')
        
# -----------------------------------------------------

def run_add():
    category = input('category : ')

    insert(category)

    run_list()
