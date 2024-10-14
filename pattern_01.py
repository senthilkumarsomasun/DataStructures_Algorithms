
list=[1,3,4,5,6]
travel=[3,3]
start=travel[0]
end=travel[1]-1
print(start)
print(end)
if start >= end :
    start,end=end,start
i=0
val=0
while (start >= i ):
    val=val+list[i]
    i+=1
    
print(val)


