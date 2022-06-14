import random
import datetime

answer = 5
b = 10
c = 2

#def main():
    #answer=()を下記に修正

def main():
    for xyz in range(answer):
        m = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        t = []
        k = []
        for i in range(c):
            a=random.randint(0,len(m)-1)
            t.append(m.pop(a))
        print("対象文字:")
        print("".join(t))
        for i in range(b):
            b =random.randint(0, len(t)-1)
            k.append(t.pop(b))
        print("表示文字")
        print(".join"(t))

        x = 1
        for i in range(c):
            kaitou = input(f"{x}文字目の欠損文字を入れてください")
            if kaitou in k:
                print("正解")
                x+=1
                k.remove(str(kaitou))
            else:
                print("不正解")
                print("--------------------")
                if xyz == 4 and len(k)!=0:
                    print("GAME OVER")
                break
            if len(k)==0:
                print("終了")
                break
start = datetime.datetime.now()
main()
end = datetime.datetime.now()
print(end-start)