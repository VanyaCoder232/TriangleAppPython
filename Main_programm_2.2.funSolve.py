import tkinter as tk # Что юзали
from tkinter import END, ttk,Canvas
from tkinter import Listbox, Variable
import math

#Функция рисования треугольника
def paint_triangle(a:float=3,b:float=3,c:float=3,
				   A:float=60,B:float=60,C:float=60.0):
	canv.delete('all')
	maxSide = max([a,b,c])
	a=a/maxSide
	b=b/maxSide
	c=c/maxSide
	A=math.radians(A)
	B=math.radians(B)
	C=math.radians(C)
	points = [	[25,170],
				[175,170],
				[0,0]]
	maxLen = math.hypot((points[0][0]-points[1][0]),(points[0][1]-points[1][1]))
	if A == max(A,B,C):
		canv.create_text(points[0][0],points[0][1]+10,anchor="nw",text=f"B={round(math.degrees(B),3)}°",fill="green")
		canv.create_text(points[1][0],points[1][1]+10,anchor="n",text=f"C={round(math.degrees(C),3)}°",fill="blue")
		canv.create_line(*points[0], *points[1],fill="red",width=3)

		points[2][0] = points[1][0] - (maxLen*b*math.cos(C))
		points[2][1] = points[1][1] - (maxLen*b*math.sin(C))
		
		canv.create_line(*points[1],*points[2],fill="green",width=3)
		canv.create_line(*points[0],*points[2],fill="blue",width=3)
		canv.create_text(points[2][0],points[2][1]-5,anchor="s",text=f"A={round(math.degrees(A),3)}°",fill="red")

		midBC = [(points[0][0]+points[1][0])/2,(points[0][1]+points[1][1])/2]
		midAC = [(points[2][0]+points[1][0])/2,(points[2][1]+points[1][1])/2]
		midAB = [(points[2][0]+points[0][0])/2,(points[2][1]+points[0][1])/2]

		canv.create_text(  midBC[0],midBC[1]+10 ,anchor="n",text=f"a={round(a*maxSide,3)}",fill="red")
		canv.create_text(  midAC[0]+10,midAC[1] ,anchor="sw",text=f"b={round(b*maxSide,3)}",fill="green")
		canv.create_text(  midAB[0]-5,midAB[1]-5 ,anchor="se",text=f"c={round(c*maxSide,3)}",fill="blue")	
	elif B == max(A,B,C):
		canv.create_text(points[0][0],points[0][1]+10,anchor="nw",text=f"A={round(math.degrees(A),3)}°",fill="red")
		canv.create_text(points[1][0],points[1][1]+10,anchor="n",text=f"C={round(math.degrees(C),3)}°",fill="blue")
		canv.create_line(*points[0], *points[1],fill="green",width=3)

		points[2][0] = points[1][0] - (maxLen*a*math.cos(C))
		points[2][1] = points[1][1] - (maxLen*a*math.sin(C))
		
		canv.create_line(*points[1],*points[2],fill="red",width=3)
		canv.create_line(*points[0],*points[2],fill="blue",width=3)
		canv.create_text(points[2][0],points[2][1]-5,anchor="s",text=f"B={round(math.degrees(B),3)}°",fill="green")

		midAC = [(points[0][0]+points[1][0])/2,(points[0][1]+points[1][1])/2]
		midBC = [(points[2][0]+points[1][0])/2,(points[2][1]+points[1][1])/2]
		midAB = [(points[2][0]+points[0][0])/2,(points[2][1]+points[0][1])/2]

		canv.create_text(  midBC[0],midBC[1] ,anchor="sw",text=f"a={round(a*maxSide,3)}",fill="red")
		canv.create_text(  midAC[0],midAC[1]+10 ,anchor="n",text=f"b={round(b*maxSide,3)}",fill="green")
		canv.create_text(  midAB[0]-5,midAB[1]-5 ,anchor="se",text=f"c={round(c*maxSide,3)}",fill="blue")
	
	elif C == max(A,B,C):
		canv.create_text(points[0][0],points[0][1]+10,anchor="nw",text=f"A={round(math.degrees(A),3)}°",fill="red")
		canv.create_text(points[1][0],points[1][1]+10,anchor="n",text=f"B={round(math.degrees(B),3)}°",fill="green")
		canv.create_line(*points[0], *points[1],fill="blue",width=3)

		points[2][0] = points[1][0] - (maxLen*a*math.cos(B))
		points[2][1] = points[1][1] - (maxLen*a*math.sin(B))
		
		canv.create_line(*points[1],*points[2],fill="red",width=3)
		canv.create_line(*points[0],*points[2],fill="green",width=3)
		canv.create_text(points[2][0],points[2][1]-5,anchor="s",text=f"C={round(math.degrees(C),3)}°",fill="blue")

		midBC = [(points[1][0]+points[2][0])/2,(points[1][1]+points[2][1])/2]
		midAC = [(points[0][0]+points[2][0])/2,(points[0][1]+points[2][1])/2]
		midAB = [(points[0][0]+points[1][0])/2,(points[0][1]+points[1][1])/2]

		canv.create_text(  midBC[0]+10,midBC[1] ,anchor="sw",text=f"a={round(a*maxSide,3)}",fill="red")
		canv.create_text(  midAC[0]-5,midAC[1]-5 ,anchor="se",text=f"b={round(b*maxSide,3)}",fill="green")
		canv.create_text(  midAB[0],midAB[1]+5 ,anchor="n",text=f"c={round(c*maxSide,3)}",fill="blue")
