from vending_machine.data import Drink

drinks = [

    Drink('可樂',20),
    Drink('雪碧',20),
    Drink('茶裏王',25),
    Drink('原翠',25),
    Drink('純粹喝',30),
    Drink('水',20),

]
balance = 0


def deposit():
    global balance  # 在deposit裡是區域變數，balance為全域變數，所以要宣告global
    value = eval(input("儲值金額:"))
    while value < 1:
        print("====儲值金額需大於零====")
        value = eval(input("儲值金額:"))
    balance += value
    print(f"儲值後餘額為{balance}元")


def buy():
    global balance
    global drinks
    # 印出品項
    print("\n請選擇商品")
    for i in range(len(drinks)):
        print(f'({i + 1})\t{drinks[i].get_name()}  \t  {drinks[i].get_price()}元')
    choose = eval(input('請選擇:'))

    while choose < 1 or choose > 6:
        print('====請輸入1-6之間====')
        choose = eval(input('請選擇:'))

    buy_drink = drinks[choose - 1]
    while balance < buy_drink.get_price():
        print('====餘額不足，需要儲值嗎?====')
        want_deposit = input('y/n?')
        if want_deposit == 'y':
            deposit()
        elif want_deposit == 'n':
            break
        else:
            print('====請重新輸入====')
    if balance < buy_drink.get_price():
        print("====，需要儲值嗎?====")
        deposit()
    else:
        print(f'已購買{buy_drink.get_name()} {buy_drink.get_price()}元')
        balance -= buy_drink.get_price()
        print(f'購買後餘額為{balance}元')
"""
數字相加
:param x:數字1
:param y:數字2
:return:相加結果
"""
