import random
import datetime

st = datetime.datetime.now()
ed = datetime.datetime.now()
print((ed-st).seconds)
lst = {"サザエの旦那の名前は？":["マスオ","ますお"],
      "カツオの妹の名前は？":["ワカメ","わかめ"],
       "タラオはカツオから見てどんな関係？":["甥","甥っ子"]}

count = 0
while count<3:
    count+=1
    randomlst = random.choice(list(lst.keys()))
    print("問題:")
    print(randomlst)
    inputlst = input("答えろ:")
    if inputlst== lst[randomlst]:
        print("正解!!!")
        if count==3:
            break
        else:
            continue
    else:
        print("違います")
        if count ==3:
            break
        else:
            continue