# Функция, решающая треугольники. 
def Solve_Triangle(a,b,c,A,B,C):
	arr = []
	A = math.radians(A)
	B = math.radians(B)
	C = math.radians(C)
	# сторона по т. косинусов
	if a ==0 and A>0 and b>0 and c>0:
		a=math.sqrt(b**2 + c**2 - 2*b*c*math.cos(A))
		arr.append(f"""\n\n{len(arr)+1}. Найти a по т. косинусов:\n a= sqrt(b^2 + c^2 - 2*b*c*cos A)""")
	elif b ==0 and B>0 and a>0 and c>0:
		b=math.sqrt(a**2 + c**2 - 2*a*c*math.cos(B))
		arr.append(f"""\n\n{len(arr)+1}. Найти b по т. косинусов:\n  b = sqrt(a^2 + c^2 - 2*a*c*cos B)""")
	elif c ==0 and C>0 and a>0 and b>0:
		c=math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C))
		arr.append(f"""\n\n{len(arr)+1}. Найти c по т. косинусов:\n c= sqrt(a^2 + b^2 - 2*a*b*cos C""")


	# Углы по т. косинусов
	if A==0 and B==0 and C==0 and a>0 and b>0 and c>0: 
		A=math.acos( (b**2 + c**2 - a**2) / (2*b*c) )
		B=math.asin((b * math.sin(A)) / a)
		C=math.pi - A - B 
		arr.append(f"""\n1. Найти А по т. косинусов:\n A = arccos( (b^2 + c^2 - a^2) / (2*b*c) ) \n
				2. Найти B по т. синусов: \n B = arcsin(b * math.sin(A) / a)\n
				3. Найти С по т. о сумме углов: \n C = 180° - A - B """)
		return a, b, c, math.degrees(A), math.degrees(B), math.degrees(C),arr
	# Углы по т. синусов
	if a>0 and A==0:
		if b>0 and B>0:
			A=math.asin((a * math.sin(B)) / b)
			arr.append(f"""\n\n{len(arr)+1}. Найти A по т. синусов:\n A = arcsin(a * sin(B) / b)""")
		elif c>0 and C>0:
			A=math.asin((a * math.sin(C)) / c)
			arr.append(f"""\n\n{len(arr)+1}. Найти A по т. синусов:\n A = arcsin(a * sin(C) / c)""")
	elif b>0 and B==0:
		if a>0 and A>0:
			B=math.asin((b * math.sin(A)) / a)
			arr.append(f"""\n\n{len(arr)+1}. Найти B по т. синусов:\n B=arcsin(b * sin(A) / a)""")
		elif c>0 and C>0:
			B=math.asin((b * math.sin(C)) / c)
			arr.append(f"""\n\n{len(arr)+1}. Найти B по т. синусов:\n B=arcsin(b * sin(C) / c)""")
	elif c>0 and C==0:
		if a>0 and A>0:
			C=math.asin((a * math.sin(A)) / a)
			arr.append(f"""\n\n{len(arr)+1}. Найти C по т. синусов:\n C=arcsin(c * sin(A) / a)""")
		elif B>0 and b>0:
			C=math.asin((c * math.sin(B)) / b)
			arr.append(f"""\n\n{len(arr)+1}. Найти C по т. синусов:\n C=arcsin(c * sin(B) / b)""")
	# Углы по т. суммы углов
	if A>0 and B>0 and C==0: 
		C=math.pi - A - B
		arr.append(f"""\n\n{len(arr)+1}. Найти C по т.о сумме углов:\n C = 180° - A - B""")
	elif A>0 and C>0 and B==0: 
		B=math.pi - A - C
		arr.append(f"""\n\n{len(arr)+1}. Найти В по т.о сумме углов:\n В = 180° - A - С""")
	elif B>0 and C>0 and A==0: 
		A=math.pi - B - C
		arr.append(f"""\n\n{len(arr)+1}. Найти А по т.о сумме углов:\n А = 180° - A - С""")
	# стороны по т. синусов
	if a==0 and A>0:
		if b>0 and B>0:
			a=math.sin(A) * b / math.sin(B)
			arr.append(f"""\n\n{len(arr)+1}. Найти а по т. синусов:\n а= sin(A) * b / sin(B)""")
		elif c>0 and C>0:
			a=math.sin(A) * c / math.sin(C)
			arr.append(f"""\n\n{len(arr)+1}. Найти а по т. синусов:\n а= sin(A) * с / sin(С)""")
	if b==0 and B>0:
		if a>0 and A>0:
			b=math.sin(B) * a / math.sin(A)
			arr.append(f"""\n\n{len(arr)+1}. Найти b по т. синусов:\n b = sin(B) * a / sin(A)""")
		elif c>0 and C>0:
			b=math.sin(B) * c / math.sin(C)
			arr.append(f"""\n\n{len(arr)+1}. Найти b по т. синусов:\n b = sin(B) * c / sin(C)""")
	if c==0 and C>0:
		if a>0 and A>0:
			c=math.sin(C) * a / math.sin(A)
			arr.append(f"""\n\n{len(arr)+1}. Найти c по т. синусов:\n c = sin(C) * a / sin(A)""")
		elif b>0 and B>0:
			c=math.sin(C) * b / math.sin(B)
			arr.append(f"""\n\n{len(arr)+1}. Найти c по т. синусов:\n c = sin(C) * b / sin(B)""")
	return a, b, c, math.degrees(A), math.degrees(B), math.degrees(C),arr
	
