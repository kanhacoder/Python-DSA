file1 = open("/home/user/Downloads/knh/asdf.txt","r")
file = file1.read()
words = file.split()
for i in words:
    if len(i)>4:
        print(i)
    