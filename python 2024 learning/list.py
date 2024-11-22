list1=[1,2,3,4,5]
print(list1)
print(list[0])

list.append(6)

#slicing (n-1)follow korba
list=[1,2,3,4,5,6]
print(list[:3])
print(list[2:3])

print(list[-1:-3])
print(list[-5:-1])
print(list[-1:])
print(list[2,3])
print(list[-1:-4])
print(list[::-1])
print(list[-1:-4:-1])

#first end step
#start = null=0
#end=null=len(list)
#step=null=1

list2=[1,2,3,4,5,6]
print("list",list2)
print("value",list2[0])
print("index_number",list2.index(3))
print(list2[:4:2])
print(list[-1::-1])

#constructor kora
n=(1,2,3,4,5)
print(n)
print(type[n])
list3=list(n)
print(type[list2])
#add
list3.append(6)
print("append",list3)
list3.insert(0,0)
print("insert",list3)
#insert and append r modai insert kon index ai data dita chacan bola dita paren


#duita list kai ak korbo
list1.extend(list3)
print("list",list1)

#remove
list1.pop()
pop_value=list1.pop("6")
print("pop",list1)
a=list1.remove(0)
#list1.clear()

list1.clear()
print("clear",list1)

#update
#for i in list2:
   # print(i)

list2.sort()
print("sort",list2)

#function oi declear oi kora dita parbo sob declear korta parbo
list2.reverse()
#list2.sort(reverse=True)

list2.sort(reverse=True)
print("sort",list2)
list2.reverse()
print("revers",list2)
list3=list2
print(list2)
print("list2",list2)

list3.append(7)
print(list1)
print(list2)
list2.append(60)