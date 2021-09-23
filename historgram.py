print('Here is the histogram represented by @ as per the string present')
string=[5,9,3,20]
for i in range(len(string)):
    #number=int(string[i])
    output=''
    j=0
    while ( j < int(string[i])):
      #print(int(string[1]))
      output += '@'
      j = j + 1
    print(output) 