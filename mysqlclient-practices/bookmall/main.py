from bookmall.model import model_cartegory, model_book, model_cart, model_member, model_orders, model_orders_book

# ------------------------------------------------------------------

print('------------회원 리스트------------')

<<<<<<< HEAD
# model_member.insert(member_name='조성훈', tel='010-1234-1234', email='sunghoon@gmail.com', password='bookmall')
# model_member.insert(member_name='둘리', tel='010-5678-5678', email='dooly@gmail.com', password='bookmall')
=======
model_member.insert(member_name='조성훈', tel='010-1234-1234', email='sunghoon@gmail.com', password='bookmall')
model_member.insert(member_name='둘리', tel='010-5678-5678', email='dooly@gmail.com', password='bookmall')
>>>>>>> branch 'main' of https://github.com/sunghoon0029/mariadb-practices.git
#
results = model_member.findall()

for index, result in enumerate(results):
    print(f'{index + 1}:{result["member_name"]}, {result["tel"]}, {result["email"]}, {result["password"]}')

# ------------------------------------------------------------------

print('------------카테고리 리스트------------')
#
<<<<<<< HEAD
# model_cartegory.insert('소설')
# model_cartegory.insert('역사')
# model_cartegory.insert('IT')
=======
model_cartegory.insert('소설')
model_cartegory.insert('역사')
model_cartegory.insert('IT')
>>>>>>> branch 'main' of https://github.com/sunghoon0029/mariadb-practices.git
#
results = model_cartegory.findall()

for index, result in enumerate(results):
    print(f'{index + 1}:{result["cartegory_name"]}')

# ------------------------------------------------------------------

print('------------상품 리스트------------')
#
<<<<<<< HEAD
# model_book.insert('어린왕자', '10000')
# model_book.insert('삼국지', '15000')
# model_book.insert('이것이 자바다', '30000')
=======
model_book.insert('어린왕자', '10000')
model_book.insert('삼국지', '15000')
model_book.insert('이것이 자바다', '30000')
>>>>>>> branch 'main' of https://github.com/sunghoon0029/mariadb-practices.git
#
results = model_book.findall()

for index, result in enumerate(results):
    print(f'{index + 1}:{result["book_name"]}, {result["price"]}')

# ------------------------------------------------------------------

print('------------카트 리스트------------')

<<<<<<< HEAD
# model_cart.insert(2, 3, 2)
# model_cart.insert(1, 2, 1)
#
results = model_cart.findall()
#
for index, result in enumerate(results):
    print(f'{index + 1}:제목:{result["book_name"]}, 수량:{result["quantity"]}, 가격:{result["price"]}')

# ------------------------------------------------------------------X

print('------------주문 리스트------------')

# model_orders.insert('15000', '비트교육센터', 1)
=======
model_cart.insert(2, 3, 2)
model_cart.insert(1, 2, 1)
#
results = model_cart.findall()
#
for index, result in enumerate(results):
    print(f'{index + 1}:제목:{result["book_name"]}, 수량:{result["quantity"]}, 가격:{result["price"]}')

# ------------------------------------------------------------------X

print('------------주문 리스트------------')

model_orders.insert('15000', '비트교육센터', 1)
>>>>>>> branch 'main' of https://github.com/sunghoon0029/mariadb-practices.git

results = model_orders.findall()

for index, result in enumerate(results):
    print(
        f'{index + 1}:주문번호:{result["orders_no"]}, 고객명:{result["member_name"]}, 이메일:{result["email"]}, 주소:{result["address"]}, 주문금액:{result["price"]}')

# ------------------------------------------------------------------X

print('------------주문도서 리스트------------')

<<<<<<< HEAD
# model_orders_book.insert(1, 1)
# model_orders_book.insert(2, 3)

# results = model_orders_book.findall()
#
# for index, result in enumerate(results):
#     print(f'{index + 1}:도서번호:{result["book_no"]}, 제목:{result["book_name"]}, 수량:{result["quantity"]}')
=======
model_orders_book.insert(1, 1)
model_orders_book.insert(2, 3)

results = model_orders_book.findall()

for index, result in enumerate(results):
    print(f'{index + 1}:도서번호:{result["book_no"]}, 제목:{result["book_name"]}, 수량:{result["quantity"]}')
>>>>>>> branch 'main' of https://github.com/sunghoon0029/mariadb-practices.git
