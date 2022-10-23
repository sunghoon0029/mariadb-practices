from bookmall.model import model_cartegory, model_book, model_cart, model_member, model_orders

print('회원 리스트')

model_member.insert(membername='조성훈', tel='010-1234-1234', email='sunghoon@gmail.com', password='bookmall' )
model_member.insert(membername='둘리', tel='010-5678-5678', email='dooly@gmail.com', password='bookmall')

results= model_member.findall()

for index, result in enumerate(results):
    print(f'{index+1}:{result["membername"]}, {result["tel"]}, {result["email"]}, {result["password"]}')
    
# ------------------------------------------------------------------

print('카테고리 리스트')

model_category.insert('소설')
model_category.insert('역사')
model_category.insert('IT')

results= model_category.findall()

for index, result in enumerate(results):
    print(f'{index+1}:{result["cartegoryname"]}')

# ------------------------------------------------------------------
    
print('상품 리스트')

model_book.insert('어린왕자', '10000', '2')
model_book.insert('삼국지', '15000', '1')
model_book.insert('이것이 자바다', '30000', '3')

results= model_book.findall()

for index, result in enumerate(results):
    print(f'{index+1}:제목:{result["bookname"]}, 가격:{result["price"]}, {result["categoryno"]}')

# ------------------------------------------------------------------
    
print('카트 리스트')

model_cart.insert(2,3,2)
model_cart.insert(1,2,1)

results= model_cart.findall()

for index, result in enumerate(results):
    print(f'{index+1}:제목:{result["bookname"]}, 수량:{result["quantity"]}, 가격:{result["price"]}')

# ------------------------------------------------------------------    

print('주문 리스트')

model_order.insert('000000001', '15000', '삼국지', 2)

results=model_order.findall()

for index, result in enumerate(results):
    print(f'{index+1}:주문번호:{result["ordersno"]}, {result["bookname"]}, {result["email"]}, 결제금액:{result["price"]}, {result["address"]}')

# ------------------------------------------------------------------    
    
print('주문도서 리스트')

model_order.insert_order_book(1,1,1)
model_order.insert_order_book(2,1,2)

results= model_order.findall_order_book()

for index, result in enumerate(results):
    print(f'{index+1}:도서번호:{result["bookno"]}, {result["bookname"]}, 수량:{result["quantity"]}')
