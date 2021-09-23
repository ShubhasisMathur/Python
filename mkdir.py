import os;
#directory=input('ENter the name of the directory where you want to create the file ')
directory='C:\\Shubhasis'
os.chdir(directory)
print(os.getcwd())
filename='Deleteit'
content='This is the content of my file'
fn = open(filename,'rt')
for line in fn.readlines():
    line=line[::-1]
    #print(line)
    fn = open(filename,'w')
    fn.write(line)
    fn.close()
#newcontent=content[::-1]
#print(newcontent)
#fn=open(filename,'wt')
#fn.write(content)
#fn.close()


         
