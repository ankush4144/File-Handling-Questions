#Q.1- Write a Python program to read n lines of a file
file_object=open('a.txt','r')
num=int(input("Enter number of lines you want to read from file"))
z=file_object.readlines()[0:num]
print("Content of file: ")
for i in z:
    print(i)
