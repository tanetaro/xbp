import tkinter
import tkinter.filedialog
import random
import datetime
import os

from PIL import ImageGrab

#ランダムに色を生成する
def make_hexcolor():
	
	color_cd = "";
	for i in range(0, 3):
		color_cd = color_cd + format(int(random.randrange(255)), 'x').zfill(2)
	return color_cd

def change_color():
	global canvas
	for ck in range(0, len(canvas_keys)):
		key_name = canvas_keys[ck]
		tagnm = "fill_" + key_name #変更したい四角のタグ名を生成する
		
		#タグ名で色を変更する
		canvas.itemconfigure(tagnm, fill="#" + make_hexcolor())

root = tkinter.Tk()
canvas_items = {}
canvas_keys = ["main", "second", "third"]

root.title(u"color_mgr") #ウィンドウタイトルを指定

rect_size = 125 #一つの四角のサイズ
canvas_keys = ["main", "second", "third"] #色表示エリアの名前を仮で指定
max_size = rect_size*len(canvas_keys) #canvasの最大幅をあらかじめ計算
root.geometry(str(max_size) + "x500") #ウィンドウサイズを指定

#表示するためのcanvasを生成する
canvas = tkinter.Canvas(root, width=max_size, height=rect_size)

#カラー表示部分の設置
for ck in range(0, len(canvas_keys)):
	key_name = canvas_keys[ck]
	canvas_items[key_name] = {}
	tagnm = "fill_" + key_name #canvasに追加する要素のタグ名を生成
	
	#fillで塗りつぶし色を指定します　初期値は真っ白を指定しています。
	canvas.create_rectangle(rect_size * ck, 0, (rect_size * ck) + rect_size, rect_size, fill="#ffffff", tag=tagnm)

#canvasをウィンドウに配置する
canvas.grid(row=0, column=0, columnspan=4)


btn_0 = tkinter.Button(root, text="色を変える", command=lambda: change_color(), width=10, height=2)
btn_0.grid(row=3, column=1, columnspan=2)


change_color()

root.mainloop()