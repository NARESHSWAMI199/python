# 'r','w','a','r+'




# with open('hello.html' ,'r') as f:
#     print(f.read())

# with open('file.txt' ,'w') as f: 
#     f.write("nothing is special this will overwirte the file content")
# # the 'w' (write) mode auto create a new file

# with open('file.txt' ,'a') as f:  # the 'a'(append) mode not overwrite
#     f.write(' this is fuck')
    
with open('file.txt' ,'r+') as f:  # 'r+' (read file and write)
    f.seek(len( *[ i for i in f]))
    f.write(' this is writing')