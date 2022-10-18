from MySQLdb import connect, OperationalError

try:
    # 1. 연결
    db = connect(
        user='webdb',
        password='webdb',
        host='127.0.0.1',
        port=3306,
        db='webdb',
        charset='utf8')

    # 2. cursor 생성
    cursor = db.cursor()

    # 3. sql(insert문) 실행
    sql = 'insert into pet values("딸랑이", "조성훈", "dog", "m", "2020-10-18", null)'
    count = cursor.execute(sql)

    # 4. commit
    db.commit()

    # 5. 자원 정리
    cursor.close()
    db.close()

    # 결과 확인
    print(f'실행결과: {count}')

    # 에러 처리
except OperationalError as e:
    print(f'에러: {e}')