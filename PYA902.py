#如果不需要做分行處理，用 read() 一次性把檔案讀出

f = open("read.txt","r",encoding="utf-8")
             
data = f.read() #data將會是字串格式 type(data) = <class 'str'>
             
f.close()

nums = list(map(int, data.split(" ")))
             
print(sum(nums))
