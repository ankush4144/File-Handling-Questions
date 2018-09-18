#Q.4- Write a Python programto combine each line from first file with the
#corresponding line in second file.
file=open('a.txt','r')
file1=open('b.txt','r')
a=file.readlines()
b=file1.readlines()
file.close()
file1.close()
c=list(zip(a,b))
print(c)
file2=open('c.txt','w')
for i in c:
    for j in i:
        file2.write(j)

file2.close()
