from random import randint
from datetime import datetime

Narutoquiz_list = []
Narutoquiz_list.append(['Who is the first Hokage in Konoha?', 
                        'Naruto', 'Hoshirama', 'Madara', 'Itachi', 2])
Narutoquiz_list.append(['How many paths did the Pain from Akatsuke?', 
                        '9','8','7','6', 4])
Narutoquiz_list.append(['How many vullages participated in World War 4 Shinobi?', 
                        '2','3', '4', '5', 4])
Narutoquiz_list.append(['Who is the second Hokage in Konoha?',
                        'Gaara', 'Shikamaru', 'Tobirama', 'Hoshirama', 3])
Narutoquiz_list.append(['Who gave sharingan to Kakashi Hatake?',
                        'Itachi', 'Shisui', 'Obito', 'Saske', 3])
Narutoquiz_list.append(['', 1])

Narutoquiz_list.append(['', 1])
points = 0

def adv():
  return ''' This is Naruto Shipuden QUIZ application created by Medina Isbaek kyzy in ''' + str(datetime.now().year) + ''' @ AlaToo '''

def selection():
  return '1.This is a quiz\n2.About\n3.NarutoShipuden\n'

def demand():
  global points
  r = randint(0, len(Narutoquiz_list) - 1)
  print(Narutoquiz_list[r][0])
  print('1) ' + Narutoquiz_list[r][1])
  print('2) ' + Narutoquiz_list[r][2])
  print('3) ' + Narutoquiz_list[r][3])
  print('4) ' + Narutoquiz_list[r][4])
 
  answer = int(input("Pick a number of answer: "))
  if answer == 22:
    print(easter_egg())
  elif answer == Narutoquiz_list[r][5]:
    points += 1
    print('You are right, yeppy , you have ' + str(points) + ' point(s) now. Congratulation!')
  else:
    print('Wrong! But do not give up!')

  def easter_egg():
    return ''' _  , /|
◥▔╲┈┈┈┈┈┈┈┈┈╱▔◤
┈╲┈╲╱▔▔▔▔▔╲╱┈╱
┈┈╲┈┈┈┈┈┈┈┈┈╱
┈┈▕┈◢◣┈┈┈◢◣┈▏
┈┈▕┈◥◤┈▃┈◥◤┈▏
┈┈▕╭╮╰┳━┳╯╭╮▏
┈┈▕╰╯┈╰━╯┈╰╯▏
┈┈┈╲▂▂▂▂▂▂▂╱'''

while True:
    choice = input(selection())
    if choice == '3':
        break
    elif choice == '2':
        print(adv())
    elif choice == '1':
        demand()

print('Good bye and Good luck!')
