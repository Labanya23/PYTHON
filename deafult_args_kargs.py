def sum(num1 , num2):
    result= num1+num2
    return result

total = sum(99,11)
print('total:',total)

#args
#def all_sum(numbers):
#def all_sum(*numbers):
    #* dila jotokhusi  number naia jba
    #jdi number fixed rakta cai
def all_sum(num1,num2,*numbers):
    print(numbers)
    #array moto kora jaba
    for num in numbers:
        print(num)
        sum=sum+num
    return sum
    
total = all_sum(45,46)
print('all sum:',total)

def do_a_lot(*args):
    print(args)
