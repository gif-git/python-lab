with open('file1.txt','w')as f: #Creating filel
    n=int(input('Enter the number of lines of data: '))
    for i in range(n):
        data=input('Enter the next line of data: ')
        f.write(data +'\n')
with open('file1.txt','r')as f: # Opening file1 in read mode
    with open('file2.txt','w')as s: #Opening file2 in write mode to copy filel
        for i in f:
            s.write(i)
            with open('file2.txt','r')as s:
                print('The content of file2 is:\n',s.read())
            with open('file1.txt','r')as f:
                d=f.read()
                i=d.split()
                count=0
                for i in l:
                    count=count+1
                    print('Number of words copied from filel to file2 is: ',count)
