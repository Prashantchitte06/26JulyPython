from itertools import count

print("-----1.1: basic example EH------")
a=10
b=2

print("program started")
try:
   print(a/b)          #risky code
except ZeroDivisionError as e:
   print("ZeroDivision Error Handled")          #only msg

print("Hi Hello")
print("program ended")


print("-----1.2: basic example EH------")
a=10
b=0

print("program started")
try:
   print(a/b)          #risky code
except ZeroDivisionError:
   print(a/1)          #only alternate solution

print("Hi Hello")
print("program ended")


print("-----1.3: basic example EH------")
a=10
b=0

print("program started")
try:
   print(a/b)          #risky code
except ZeroDivisionError:
   print(a/1)                            #alternate solution
   print("ZeroDivision Error Handled")   #msg

print("Hi Hello")
print("program ended")


print("-----------2: Example of Multiple Except block-----------")
a=10
b=2

print("program started")
try:
   print(a/b)
except ValueError:
   print("Value Error Handled")
except ZeroDivisionError:
   print("ZeroDivision Error Handled")
print("program ended")



print("-----------3.1: Example of Generic exception-----------")
a=10
b=0

print("program started")
try:
   print(a/b)
except Exception:
   print("Generic exception handled")
print("program ended")


print("-----------3.2: Example of Generic exception-----------")
a=10
b=0

print("program started")
try:
   print(a/b)
except Exception as e:
   print("Generic exception handled")
   print(e)
print("program ended")



print("-----4: Example of Correct way of using Generic exception-------")
a=10
b=0

print("program started")
try:
   print(a/b)
except ValueError:
   print("Value Error Handled")
except ZeroDivisionError:
   print("Zero Division Error")
except Exception as e:
   print("Generic Exception handled")
   print(e)
print("program ended")


print("-----------5: Alternative way of using Generic exception-----------")
a=10
b=0

print("program started")
try:
   print(a/b)
except:
   print("Generic exception handled")
print("program ended")



print("-----------6: finally block-----------")
a=10
b=0

print("program started")
try:
   print(a/b)
except:
   print("Generic exception handled")
finally:
   print("Running finally block")
print("program ended")



