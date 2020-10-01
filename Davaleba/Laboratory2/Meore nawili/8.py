sum = 0
for i in range(1500,2100):
  if i%5==0 and i%7==0:
    while sum<20000:
      sum+=i
print(sum)