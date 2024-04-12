##String="HELLO"
##lowercase=""
##for char in String:
##    if"A"<="Z":
##        lowercase+=chr(ord(char)+32)
##    else:
##        lowercase+=char
##print(lowercase)



##String="phython programming"
##space=False
##result=""
##for char in String:
##    if 'a'<=char<='z':
##        result+=chr(ord(char)-32)
##    else:
##        result+=char
##    if char==" ":
##        space=True
##print(result)
##

# Remove the vowels from the string:
##String="Manogari"
##vowels="aeiouAEIOU"
##result=""
##for char in String:
##    if char not in vowels:
##        result+=char
##print(result)




#count the camel case Character
##a="STRing"
##uppercase=""
##for i in a:
##    if i<="A"or i<="Z":
##        uppercase=uppercase+i
##length=len(uppercase)
##print(length)

#check the string

##a="ggf"
##b=True
##if a:
##    first=a[0]
##    for char in a:
##        if char!=first:
##            b=False
##print(b)
##    
##    
##       

#Display longest character:
##names=["Rajesh","helloworld","kingdown"]
##max_length=0
##longest_name=""
##for i in names:
##    if len(i)>max_length:
##        max_length=len(i)
##        longest_name=i
##print(longest_name)

#Check for binary

##Str="101"
##binary=True
##for i in Str:
##    if i!='0' and i!='1':
##        binary=False
##print(binary)

##S="example"
##result=""
##for i in range(len(S)):
##    if i%2==0:
##        result+=S[i]
##print(result)

##String=input("Enter a string:")
##for i in range(len(String),0,-1):
##    print(String[i:])

#Prime Numbers:

##num=int(input("Enter a number:"))
##if num<=1:
##    print("is not a prime number")
##else:
####    prime=True
##    for i in range(2,num):
##        if num%i==0:
##            prime=False
##            break
##    if prime:
##            print("is a prime number",num)
##    else:
##            print("is not a prime number",num)
##


#Fibbanocci Series

##nterms=int(input("Enter a terms:"))
##n1=0
##n2=1
##count=0
##if nterms<=0:
##    print("Enter a positive integers:")
##else:
##    print("Fibbanocci Series:")
##while count<nterms:
##    print(n1)
##    nth=n1+n2
##    n1=n2
##    n2=nth
##    count+=1

#Reverse a integer:
##num=65
##b=0
##while num>0:
##    a=num%10
##    b=(b*10)+a
##    num//=10
##print("Reversed_integer",b)

#Print the same character
##S1=input("Enter a string:")
##S2=input("Enter a another string:")
##for i in S1:
##    for j in S2:
##        if i==j:
##            print(i,end=" ")
         

##para=input("Enter a paragraph:")
##char=input("Enter the character to count:")
##count=0
##for i in para:
##    if i==char:
##        count+=1
##print("The character",char,"appears",count,"times in the paragraph",)
##         
##
##

##para=input("Enter a paragraph:")
##char=input("Enter the character to count:")
##count=0
##for i in para:
##    if i==char:
##        count+=1
##print("The character",char,"appears",count,"times in paragraph")
##

#Password checking
##
##Pwd=input("Enter a password:")
##pre="Tall$%"
##if pre==Pwd:
##    print("Correct Password")
##else:
##    print("Invalid Password")


##String=input("Enter a string:").upper()
##print(String)

##Vowels Replacement:
##
##String=input("Enter a String:")
##Vowels="aeiouAEIOU"
##output=""
##for char in String:
##    if char in Vowels:
##        output+='*'
##    else:
##        output+=char
##print(output)
##


##String="Hello Everyone"
##output=""
##for char in String:
##    if char !=' ':
##        output+=char
##print(output)



##LIST
##Sum Of Array:

##S=[1,2,3]
##Sum=sum(S)
##print(Sum)


##Value equal to index:

##a=[0,1,3,2,5]
##for i in range(len(a)):
##    if i ==a[i]:
##        print("Value equal to its index:",i)




##Alternate ellement in a ist
##List=[1,4,6,8,6,8]
##print(List[::2])



#PalinArray..

##S=int(input("Enter the number of value:"))
##Array=input("Enter the array:")
##reverse=Array[::-1]
##if Array==reverse:
##    print("1")
##else:
##    print("0")


##a=[]
##num=input("Enter the value:")
##for i in a:
##    if i<=num:
##        print(a)



##num=int(input("enter your array length: "))
####l=[0]*num
####for i in range(0,num):
####    l[i]=int(input("Enter the element: "))
####print(l)
##l=[int(input("Enter the element: ")) for i in range(0,num)]
##print(l)