def CheckAndСhangeFormat(string:str):
		if string.isdigit():
			return float(string)

		elif "," in string:
			string = string.replace(",",".")

		if "." in string:
			str1,str2 = string.split(".")

			if str1.isdigit() and str2.isdigit():
				return float(string)
				 
			else:
				label_main.configure(text="Некорректный ввод")
				return "False"

		else:
			label_main.configure(text="Некорректный ввод")
			return "False"

# Функции открытия окон
def HI_window():
    
	# Циклы выравнивания рядов
	for r in range(10): root.rowconfigure(index=r, weight=0)
	for c in range(6): root.columnconfigure(index=c, weight=0)
	for r in range(3): root.rowconfigure(index=r, weight=1)
	for r in range(3): root.columnconfigure(index=r, weight=1)
 
	#Цикл очистки всех Entry после выхода в нач.окно
	for entry in [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9,entry_10,entry_11,entry_12]:
		entry.delete(0,END)

	#Цикл сворачивания виджетов
	for hidden_widget in [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9,entry_10,entry_11,entry_12,
							label_1,label_2,label_3,label_4,label_5,label_6,label_7,label_8,label_9,

							button_solve,button_clear_triangles,button_conv,button_clear_conv,button_conv_root,button_clear_root,button_back,

							info_listbox,canv,labelForDescribeSteps]:

		hidden_widget.grid_forget()


	#Цикл для развёртывания кнопок
	COLUMN = 0
	for button in [button_1,button_2,button_3]:
		button.grid(column=COLUMN,row=1,columnspan=1,rowspan=1, sticky="nsew", ipadx=6, ipady=6, padx=4, pady=4)
		COLUMN +=1

	label_main.configure(text="Добро пожаловать в окно для решения треугольников!")
