import os

print(os.name)
print(os.getenv("USERNAME"))
print(os.getcwd())
#os.mkdir("Temporary")
#os.makedirs(r"C:\Users\ruban.kumar\Desktop\Python\First\Second\Third")

#os.system("regedit")
os.chdir(r"C:\Users\\ruban.kumar\Desktop\\")
#os.startfile(r"C:\Users\\ruban.kumar\Desktop\\Ruban_Kumar_2178481_Insurance.docx")
pathe = r"C:\Users\\ruban.kumar\Desktop\\new"
d, f = os.path.split(r"C:\Users\ruban.kumar\Desktop\new\kumaruba.crt")
for root, dirs, files in os.walk(pathe):
    print(root)
    for _file in files:
        print(_file)
print("filename: %s" % f)
print("path: %s" % d)
path = os.path.join(d, f)
size = os.path.getsize(path)
print("%s Kbs" % str(size//1024))
print(os.path.exists(r"C:\Users\\ruban.kumar\Desktop\whatthehell\\"))
print(dir(os.path))
print(os.path.abspath("..\system.log"))
encode = os.fsencode(path)
print(encode)
decode = os.fsdecode(encode)
print(decode)
#Creating a link/unix or shortcut/windows


