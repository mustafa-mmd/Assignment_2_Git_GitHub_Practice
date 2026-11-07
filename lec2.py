#file handling in python

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
    
#  with open("example.txt", "w") as file:
#     file.write("Hello, World!")
#     print("Content written to the file.")

# with open("example.txt", "a") as file:
#     file.write("\nThis is an additional line.")

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "r") as file:
#     lines = file.readlines()  

# with open("example.txt", "r") as file:
#     for line in file:
#         print(line)


# with open("example.txt", "r") as file:
#     content = file.readlines()
#     print(content)


#copy file content to another file
# import shutil

# shutil.copy("example.txt", "example_copy.txt")

#delete a file
# import os
# os.remove("example.txt")
#rename a file
# import os
# os.rename("example_copy.txt", "renamed_example.txt")



# oops object oriented programming
# class
# class Car:
#     model=2026 
#     color="red"
    
    
# #  object   
# car1=Car()
# print(car1.color)    


# class Person:
#     name="Mustafa Jamal"
#     age=21
    
# p1=Person()    
# print(p1.name)


# behind the seen init is called constructor whenever we create an object init is called automatically

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Mustafa Jamal", 21)
# print(p1.name)