def window_solve_triangles():  
	label_main.configure(text = "Ввод данных для решения треугольников")

	for button in [button_1,button_2,button_3]:
		button.grid_forget()

	for r in range(10): root.rowconfigure(index=r, weight=1)
	for c in range(6): root.columnconfigure(index=c, weight=1)

	for ROW ,widgetInColumn0 in zip( [1,2,3,5] , [label_1,label_2,label_3,label_7] ):
		widgetInColumn0.grid(column=0,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
  
	for ROW ,widgetInColumn1 in zip( [1,2,3,5,7] , [entry_1,entry_2,entry_3,entry_7,entry_9] ):
		widgetInColumn1.grid(column=1,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
  
	for ROW ,widgetInColumn2 in zip( [1,2,3,5,7,8] , [label_4,label_5,label_6,label_8,label_9,entry_12] ):
		widgetInColumn2.grid(column=2,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
  
	for ROW ,widgetInColumn3 in zip( [1,2,3,5,7] , [entry_4,entry_5,entry_6,entry_8,entry_10] ):
		widgetInColumn3.grid(column=3,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
  
	for ROW ,widgetInColumn4 in zip( [1,2,5,7,8] , [button_solve,button_clear_triangles,button_conv,button_conv_root,button_clear_root] ):
		widgetInColumn4.grid(column=4,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
  
	for ROW ,widgetInColumn5 in zip( [5,7,9] , [button_clear_conv,entry_11,button_back] ):
		widgetInColumn5.grid(column=5,row=ROW,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
    
	labelForDescribeSteps.grid(column=6,row=1,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
	canv.grid(column=5,row=1,columnspan=1,rowspan=3,sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
	for entry in [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_10,entry_11]:
		entry.insert(0 ,"0.0")
    
	entry_12.insert(0,"2.0")
	entry_9.insert(0,"1.0")
	paint_triangle()
def window_about_authors():
	root.columnconfigure(index=2, weight=0)
	root.columnconfigure(index=0, weight=2)

	for button in [button_1,button_2,button_3]:
		button.grid_forget()

	label_main.configure(text="Авторы, создатели и люди, содействовавшие созданию программы")
	info_listbox.configure(listvariable=Variable(value=authors))
	info_listbox.grid(column=0,row=1,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=170, ipady=6, padx=4, pady=4)
	button_back.grid(column=1 ,row=2,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
def window_about_programm():
	root.columnconfigure(index=2, weight=0)
	root.columnconfigure(index=0, weight=2)

	for button in [button_1,button_2,button_3]:
		button.grid_forget()

	label_main.configure(text="Информация о программе (История, инструкция и пр.)")
	info_listbox.configure(listvariable=Variable(value=about_programm))
	info_listbox.grid(column=0,row=1,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=170, ipady=6, padx=4, pady=4)
	button_back.grid(column=1 ,row=2,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)

# Функции главного окна:
def solve():
	#Тут происходит получение данных, их проверка, ввод данных в класс и вывод данных
	#Локальная переменная, считающая число введённых элементов
	Count=0
  
	A = CheckAndСhangeFormat(entry_1.get())
	B = CheckAndСhangeFormat(entry_2.get())
	C = CheckAndСhangeFormat(entry_3.get())
 
	a = CheckAndСhangeFormat(entry_4.get())
	b = CheckAndСhangeFormat(entry_5.get())
	c = CheckAndСhangeFormat(entry_6.get())

	for i in [a,b,c,A,B,C]:
		if i == "False":
			label_main.configure(text="Некорректный ввод")
			return
		# Проверка на углы и стороны <0
		if i<0:
			label_main.configure(text = "Угол или сторона не могут быть отрицательными")
			return
			
		
  	# Проверка на число введённых элементов
	if a>0:
		Count+=1
	if b>0:
		Count+=1
	if c>0:
		Count+=1
	if A>0:
		Count+=1
	if B>0:
		Count+=1
	if C>0:
		Count+=1

	if Count<3:
		label_main.configure(text="Пожалуйста, введите минимум 3 элемента треугольника (стороны или углы)")
		return

	# Проверка на наличие сторон
	if a==0 and b==0 and c==0:
		label_main.configure(text="Пожалуйста, введите хотя бы 1 сторону")
		return

	elif ((a+b<=c or a+c<=b or b+c<=a) and
		a>0 and b>0 and c>0):

		label_main.configure(text= "Две стороны не могут быть равны или меньше третьей")
		return
	
	a,b,c,A,B,C,describ = Solve_Triangle(a, b, c, A, B, C)
 
	for i in [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6]:
		i.delete(0,END)

	entry_1.insert(0, str(A))
	entry_2.insert(0, str(B))
	entry_3.insert(0, str(C))
	entry_4.insert(0, str(a))
	entry_5.insert(0, str(b))
	entry_6.insert(0, str(c))
	paint_triangle(a,b,c,A,B,C)
	labelForDescribeSteps.configure(text= describ)
def clear_triangles():
    
	for i in [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6]:
		i.delete(0,END)
		i.insert(0,"0.0")

	label_main.configure(text = "Ввод данных для решения треугольников")
	paint_triangle()
	labelForDescribeSteps.configure( text="""Пояснение, что делать \n чтобы решить треугольник""")
def convert():

	a = CheckAndСhangeFormat(entry_7.get())

	if (a != "False") and (a != 0):
		entry_8.delete(0,END)
		entry_8.insert(0,str(math.radians(a)))

	elif a == 0:
		a = CheckAndСhangeFormat(entry_8.get())

		if (a != "False") and (a != 0):
			entry_7.delete(0,END)
			entry_7.insert(0,str(math.degrees(a)))
		elif (a == "False"):
			label_main.configure(text = "Некорректный вывод")

	else:
		label_main.configure(text = "Некорректный вывод")
def clear_conv():
	for i in [entry_7,entry_8]:
		i.delete(0,END)
		i.insert(0,"0.0")

# Функции счёта корней
def conv_root():

	a = CheckAndСhangeFormat(entry_9.get())
	b = CheckAndСhangeFormat(entry_10.get())
	c = CheckAndСhangeFormat(entry_12.get())

	if (a !="False") and (b !="False") and (c !="False"):
		entry_11.delete(0,END)
		entry_11.insert(0, str(a * b ** (1/ c)))

	else:
		label_main.configure(text="Некорректный ввод")   
def clear_root():
    
	for entry in [entry_9,entry_10,entry_11,entry_12]:
		entry.delete(0,END)

	entry_9.insert(0, "1.0")
	entry_10.insert(0, "0.0")
	entry_11.insert(0, "0.0")
	entry_12.insert(0,"2.0")
# Инициализация всего, что нужно
#*************************************************************************************************************
root= tk.Tk()
root.title("Программа для решения треугольников")
root.geometry('1100x600')
for r in range(3): root.rowconfigure(index=r, weight=1)
for r in range(3): root.columnconfigure(index=r, weight=1)

# Инициализация виджетов приветственного окна
label_main = ttk.Label(text="Добро пожаловать в окно для решения треугольников!")
label_main.grid(column=0,row=0,columnspan=4,rowspan=1, ipadx=6, ipady=6, padx=4, pady=4)
button_1 = ttk.Button(text= "О программе",command=window_about_programm)
button_1.grid(column=0,row=1,columnspan=1,rowspan=1, sticky="nsew", ipadx=6, ipady=6, padx=4, pady=4)
button_2 = ttk.Button(text= "Решить треугольник",command=window_solve_triangles)
button_2.grid(column=1,row=1,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)
button_3 = ttk.Button(text= "Об авторах",command=window_about_authors)
button_3.grid(column=2,row=1,columnspan=1,rowspan=1, sticky= 'nsew', ipadx=6, ipady=6, padx=4, pady=4)

# Кнопка перехода на приветственное окно (размещается в других окнах)
button_back = ttk.Button(text= "На начальное окно",command=HI_window)

# Инициализация виджетов окна для решения треугольников и т.д.
# Поля ввода
entry_1 = ttk.Entry()
entry_2 = ttk.Entry()
entry_3 = ttk.Entry()
entry_4 = ttk.Entry()
entry_5 = ttk.Entry()
entry_6 = ttk.Entry()
entry_7 = ttk.Entry()
entry_8 = ttk.Entry()
entry_9 = ttk.Entry()
entry_10 = ttk.Entry()
entry_11 = ttk.Entry()
entry_12 = ttk.Entry()
# Надписи
label_1 = ttk.Label(text="угол A (град):", anchor= "center")
label_2 = ttk.Label(text="угол B (град):", anchor= "center")
label_3 = ttk.Label(text="угол C (град):", anchor= "center")
label_4 = ttk.Label(text="сторона a (BC):", anchor= "center")
label_5 = ttk.Label(text="сторона b (AC):", anchor= "center")
label_6 = ttk.Label(text="сторона c (AB):", anchor= "center")
label_7 = ttk.Label(text="Градусы:", anchor= "center")
label_8 = ttk.Label(text="Радианы:", anchor= "center")
label_9 = ttk.Label(text=" ==>  A * N√B  <== \n                 /\ \n                 | |", anchor= "center")
labelForDescribeSteps = ttk.Label(anchor= "center",
								  text="""Пояснение, что делать \n чтобы решить треугольник""")
# Кнопки
button_conv = ttk.Button(text= "Перевести",command=convert)
button_clear_conv = ttk.Button(text= "Очистить конвертер",command=clear_conv)
button_solve = ttk.Button(text= "Решить",command=solve)
button_clear_triangles = ttk.Button(text= "Очистить данные",command=clear_triangles)
button_conv_root = ttk.Button(text= "=",command=conv_root)
button_clear_root = ttk.Button(text= "Очистить корни",command=clear_root)
#Холст
canv = Canvas(bg="white",width=200,height=150)
#********************************************************************************************************

# Списки для информации об авторах и программе
info_listbox = Listbox()
authors = 	  	 ["Крестьянников Иван - создатель программы", 
				  "",
				  "Люди из школы, сподвигшие меня сделать эту программу:", 
                  "Подакова Светлана Сергеевна - учитель информатики",
                  "Усольцева Наталья Петровна - учитель математики, спасибо за задачи",
				  "", 
				  "Люди из IT-куба, сподвигшие меня сделать приложение на Android:",
				  "Попов Владимир - андроид разработчик, скинул мне гайд на Android",
				  "Самолов Алексей Александрович - Преподаватель в IT-кубе",
				  "", 
                  "Python - язык программы, Гвидо Ван Россум, спасибо за язык"]

about_programm = ["Данная программа продаже и/или модификации НЕ ПОДЛЕЖИТ",
                  "использование согласовывать с автором программы",
                  "(можно попросить дать попользоваться)",
				  "",
                  "История создания: (Если нужна инструкция - листайте ниже)",
                  "",
       			  "Данная программа была создана для решения задач о треугольниках.",
                  "Изначально я (автор), когда учился в школе, столкнулся с этими задачами",
                  "в 8-м классе. Тогда были выучены теоремы для их решения.",
                  "Однако у меня не было своего калькулятора.",
                  "И они решались м-е-е-е-дленно. В общем больная была тема...",
                  "Спустя время, когда задачи эти уже прошли (и к ним не вернулись),",
                  "Я обучился программированию, но горечь осталась.",
                  "И вот, когда наступили летние каникулы (и было много времени)",
                  "меня осенило - А что мне мешает сделать это?",
                  "И я сделал.",
                  "Думал, что мой учитель математики рассердистся:",
                  "Я посмел применить великую силу программирования против её задач.",
                  "Но она порадовалась, сказала, что это будет хороший проект!",
                  "Учитель информатики сказала то же самое.",
                  "Я так и сделал. И не жалею.",
                  "Это моя самая большая программа за всю мою историю программирования.",
                  "(на момент сент. 2024).",
                  "Я написал её для себя, чтобы излить горечь, выразить чувства.",
                  "Буду признателен, пользователь, если ты дочитаешь это до конца,",
                  "поймёшь меня. Я впервые с людьми и с тобой общаюсь через интерфейс,",
                  "возможно сквозь время, возможно прога, нет, творение переживёт меня",
                  "и расскажет обо мне людям, возможно, это письмо в будущее.",
                  "Чувство необычайное, когда ты создал что-то стоящее, вложил душу,",
                  "оставил часть себя, отдаёшь творение в свет, на суд людям. Волнительно.",
                  "и творение - отпечаток твоего состяния в момент его создания,",
                  "или коллаж состояний, отпечатков, следы истории. И вы - зритель, слушатель,",
                  "пользователь слушаете, чувствуете меня. Это прекрасно.",
                  "Человечество... Общество... Наследие... Преемственность поколений",
                  "Это прекрасное чувство, когда ты оставляешь что-то после себя,",
                  "чтобы этим воспользовались другие и продолжили после тебя...",
                  "Осознание, что твои творения, твои действия останутся в истории",
                  "вселяют веру и желание жить...",
                  "Надеюсь, вы тоже это испытаете, а если испытали, то меня поймёте...",
                  "",
                  "",
                  "Инструкция по использованию:",
                  "",
                  "1.   Пожалуйста, НЕ вводите слова, буквы и пр. символы, не являющиеся цифрами",
                  "     в окна ввода (Ничего не будет, но программа известит о неправильном вводе).",
                  "",
                  "2.   Числа можно вводить в формате:",
				  "     Просто число (3), Через точку (3.14) и через запятую (3,14)",
				  "     Но НИГДЕ НЕЛЬЗЯ вводить отрицательные числа",
                  "",
                  "3.   Данная программа призвана решать треугольники т.е.:",
                  "     получать имеющиеся элементы треугольника (углы и стороны)",
                  "     и находить оставшиеся согласно теоремам о треугольниках.",
                  "",
                  "3.1. Минимальный набор вводимых элементов:",
                  "     3 стороны,",
                  "     2 стороны и 1 угол (любой),",
                  "     1 сторона и 2 угла (любые),",
                  "     Если что-то введено не так, программа подскажет, изменив верхнюю надпись",
                  "3.2. В программе нельзя отметить, являются ли стороны или углы равными по условию.",
                  "",
                  "4. В программу встроены конвертер углов и калькулятор корней:",
                  "",
                  "    4.1. Конвертер углов. Конвертирует градусы в радианы и обратно.",
                  "        Если оба поля заполнены - приоритет отдаётся переводу град. -> рад.",
                  "",
                  "    4.2. Калькулятор корней. Переводит корни n-й степени и их множитель (7 * 2√2 =)",
                  "        в число с плав. точкой (= 9.899494936611665)."
                  ]

root.mainloop()
