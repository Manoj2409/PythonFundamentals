num1=11
num2=num1

print(num1,end=" ")
print(num2)
print("num 1 id : ",id(num1))
print("num 2 id : ",id(num2))
num1=30

print(num1,end=" ")
print(num2)
print("num 1 id : ",id(num1))
print("num 2 id : ",id(num2))

dict1={
    "value":10
}
dict2=dict1

print("dict1 :",dict1)
print("dict2 :",dict2)

print("dict1 id",id(dict1))
print("dict2 id",id(dict2))

dict2['value']=100

print("dict1 :",dict1)
print("dict2 :",dict2)

print("dict1 id",id(dict1))
print("dict2 id",id(dict2))

#integer in immutable where as dict is mutable
# since there is no value pointed at value 10 ,
# it will be taken care by process garbage collection

