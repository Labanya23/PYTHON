def full_name(first,last):
    name = f'{first} {last}'
    return name

#take parameter in order jai aga saia aga boshba
#name=full_name('ss','pd')
name=full_name(last='ls',first='pd')
print(name)

#def famous_name(first,last,title,additional):
def famous_name(first,last,**additional):
    name= f' {first} {last}'
    print(addition)
    return name
#print(additional['title'])
for key value in addition.items()
    print(key,value)
return name

name=famous_name(first = 'labanya', last='saha',title='engineer',additional='cse')
ptint(name)

#def function_name(num1,num2,*args,**kargs):

def a_lot(num1,num2):
    sum=num1+num2
    multi=num1*num2
    remain=num1-num2
    #return sum,multi,remain
    return[sum,multi,remain]

everything=a_lot(55,21)
print(everything)
