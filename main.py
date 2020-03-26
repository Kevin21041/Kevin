# '''List'''
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# print(mathScores[2])
# print(mathScores[1:6])
# print(mathScores[-1])
# print(mathScores[5:])
# print(len(mathScores))
# print(sum(mathScores))
# print(max(mathScores))
# print(min(mathScores))
# print(sum(mathScores) / len(mathScores))
# mathScores2 = []
# print(mathScores2)
# mathScores2.append(60)
# print(mathScores2)
# mathScores2.append(70)
# print(mathScores2)
# mathScores2.append(50)
# print(mathScores2)
# mathScores2.append(40)
# print(mathScores2)
# mathScores2.insert(3, 30)
# print(mathScores2)
#
# mathScores2[1] = 55
# print(mathScores2)
# mathScores2.pop(1)
# print(mathScores2)
# print(33 in mathScores2)
# print(50 in mathScores2)
# print(50 not in mathScores2)
# mathScores2.append(70)
# print(mathScores2)
# mathScores2.append(40)
# print(mathScores2)
# mathScores2.append(70)
# print(mathScores2)
# print(mathScores2.count(70))
# print(mathScores2.index(70))
# print(sorted(mathScores2))
# print(sorted(mathScores2, reverse=True))
# print(mathScores + mathScores2)
#
# ls = [[1, 2, 3], [4, 5, 6]]
# print(ls[0])
# print(ls[0][2])
# '''練習1'''
# grades = [[5, 14, 7], [23, 36, 28], [88, 80, 92]]
# '''印出數學成績'''
# print(grades[2])
# '''印出各科平均'''
# avg1 = (sum(grades[0]) / len(grades[0]))
# print(avg1)
# avg2 = (sum(grades[1]) / len(grades[1]))
# print(avg2)
# avg3 = (sum(grades[2]) / len(grades[2]))
# print(avg3)
# '''加入自然成績'''
# grades.append([94, 90, 96])
# print(grades)
# '''將國文小考2的成績改為20'''
# grades[0][1] = 20
# print(grades)
#
#
# '''Tuple'''
# tuple1 = (1, 2, 3, 4, 5, 3, 1)
# print(tuple1[3])
# print(tuple1.index(4))
# print(tuple1.count(3))
#
# tuple2 = (1, 2, 3, 4, 5)
# tuple3 = (4, 3, 4, 1, 6)
# print(tuple2 + tuple3)
# print(sorted(tuple3))
# print(sorted(tuple3, reverse=True))
# print(1 in tuple1)
#
# tuple4 = (88, 12)
# x, y = tuple4
# print(x)
# print(y)
# '''練習2-Tuple'''
# gradesTuple = ([5, 14, 7], [23, 36, 28], [88, 80, 92])
# '''印出數學成績'''
# print(gradesTuple[2])
# '''印出各科平均'''
# avg4 = (sum(gradesTuple[0]) / len(gradesTuple[0]))
# print(avg4)
# avg5 = (sum(gradesTuple[1]) / len(gradesTuple[1]))
# print(avg5)
# avg6 = (sum(gradesTuple[2]) / len(gradesTuple[2]))
# print(avg6)
#
#
# '''Dict'''
# family = {"dad": "Homer",
#           "mom": "Marge",
#           "son": "Bart",
#           "daughter": "Lisa"
#           }
# print(family["dad"])
# print(family.get("dog"))
#
# print("dog" in family)
# print(family.keys())
# print(family.values())
# print(family.items())
# family = {}
# print(family)
# family["cousin"] = "Max"
# print(family)
# family.update({
#     "uncle": "Martin",
#     "aunt": "May",
# })
# print(family)
# del family["uncle"]
# print(family)
# print(family.pop("cousin"))
#
# '''練習3-Dictionary'''
# gradesDict={"chinese":[5,14,7],
#             "english":[23,36,28],
#             "math":[88,80,92],
# }
# print(gradesDict.get("math"))
# print(sum(gradesDict.get("chinese"))/len(gradesDict.get("chinese")))
# print(sum(gradesDict.get("english"))/len(gradesDict.get("english")))
# print(sum(gradesDict.get("math"))/len(gradesDict.get("math")))
# gradesDict["science"]=[94,90,96]
# print(gradesDict.items())
#
# '''Set'''
# fruits = {
#     "apple",
#     "banana",
#     "guava",
#     "guava"
# }
# fruits1 = {
#     "strawberry",
#     "papaya",
#     "banana"
# }
# '''聯集'''
# print(fruits|fruits1)
# '''交集'''
# print(fruits&fruits1)
# '''差集'''
# print(fruits-fruits1)
#
#
# print(sorted(fruits))
# """練習4"""
# allStudents = {
#      "John",
#      "Eva",
#      "Jill",
#      "Eric",
#      "Andy",
#      "Albert",
#      "Polina",
#      "Kristin",
#      "Angela"
#  }
# guitarClub = {
#      "John",
#      "Eva",
#      "Jill",
#      "Eric",
#      "Andy"
# }
# danceClub = {
#      "Andy",
#      "Eric",
#      "Albert",
#      "Polina",
#      "Kristin",
# }
# print(danceClub & guitarClub)
# print(guitarClub - danceClub)
# print(allStudents - guitarClub - danceClub)
#
#
#
# """ch3"""
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# x=4**0.5
# print(x)
# import math
# print(math.sqrt(5.8))
# '''練習'''
# '''圓面積math.pi待解決'''
# # r=3
# # pi=3.14
# # print((r**2*pi)
# # '''計算學生的平均成績'''
# # Score =[10,30,40,90,100,61]
# # print(round((sum(Score)/len(Score))))
#
# '''elif=else if'''
# score = 53
# if score >= 60:
#     print("及格了")
# elif 55 <= score < 60:
#     print("教授拜託調個分")
# elif 50 <= score <55:
#     print("可惡差一點點")
# else:
#     print("被當了")
# '''等於下面'''
# SCORE = 56
# if SCORE >= 60:
#     print("及格了")
# elif 55 <= SCORE and SCORE < 60:
#     print("教授拜託調個分")
# elif 50 <= SCORE and SCORE< 55:
#     print("可惡差一點點")
# else:
#     print("被當了")
#
# score = 86
# if score >= 60:
#     print("及格了")
#     if score >=90:
#         print("你最棒")
#     else:
#         print("還不錯棒")
# elif 55 <= score < 60:
#     print("教授拜託調個分")
# elif 50 <= score <55:
#     print("可惡差一點點")
# else:
#     print("被當了")
#
# print("Hello","world","!")
# print("Hello \nworld\n !")
# print("1是左腳",end="2是右腳")
# print("121")
#
# w=42
# print(f"Value of w is {w}")
#
# firstItem = f"first item in mathScores is {mathScores[0]}"
# print(firstItem)
# firstItem = f"first item in mathScores is {len(mathScores)}"
# print(firstItem)
#
# '''迴圈'''
# for i in range(0,10,2):
#     print(i)
#
# for i in range(len(mathScores)):
#     print(i,mathScores[i])
# '''等於下面'''
# for i in mathScores:
#     print(i)
#
# family = {
#     "dad": "Homer",
#     "mom": "Marge",
#     "son": "Bart",
#     "daughter": "Lisa"
# }
# '''.items出來是tuple格式,不用items出來是key的形式'''
# for member in family.items():
#     print(member)
#
# for key,value in family.items():
#     print(f"my {key} is {value}")
#
# '''練習2'''
# for newScore in mathScores:
#     print("newScore",math.sqrt(newScore)*10)
#
# '''串列綜合表達式0-9'''
# [print(i) for i in range(10)]
#
# [print(math.sqrt(newScore)*10) for newScore in mathScores]
#
# count=0
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("loop end")
#
# mathScores = [60, 70, 10, 20, 81, 63, 4]
# for x in mathScores:
#      if x>80:
#          break
#      print(x)
#
# for x in mathScores:
#     if x>80:
#         continue
#     print(x)
#
# import random
# i = random.randint(1,50)
# print(i)
# x = eval(input("How many rows:"))
# print(type(x))

