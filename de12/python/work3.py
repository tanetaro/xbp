name=input("お名前は？")
waist=input("腹囲は？")
age=input("年齢は？")

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪貯蓄注意です")
else:
    print(name,"さん、腹囲は問題ありません")