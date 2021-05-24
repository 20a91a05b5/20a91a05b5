n=int(input())
if 1000<=n<2000:
print('total bill is %d',n)
c=(10*n)/100
print('discount on billed amount is %d',c)
print('paid bill is %d',n-c)
elif 2000<=n<3000:
print('total bill is %d',n)
print('discount on billed amount is %d',c)
print('paid bill is %d',n-c)
elif 3000<=n<5000:
print('total bill is %d',n)
print('discount on billed amount is %d',c)
print('paid bill is %d',n-c)
elif n>5000:
print('total bill is %d',n)
print('discount on billed amount is %d',c)
print('paid bill is %d',n-c)
else:
print('you are not eligible for discount')






'''output:
1000
total bill is 1000
discount on billed amount is 100
paid bill is 900'''