# with open('hello.html','r') as f:
#     with open('output.txt','a') as wf:
#         for i in f.readlines():
#             if '.com' in i:
#                 n = i.split('"')
#                 wf.write(f"{n[1]}\n")


# orignal

# with open('hello.html','r') as f:
#     with open('output.txt','a') as wf:
#         for i in f.readlines():
#             if '<a href=' in i:
#                 pos = i.find("<a href=")
#                 first = i.find('"',pos)
#                 secound = i.find('"',first+1)
#                 url = i[first+1:secound]
#                 wf.write(f"{url} \n")


# accurate

with open('hello.html','r') as f:
    with open('output.txt','a') as wf:
        page = f.read()
        link = True
        while link:
            pos = page.find('<a href=')  # the find is flase the return -1
            if pos == -1:
                link = False
            else:
                first = page.find('"',pos)
                secound = page.find('"',first+1)
                url = page[first+1:secound]
                wf.write(f"{url} \n")
                page = page[secound :]
            
