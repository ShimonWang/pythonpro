lst = []

for i in range(5):
    goods = input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)

for item in lst:
    print(item)

cart = []
while True:
    flag = False
    num = input('请输入要购买的商品编号：')

    for item in lst:
        if num == item[0:1]:
            flag = True
            cart.append(item)
            print('商品已经成功添加到购物车')
            break
    if not flag and num != 'q':
        print('商品不存在')

    if num == 'q':
        break
print('-'*50)
print('您购物车里已选择的商品为：')
cart.reverse()
for item in cart:
    print(item)