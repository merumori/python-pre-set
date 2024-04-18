#1

# a = int(input("Enter number:-"))
# b = int(input("Enter number:-"))


# if a > b:
# 	print("A is bigger")
# else:
# 	print("B is bigger")

#2  

# a = int(input("Enter number:-"))

# if a % 5 == 0:
# 	print("Number divisible by 5")
# else:
# 	print("Number not divisible by 5")

#3

# a = int(input("Enter number:-"))

# if a >= 0 and a <= 100:
# 	print("Number is between 0 to 100")
# else:
# 	print("Number is not between 0 to 100")

#4

# a = int(input("Enter number:-"))
# length = len(str(a))
# print("Number Length is ", length)

# if length == 4:
# 	print("Number is 4 digit")
# else:
# 	print("Number is not 4 digit")

#5

# a = int(input("Enter number:-"))

# if a == 1:
# 	print("Monday")
# elif a == 2:
# 	print("Tuesday")
# elif a == 3:
# 	print("Wednesday")
# elif a == 4:
# 	print("Thursday")
# elif a == 5:
# 	print("Friday")
# elif a == 6:
# 	print("Saturday")
# elif a == 7:
# 	print("Sunday")
# else:
# 	print("Please enter valid number")


#6

# a = int(input("Enter number of opration:-"))

# if a <= 4:
# 	num1 = int(input("Enter number 1:-"))
# 	num2 = int(input("Enter number 2:-"))

# if a == 1:
# 	sum = num1+num2
# 	print("Addition is",sum)
# elif a == 2:
# 	sub = num1-num2
# 	print("Substraction is",sub)
# elif a == 3:
# 	mul = num1*num2
# 	print("Multiple is",mul)
# elif a == 4:
# 	div = num1/num2
# 	print("Division is",div)
# else:
# 	print("Enter valid number")

#7 

# string_name = input("Enter String:-")
# vowels = "aeiouAEIOU"

# vowelcount = sum(string_name.count(vowel) for vowel in vowels)
# length = len(string_name)
# concount = length - vowelcount

# print("Vowel count is:- ", vowelcount)
# print("Constraint count is:- ", concount)


#8

# num = int(input("Enter Number:- "))

# for i in range(1,11):
# 	print(num, "*", i, "=", (num*i))

# 9
# for i in range(1,11):
# 	print("Sq = ",i, i*i, "cube = ",i, i*i*i)

# 10

# a=input('enter your lowar case string :-')
# b=a.upper()
# print(b)


# 11

# for i in range(1,11):
#  	print(i)
# for i in range(10,0,-1):
# 	print(i)
# for i in range(1,11,2):
# 	print(i)
# for i in range(2,11,2):
# 	print(i)

# for i in range(1,1026):
# 	print(i*=2)


# 12

# p=1;
# for i in range(11):
#     print(p);
#     p=p*2;

# 13


# num = int(input("Enter Number:- "))

# for i in range(1,11):
#  	print(num, "*", i, "=", (num*i))

# 14 

no=input("enter the first number and spece and second number:-")

no_list=sum(int(num) for num in no)

print('sum of the number',no_list)

#15


# no=input("enter the first number and spece and second number:-")

# no_list=[int(num) for num in no.split()]
# c_of_num=len(no_list)
# print('count of the number',c_of_num)


# 16
# z=input("enter the number:-")
# c_z=str(z).count('0')
# print("number of zero in the input :",c_z)

# 17
# while True:
# 	num = int(input("Enter the number: "))
# 	if num % 2 == 0:
# 		print(f"{num} is an even number")
# 	else:
# 		print(f"{num} is an odd number")
# 		choice = input("Do you want to check another number? (Y/N): ")
# 		if choice.upper() != 'Y':
# 			break
