#Q.3- Write a Python program to copy the contents of a file to another file
file_object=open('a.txt','r')
file_object1=open('b.txt','w')
z=file_object.readlines()
file_object.close()
file_object1.writelines(z)
file_object1.close()

