from bookmall.model import model_cartegory, model_book, model_cart, model_member, model_orders


def run_list1():
    results = model_member.findall()

    for index, result in enumerate(results):
        print(f'{index + 1}:{result["cartegory_name"]}')

# ------------------------------------------------------------------
def run_add1():
    cartegoryname = input('cartegory_name: ')

    model_member.insert(cartegoryname)

    run_list1()
# ------------------------------------------------------------------

# run_list1()
# run_add1()



def run_list2():
    results = model_book.findall()

    for index, result in enumerate(results):
        print(f'{index + 1}:{result["book_name"]}:{result["price"]}')

# ------------------------------------------------------------------
# def run_add2():
#     cartegoryname = input('cartegory_name: ')
#
#     model_member.insert(cartegoryname)
#
#     run_list()
# ------------------------------------------------------------------
run_list2()

# from models import model_member

# print("--회원 리스트--")
# model_member.insert()
# model_member.insert()
# results = model_member.findall()
# for result in results:
#     print(result)
#
# print("--카테고리 리스트--")
#
#
# print("--상품리스트--")
#
#
# print("--카트 리스트--")
#
#
# print("--주문 리스트--")
#
#
# print("--주문 도서 리스트--")



