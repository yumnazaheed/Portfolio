#Quadratic.py
import math
print('This program finds the real solution to a quadratic n ')
try:
    a,b,c=eval(input("please enter the co-efficients (a,b,c):"))
    diskRoot=math.sqrt(b*b-4*a*c)
    root1=(-b+diskRoot)/(2*a)
    root2=(-b-diskRoot)/(2*a)
    print("\n The solutions are: ",root1,root2)
except ValueError as excobj:
    if str(excobj)=="math domain error":
        print("no Real roots")
    else:
        print( "you didn't give me the right number of co-efficients")
except NameError:
    print("\n you didn't enter 3 numbers")
except TypeError:
    print("\n your inputs were not all numbers")
except SyntaxError:
    print("\n your input wasn't in the correct form, missing comma?")
except:
    print("\n something went wrong. sorry!")
