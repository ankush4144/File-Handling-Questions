#Q.2- Write a Python program to count the frequency of words in a file.
file_object=open('a.txt','r')
num=input("String to be counted in file")
z=file_object.read()
counter=z.count(num)
print("Frequency of %s is %d" %(num,counter))
