from rich.traceback import install
install(show_locals=True)

import customtkinter, tkinter, random , os
from rich import print
from PIL import Image

anim=0
version='0.8.0'
app = customtkinter.CTk()
i=0
keys = ['1' for g in range(9)]
print(keys)
test = 9

fl = True

Attack = False


buttonn = []

HumanWins=0
DumbAIWins=0

defaultTitle = 'бот--> o  x <--ты '

win = False
app.geometry('440x450')
app.title(f'{defaultTitle}            Крестики-нолики v{version}')
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".")
Ximg = customtkinter.CTkImage(
  light_image=Image.open(os.path.join(image_path, "2.png")),
  dark_image=Image.open(os.path.join(image_path, "2.png")), size=(48,48)
  )
Oimg = customtkinter.CTkImage(
  light_image=Image.open(os.path.join(image_path, "1.png")),
  dark_image=Image.open(os.path.join(image_path, "1.png")), size=(48,48)
  )
Emptyimg = customtkinter.CTkImage(
  light_image=Image.open(os.path.join(image_path, "empty.png")),
  dark_image=Image.open(os.path.join(image_path, "empty.png")), size=(48,48)
  )
def welcome():
  global anim
  if anim == 0:
    app.title('                                                        Добро пожаловать!')
    anim=anim+1
    app.mainloop()
  if anim == 1:
    app.title(f'Крестики нолики v{version}')
    app.mainloop()
  else: pass
  app.after(10000,welcome)


# [v] Сделать так чтобы я не мог ходить не в свою клетку
# [v] Рандомно комп ходил
# [v] Марафет
# [v] Тактика для бота

target=8

#Функция для рестарта
def restart():
  global win,keys,target,Attack
  for popopo in range(0,9):
    buttonn[popopo].configure(image=Emptyimg)
  target=8
  win=False
  Attack = False
  keys = ['1' for g in range(9)]
  print('[red]----------RESTART--------[red/]')
  
  for ooooo in range(0,9):
    buttonn[ooooo].configure(state=tkinter.NORMAL)

def bot():
  global target, fl, Attack
  num=[]
  Attack=False
  #НАПАДЕНИЕ
  
  
  #   СТРОКИ
  
  for n in 0,3,6:
    #global Attack
    if keys[n:n+3].count('o')==2 and keys[n:n+3].count('1')==1 and not Attack:
      
      test=keys[n:n+3].index('1')+n
      print(test)
      target=test
      Attack=True
      
  #   СТОЛБЦЫ
  for n in 0,1,2: # error in '2'
    
    if keys[n:n+6:3].count('o')==2 and keys[n:n+7:3].count('1')==1 and not Attack:
      
      test=keys[n:n+3].index('1')*3+n
      print(test)
      target=test
      Attack=True
      
  #      ДИАГОНАЛИ
    if keys[0]=='o' and keys[4]=='o' and keys[8]=='1'and not Attack: 
      test=8
      print(test)
      target=test
      Attack=True
    if keys[0]=='1' and keys[4]=='o' and keys[8]=='o'and not Attack:
      test=0
      print(test)
      target=test
      Attack=True
    if keys[0]=='o' and keys[4]=='1' and keys[8]=='o'and not Attack:
      test=4
      print(test)
      target=test
      Attack=True


    if keys[2]=='o' and keys[4]=='o' and keys[6]=='1'and not Attack:
      test=6
      print(test)
      target=test
      Attack=True
    if keys[2]=='1' and keys[4]=='o' and keys[6]=='o'and not Attack:
      test=2
      print(test)
      target=test
      Attack=True
    if keys[2]=='o' and keys[4]=='1' and keys[6]=='o'and not Attack:
      test=4
      print(test)
      target=test
      Attack=True

  #ЗАЩИТА
  #   СТРОКИ
  if Attack==False:
    for n in 0,3,6: # error

      if keys[n:n+3].count('x')==2 and keys[n:n+3].count('1')==1:
        test=keys[n:n+3].index('1')+n
        print(test)
        target=test
        Attack=True
    #   СТОЛБЦЫ
    for n in 0,1,2:

      if keys[n:n+6+1:3].count('x')==2 and keys[n:n+7:3].count('1')==1 and not Attack: # error in 1
        test=keys[n:n+6+1:3].index('1')*3+n # n:n+3
        print(test)
        target=test
        Attack=True
        

    #      ДИАГОНАЛИ
    if keys[0]=='x' and keys[4]=='x' and keys[8]=='1': 
      test=8
      print(test)
      target=test
      Attack=True
    if keys[0]=='1' and keys[4]=='x' and keys[8]=='x':
      test=0
      print(test)
      target=test
      Attack=True
    if keys[0]=='x' and keys[4]=='1' and keys[8]=='x':
      test=4
      print(test)
      target=test
      Attack=True


    if keys[2]=='x' and keys[4]=='x' and keys[6]=='1':
      test=6
      print(test)
      target=test
      Attack=True
    if keys[2]=='1' and keys[4]=='x' and keys[6]=='x':
      test=2
      print(test)
      target=test
      Attack=True
    if keys[2]=='x' and keys[4]=='1' and keys[6]=='x':
      test=4
      print(test)
      target=test
      Attack=True


    if keys[4]=='1' and not Attack:
        test=4
        print(test)
        target=test
        Attack=True
    elif not Attack:
      for i in range(9):
        if keys[i]=='1':num.append(i)
        try:
          test=random.choice(num)
          print(test)
          
        except IndexError: print('[red][IndexError][/red] Список "num" за пределами. Возможная ничья. [yellow](131 стр.)[/yellow]')
        try:
          target=test
          Attack=True
        except:pass

  keys[target]='o'
  buttonn[target].configure(image=Oimg)
  print(target)
  print(keys)
  print('\n')
  print(keys[0:3])
  print(keys[3:6])
  print(keys[6:9])
  check_of_win()

                           # ['0', '1', '2',
                           #  '3', '4', '5',
                           #  '6', '7', '8']
 
 
