import random
lst = {"サザエの旦那の名前は？":"マスオ",
      "カツオの妹の名前は？":"ワカメ",
       "タラオはカツオから見てどんな関係？":"甥"}

count = 0
while count<3:
    count+=1
    randomlst = random.choice(list(lst.keys()))
    print("問題:")
    print(randomlst)
    inputlst = input("答えるんだ:")
    if inputlst== lst[randomlst]:
        print("正解!!!")
        if count==3:
            break
        else:
            continue
    else:
        print("出直してこい")
        if count ==3:
            break
        else:
            continue