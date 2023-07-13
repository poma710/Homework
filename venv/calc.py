print("*" * 15, " Калькулятор ", "*" * 15)
print("Для выхода введите q в качестве знака операции")
while True:
 s = input("Знак (+,-,*,/): ") 
 if s == 'q': break
 x = float (input ("x= ") ) 
 у = float (input ("y= ") ) 
 if s == '+':
  print("%.2f" % (x+y)) 
 elif s == '-':
  print("%.2f" % (x-y)) 
 elif s == '*':
  print ("%,2f" % (x * у)) 
 elif s == '/':
  if у != 0:
   print(" %.2f " % (x/y)) 
 else:
  print("Деление на ноль!")
else:
  print("Неверный знак операции!")