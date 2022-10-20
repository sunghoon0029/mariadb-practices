from MySQLdb import connect, OperationalError

try:
    db = connect(
        user='bookmall',
        password='bookmall',
        host='127.0.0.1',
        port=3306,
        db='bookmall',
        charset='utf8')

    print('연결 성공')
except OperationalError as e:
    print(f'에러: {e}')