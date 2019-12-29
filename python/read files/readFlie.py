# open method     open the file using file loaction
# seek method     use for the cursor controll
# close method    use and close the file
# tell            use for check cursor current position
# readline        use for read line by line
# readlines       use for read all lines in one time

# name          this is not a function and display the file name
# closed        this is not a function and return true and false that file closed or not






f = open("hello.html")  # by default the open have read mode else write like 
# f = open("hello.html",'r or w')
print(f"the cursor current position is {f.tell()}")
# print(f.read())
# print(f"the cursor current position is {f.tell()}")
# f.seek(0)   # the seek function set the cursor position
# print(f.read())
# print(f"the cursor current position is {f.tell()}")
print(f.readline(),end='')  
# print(f.readline())  line by line print the file txt
print(f"the cursor current position is {f.tell()}")
f.close()