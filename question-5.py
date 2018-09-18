#Q.5- Write a Python program to write 10 random numbers into a file.
#Read the file and then sort the numbers and then store it to another file.

import random
file1=open('d.txt','w')
for i in range(1,11):
    file1.writelines(str(random.randrange(1,100))+'\n')
file1.close()
file1=open('d.txt','r')
file_content=file1.readlines()
file1.close()
file1=open('d.txt','w')
sorting=[]
for i in file_content:
    sorting.append(int(i.strip()))
sorting.sort()
sorting=[str(i) for i in sorting]
file1.writelines('\n'.join(sorting))
file1.close()
