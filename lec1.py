# print("Hello, World! \n" *3)

# for i in range(10):
#     print("Hello, World!")
    # finding diameter of a circle formula d=2r
    
# radius = float(input("Enter the radius of the circle: "))
# diameter = 2 * radius
# print("The diameter of the circle is:", diameter)
# now we find the speed of a car formula speed = distance/time
# distance = float(input("Enter the distance traveled by the car (in kilometers): "))
# time = float(input("Enter the time taken by the car (in hours): "))
# speed = distance / time
# print("The speed of the car is:", speed, "km/h")
#take input from user and print the sum of two numbers
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# sum = num1 + num2
# print("The sum of the two numbers is:", sum)

# h1="hello"
# h2="world"
# print(h1+h2)


# val1=input("Enter first value")
# val2=input("Enter second value")
# comb=val1+val2
# print(comb)

# totalBill=float(input("Enter the total bill amount: "))
# totalPeople=int(input("Enter the number of people: "))
# billPerPerson = totalBill / totalPeople
# print("Each person should pay:", billPerPerson) 



# no1=int(input("Enter first number: "))
# no2=int(input("Enter second number: "))
# sum=no1*no2
# print("The sum of the two numbers is:", sum)


# #list this is mutable
# my_list = [1, 2, 3, 4, 5]
# print(my_list)

# # tuple this is not mutable
# my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

# #dictionary this mutable and unordered store data in key value pair
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print(my_dict)  


#set this is mutable and unordered but does not allow duplicate values
# my_set = {1, 2, 3, 4, 5}
# print(my_set)

#loop

# num=5
# while num<=10:
#     print("Hello, World!")
#     num+=1
# print("Loop ended")

# numb=5
# for i in range(numb):
#     print("Hello, World!")
 
# print("Loop ended")

# even_numbers =2
# while even_numbers<=20:
#     print(even_numbers)
#     even_numbers+=2


# even_numbers = 2
# while even_numbers <= 20:
#     if even_numbers % 2 == 0:
#         print(even_numbers)
#     even_numbers += 1
    
    
# n=int(input("Enter a number: "))
# sum=0
# while n>=1:
#     sum+=n
#    n-=1
# print("The sum is:", sum)


# n=1
# while n<=5:
#     print("*"*n)
#     n+=1
    
# n=1
# while n<=5:
#     print(n,"mustafa jamal")
#     n+=1


# n=1
# while n<=10:
#     print(n*2)
#     n+=1
    
# n=1
# multiplier=int(input("Enter a number to print its multiplication table: "))
# while n<=10:
#     print(multiplier,"*",n,"=",multiplier*n)
#     n+=1

# mylist=[1,2,3,4,5]
# for i in mylist:
#     print(i)

# for i in range(1,11,1):
#     print(i)


# for num in range(1, 11):
#     if num == 5:
#         break
#     print(num)


# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# import time
# count=int(input("Enter a number: "))
# print("Countdown start: ")

# for i in range(count, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Countdown finished!")


#expense tracker

# expenses = []
# print("Welcome to the Expense Tracker!")

# while True:
#     print("\n1. Add Expense")
#     print("2. View Expenses")
#     print("3. Calculate Total")
#     print("4. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         expense = float(input("Enter the expense amount: "))
#         expenses.append(expense)
#         print("Expense added successfully!")
#     elif choice == "2":
#         if expenses:
#             print("Total Expenses:")
#             for i, expense in enumerate(expenses, start=1):
#                 print(f"{i}. {expense}")
#         else:
#             print("No expenses to display.")
#     elif choice == "3":
#         total = sum(expenses)
#         print(f"Total expenses: {total}")
#     elif choice == "4":
#         print("Thank you for using the Expense Tracker!")
#         break
#     else:
#         print("Invalid choice. Please try again.")