# ЭТО НЕ ТРОГАЙ  
def check_of_win():
  global win,HumanWins,DumbAIWins
  if keys[0]==keys[3]==keys[6]=='x' or keys[1]==keys[4]==keys[7]=='x' or keys[2]==keys[5]==keys[8]=='x' or keys[0]==keys[1]==keys[2]=='x' or keys[3]==keys[4]==keys[5]=='x' or keys[6]==keys[7]==keys[8]=='x' or keys[6]==keys[4]==keys[2]=='x' or keys[0]==keys[4]==keys[8]=='x':
    print('ИГРОК')
    for ooooo in range(0,9):
      buttonn[ooooo].configure(state=tkinter.DISABLED)
    win=True
    HumanWins+=1
    app.title(f'{defaultTitle} Игрок выйграл {HumanWins}:{DumbAIWins}')
      
  if keys[0]==keys[3]==keys[6]=='o' or keys[1]==keys[4]==keys[7]=='o' or keys[2]==keys[5]==keys[8]=='o' or keys[0]==keys[1]==keys[2]=='o' or keys[3]==keys[4]==keys[5]=='o' or keys[6]==keys[7]==keys[8]=='o' or keys[6]==keys[4]==keys[2]=='o' or keys[0]==keys[4]==keys[8]=='o':
    print('ИИ')
    for ooooo in range(0,9):
      buttonn[ooooo].configure(state=tkinter.DISABLED)
    win=True
    DumbAIWins+=1
    app.title(f'{defaultTitle}  ИИ выйграл    {HumanWins}:{DumbAIWins}')
  else:
    if win==False and '1' not in keys:
      print('Ничья')
      app.title(f'{defaultTitle}  Ничья             {HumanWins}:{DumbAIWins}')
# ЭТО НЕ ТРОГАЙ


# ЭТО НЕ ТРОГАЙ
def turn(event,btn,i):
  global fl
  if not win:
    if keys[i]=='1':
      keys[i]='x'
      fl = True
      btn.configure(image=Ximg)
      check_of_win()
      if not win:
        bot()
      #app.after(0,bot)
    else: print('эта клетка занята')
    print(keys[i])
# ЭТО НЕ ТРОГАЙ   
    
#Создаём сетку
for c in range(3): app.columnconfigure(index=c, weight=1)
for r in range(4): app.rowconfigure(index=r, weight=1)

#Кнопочка для рестарта
ButtonRestart = customtkinter.CTkButton(app,text='Restart',width=20,command=restart).grid(row=4,column=1)

#Расставляем кнопочки по сетке
for r in range(3):
    for c in range(3):
        btn = customtkinter.CTkButton(app,image=Emptyimg,text='',width=121,height=121,corner_radius=20)
        buttonn.append(btn)
        btn.bind('<Button-1>',lambda event,btn=btn,i=i: turn(event,btn,i))
        btn.grid(row=r, column=c)
        i=i+1

#print(buttonn)


app.mainloop()