# -"a" append data ， 找到游標所在的地方，開始往下加

file = open("data.txt","a",encoding="utf-8")

[file.write("\n"+input()) for i in range(5)]
    
file.close()

############################################
# file.read():把資料一次性讀出外，格式也會讀出。

print("Append completed!")
print('Content of "data.txt":')

f = open("data.txt","r",encoding="utf-8")

print(f.read())

f.close()
