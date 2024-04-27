""""
interupting the normal execution code is called error
"""

a=1
#print(b)

try:
    print('a'+33)
except:
    print("type error")
# except:
#     print("value error")
else:
    print('no error')
finally:
    print("always")