# 練習1
# for i in range(1,10):
#     for j in range(1,10):
#          print(f"{i}*{j}","=",i*j)
#
# 練習2
# count=0
# while count < 50:
#     print("你好")
#     count +=1
# else:
#     print("我說完了拉")
# 練習3
# num = eval(input("請輸入數字:"))
# # for x in range(1,num+1):
# #     if x%2 ==1:
# #        print(x)
# 練習4
# import random
# ls = []
# rows = eval(input("請輸入列數:"))
# columns = eval(input("請輸入行數:"))
# for i in range(rows):
#     ls.append([])
#     for j in range(columns):
#         num = random.randint(1,100)
#         ls[i].append(num)
# for x in range(rows):
#     for y in range(columns):
#         print(f"{ls[x][y]}", end=" ")
#     print()
# # 練習5
# total = 0
# for i in range(rows):
#     for j in range(columns):
#         total += ls[i][j]
# print("total is",total)
# # 練習6
# row_totals= []
# for i in range(rows):
#     row_total = 0
#     for j in range(columns):
#         row_total += ls[i][j]
#     row_totals.append(row_total)
#     print("row_totals are",row_totals)
# # 練習7
# column_totals = []
# for column in ls:
#     column_totals.append(sum(column))
#     print("column_totals are",column_totals)
"CH4 販賣機"
import vending_machine.vending_service as machine
flag = True

while flag:
    print("\n====================")
    select = eval(input("1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:"))

    if select == 1:  # 儲值
        machine.deposit()
    #若使用者輸入數字小於零，需要重新輸入
    elif select == 2:  # 購買
        machine.buy()

    elif select == 3:  # 查詢餘額
        print(f"目前餘額為{machine.balance}元")
        if machine.balance == 0:
            print("====餘額不足====")
        machine.deposit()
    elif select == 4:  # 離開
        print("謝謝光臨~~Bye Bye")
        flag = False
        break
    else:
         print("====請輸入1-4之間====")
         continue

x=1
# weight = 100
# weight1 = 80
# def add_weight(w1,w2=1):
#     result = w1+w2
#     result1 = w1/w2
#     return result,result1
# x,y= add_weight(weight,weight1)
# print(x,y)
#
# y1,y2 = add_weight(w2=weight,w1=weight1)
# print(y1,y2)




