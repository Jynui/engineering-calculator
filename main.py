import math
import os
import platform
os.environ['TERM'] = 'xterm-256color'
def clear_console():
    system_platform = platform.system()
    if system_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
print("калькулятор Тагира")
while True:
    num1=int(input("введите первое число: "))
    op=str(input("выберите действие(+,-,*,/,sin,cos,tan,!,#,^): "))
    if op!="!" and op!='sin' and op!="cos" and op!="tan" and op!="#":
        num2 = int(input("введите второе число: "))
    else:
        num2=2
    if op!="+" and op!="-" and op!="*" and op!="^" and op!="sin" and op!="cos" and op!="tan":
        if num2==0 or num1==0:
            op="_"
    match op:
        case "+":
            clear_console()
            print(num1+num2)
        case "-":
            clear_console()
            print(num1-num2)
        case "*":
            clear_console()
            print(num1*num2)
        case "/":
            clear_console()
            print(num1/num2)
        case "^":
            clear_console()
            print(num1**num2)
        case "#":
            clear_console()
            print(num1**0.5)
        case "!":
            clear_console()
            print(math.factorial(num1))
        case"sin":
            clear_console()
            print(math.sin(num1))
        case"cos":
            clear_console()
            print(math.cos(num1))
        case"tan":
            clear_console()
            print(math.tan(num1))
        case _ :
            clear_console()
            print("попробуйте еще раз")