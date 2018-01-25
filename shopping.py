salary = input('please input your salary:')
item_list=[[1,'iphonex-64G','8388'],[2,'iphonex-256G','9688'],[3,'AppleWatch-42MM','3488'],[4,'airpods','1198']]
print(item_list)
choice = input('please input the index:')
item_price=item_list[int(choice)-1][2]
left_salary = int(salary) - int(item_price)
if int(salary)>int(item_price):
    print(item_list[int(choice)-1][1],'已加入购物车')
    if left_salary > 1198:
        print('您的余额为',left_salary)
        print(item_list)
        choice = input('please input the index:')
        print(item_list[int(choice) - 1][1], '已加入购物车')
    else:
        print('您的余额已不足以购买其他商品，您本次购买的商品为',item_list[int(choice)-1][1],'价格为',item_list[int(choice)-1][2])
else:
    print('您的余额不足，请重新选择')
    print(item_list)
    choice = input('please input the index:')
