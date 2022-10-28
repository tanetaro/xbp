name="aaa"
waist=85
age=39
body_weight=50
height=170

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪貯蓄注意です")
else:
    print(name,"さん、腹囲は問題ありません")