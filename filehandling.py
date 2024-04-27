"""
open
read/
write

close

"""

# s=open('filehndl_demo.txt', mode='r')
# print(s.read())
# s.close()


# s=open('filehndl_demo.txt', mode='w')# truncate
# s.write("Bye Bye")
# s.close()

# s=open('filehndl_demo.txt', mode='a')# append
# s.write("hi hi")
# s.close()

# s=open('filehndl_demo.txt', mode='r+')# read and then write
# print(s.read())
# s.write(" r+ mode")
# s.close()

s=open('filehndl_demo.txt', mode='r+')# read and then write
s.write(" w+ mode")
s.seek(0)# file pointer change
print(s.read())
s.close()