# expeneseslist = []
# print("Welcome to the Expense Tracker!")
# while True:
#     print("\n1. Add Expense")
#     print("2. view All Expenses")
#     print("3. calculate Total")
#     print("4. Exit")
#     choice=input("Enter your choice: ")
#     if choice=="1":
#         expense=float(input("Enter the expense amount: "))
#         category=input("Enter the category of the expense: ")
#         date=input("Enter the date of the expense (YYYY-MM-DD): ")
#         lest=expeneseslist.append({"amount": expense, "category": category, "date": date})
#         print("Expense added successfully!")
#     elif choice=="2":
#         if expeneseslist:
#             print("All Expenses:")
#             for i,lest in enumerate(expeneseslist, start=1):
#                 print(f"{i}. Amount: {lest['amount']}, Category: {lest['category']}, Date: {lest['date']}")
        
#     elif choice=="3":
#         total=sum(expense["amount"] for expense in expeneseslist)
#         print(f"Total expenses: {total}")
#     elif choice=="4":
#         print("Thank you for using the Expense Tracker!")
#         break
#     else:
#         print("Invalid choice. Please try again.")


#functions
# def greet(name):
#     print("Hello, " + name + "! Welcome to the program.")

# greet("Alice")

# def add_numbers(num1, num2):
#     return num1 + num2 

# result = add_numbers(5, 10)
# print(result)

#take input from user and print the sum of two numbers using function
# def add_numbers(num1, num2):
#     return num1 + num2

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")

# def vowConsonantCount(user_input):
#     vowels="aeiouAEIOU"
#     consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     vowel_count=0   
#     consonant_count=0
#     for char in user_input:
#         if char in vowels:
#             vowel_count+=1
#         elif char in consonants:
#             consonant_count+=1
#     return vowel_count, consonant_count
# vowel_count, consonant_count=vowConsonantCount(input("Enter a string: "))
# print(f"Number of vowels: {vowel_count}")
# print(f"Number of consonants: {consonant_count}")


# # lets build Rules base AI chatbot using python
# import datetime
# import time

# presenthour = datetime.datetime.now().hour
# name=input("Enter your name: ")
# if presenthour < 12:
#     print("Good Morning!", name)

# elif presenthour < 18:
#     print("Good Afternoon!", name)
# else:
#     print("Good Evening!", name)

# print("Welcome to the Rule-Based AI Chatbot!")
# print("you can ask simple questions and I will try to answer them. Type 'exit' to end the conversation.")


# #Lets create a dictionary of predefined responses for the chatbot
# responses = {
#     "hello": "Hello! How can I assist you today?",
#     "hi": "Hi there! What can I do for you?",
#     "how are you": "I'm just a chatbot, but I'm here to help you!",
#     "what is your name": "I am a Rule-Based AI Chatbot.",
    
# }


# while True:
#     user_input = input("Ask me questions: ").lower()
#     if user_input == "exit":
#         print("Chatbot: Goodbye! Have a great day!")
#         break
#     elif user_input in responses:
#         print("Chatbot Response:", responses[user_input])
#     else:
#         print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")



#let use api key to build a chatbot using gemini api        

import os
from google import genai

# 1. Initialize the Gemini Client directly with your string key
client = genai.Client()

print("Welcome to the Gemini AI Chatbot!")
print("You can ask any question. Type 'exit' to end the conversation.\n")

# 2. Start a continuous chat session
chat = client.chats.create(model="gemini-2.5-flash")

while True:
    # Removed .lower() from here so your questions keep proper capitalization
    user_input = input("Ask questions: ")
    
    # Check if the user wants to leave (using .lower() safely here instead)
    if user_input.strip().lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
        
    if not user_input.strip():
        continue

    try:
        # 3. Send the message to Gemini and get a response
        response = chat.send_message(user_input)
        print(f"Chatbot: {response.text}\n")
        
    except Exception as e:
        print(f"Chatbot Error: Could not connect to Gemini. ({e})")
