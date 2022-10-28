#a=int("10")#10という文字列を整数に変換してaに代入
#b=float("1.5")#1.5という文字列を数字に変換してbに代入

for i in range(1,4): #コロンが入っていることに注意
    print(i,"人目") #タブでずらしていることに注意！

    name=input("お名前は？")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=40:
         print(name,"さん、内臓脂肪貯蓄注意です")
    else:
         print(name,"さん、腹囲は問題ありません")