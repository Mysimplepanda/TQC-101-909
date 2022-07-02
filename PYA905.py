#list: 一個一個處理資料
#string.replace(old_str, new_str)

f_name = input()
mystr = input()

with open(f_name,"r",encoding="utf-8") as hfile:
    data = hfile.read()
    
    print("=== Before the deletion")
    print(data)
    
    print("=== After the deletion")
    new_data = data.replace(mystr, "")
    print(new_data)
