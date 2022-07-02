#TODO

money=int(input())
lu=float(input())
month=int(input())

#此為格式化輸出之標頭
print('%s \t  %s' % ('Month', 'Amount'))
#TODO


    #此為格式化輸出之內容，需置於置於迴圈中
for i in range(1,month+1):
    money=money + money * lu / 1200
    print('%3d \t %.2f' % (i, money))