##num=int(input("Enter your array length:"))
##l=[int(input("Enter the element:")) for i in range(0,num)]
##for i in range(len(l)):
##    print(l[i],end=" ")
##
##data=[
##        {
##            "name":"Yuvasri",
##            "Age":23,
##            "skill":"Dancing",
##            "Height":5.8,
##        },
##        {
##            "name":"Yuva",
##            "Age":16,
##            "skill":"Painting",
##            "Height":5.2,
##        }
##    ]
##list1=[]
##list2=[]
##for i in data:
##    if i["Age"]<18:
####        print(i["name"],"is not eligible for voting")
##        list1.append(i["name"])
##    else:
####        print(i["name"],"is eligible for voting")
##        list2.append(i["name"])
##print("is not eligible for voting",list1)
##print("is eligible for voting",list2)
##



##Swap the Kth element

##
##num=int(input("Enter the element:"))
##l=[int(input("Enter the element: ")) for i in range(0,num)]
##print(l)
##K=2
##if K>len(l)or K<1:
##    print("Invalid value of K")
##else:
##    a=l[K-1]
##    l[K-1]=l[-K]
##    l[-K]=a
##print(l)


##num=int(input("Enter a element:"))
##l=[int(input("Enter th element:"))for i in range(0,num)]
##print(l)
##k=3
##for i in range(


##num=input("Enter a Name:")
##a={}
##for i in num:
##    if i in a:
##        a[i]+=1
##    else:
##        a[i]=1
##print(a)
##d={'a','b','c'}
##d2={'d','e','f'}
##d3={**d,**d2}
##print(d3)

##dict1={'a':1,'b':2}
##dict2={'c':3,'d':4}
##dict3={'e':5,'f':6}
##new_dict={**dict1,**dict2,**dict3}
##print("concatenated dictionary",new_dict)

##Check whether the is exict or not
##my_dict={'a':1,'b':2,'c':3}
##print('b' in my_dict)
##print('c' in my_dict)

##n=int(input("Enter a number:"))
##if n<=0:
##    print("Give a positive integer:")
##else:
##    d={}
##    for i in range(1,n+1):
##        d[i]=i*i
##    print(d)



    
##Add a key
##d={'b':2,'c':4}
##print(d)
##d.update({'z':5})
##print(d)

##Dict between 1 and 15
##d={}
##for i in range(1,16):
##    d[i]=i*i
##print(d)


####Merge a dictionary
##dict1={'a':1,'b':2}
##dict2={'c':3,'d':4}
##dict3={'e':5,'f':6}
##new_dict={**dict1,**dict2,**dict3}
##print("Merge dict",new_dict)


##my_dict = {'a': 10, 'b': 20, 'c': 30}
##total_sum = sum(my_dict.values())
##print("Total sum of items in the dictionary:", total_sum)
##


##Neon number
##number = int(input("Enter a number: "))
##square = number * number
##d=0
##while square != 0:
##    digit = square % 10
##    d+= digit
##    square //= 10
##if d == number:
##    print(number, "is a neon number.")
##else:
##    print(number, "is not a neon number.")


##Anagram or not
##
##string1 = input("Enter the first string: ")
##string2 = input("Enter the second string:")
##
##
##if sorted(string1)==sorted(string2):
##    print("The strings are anagrams.")
##else:
##    print("The strings are not anagrams.")
##
##



##arr = [1, 2, 3, 4, 5]
##d = 2
##n = len(arr)
##rotated_arr = arr[d:] + arr[:d]
##print("Original array:", arr)
##print("Array rotated by", d, "elements:", rotated_arr)
##
##Array rotation
##arr = [1, 2, 3, 4, 5]
##d = 2
##n = len(arr)
##rotated_arr = arr[d:] + arr[:d]
##
##print("Original array:", arr)
##print("Array rotated by", d, "elements:", rotated_arr)




##my_dict = {'a': 10, 'b': 20, 'c': 30}
##result=1
##for i in my_dict.values():
##    result*=i
##print(result)



##Add a key
##d={'b':2,'c':4}
##print(d)
##d.remove({'z':5})
##print(d)
##





##s = input("Enter a string with brackets: ")
##
##count = 0
##for char in s:
##    if char == '(':
##        count += 1
##    elif char == ')':
##        count -= 1
##    if count < 0:
##        break
##
##balanced = count == 0
##print(balanced)


##numbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
##n = len(numbers) + 1
##print(n)
##a= n * (n + 1) // 2
##print(a)
##b = sum(numbers)
##print(b)
##c = a - b
##print("The missing number is:",c)


S1=[1,2,3]
carry=1
result=[]
for i in range(len(S1)-1,-1,-1):
    total=S1[i]+carry
    result.append(total%10)
    carry=total//10
result.reverse()
print("list",result)














