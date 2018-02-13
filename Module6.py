# File descriptors

import sys

pathA= 'content/textfiles/parrot.txt'
pathB= 'content/textfiles/empty.txt'
pathC= 'content/textfiles/cheese.txt'

fileA= open(pathA, 'r')                # open file 1
fileB= open(pathB, 'r')                # open file 2

fd1= fileA.fileno()                    # get file descriptor 1
fd2= fileB.fileno()                    # get file descriptor 2

print ('File Descriptor A: '+str(fd1)) # print the fd number
print ('File Descriptor B: '+str(fd2)) # print the fd number

fileA.close()                          # close file 1, freeing fd1
print ('Closed FD A ['+str(fd1)+'].')

fileC= open(pathC, 'r')                # open file 3
fd3= fileC.fileno()                    # get file descriptor 3
print ('File Descriptor C: '+str(fd3)) # print the fd number

fileB.close()                          # close the file
fileC.close()                          # close the file


# Reading a text file
filepath= 'content/textfiles/parrot.txt'

# Open the file in filename for reading
file1= open(filepath, 'r')

# Read the entire file into the variable
data = file1.read()

# Print out the contents
print(data)


# Reading a text file
filepath= 'content/textfiles/parrot.txt'

# Open the file in filename for reading
file1= open(filepath, 'r')

# Read the entire file into the variable
data = file1.read()

# Print out the contents
print(data)


# Challenge: Reading a text file
# Load our command line arguments
import sys
P= sys.argv[1]
S= sys.argv[2]

# Your code goes here
file1= open(P, 'r').read()
#data = file1.read()

#count = data.count(S)

print(file1.count(S))

# Writing a text file
# set a variable to the path of the file
filepath= '/tmp/out.txt'

# something to write out
text= "A newt?"

# open our file for writing
file1= open(filepath, 'w')

# write 'text', to the file at ‘filepath’
file1.write(text)
file1.close()

# print out the contents of the file
file1= open(filepath, 'r')
print(file1.read())
file1.close()

# write something else out to the same file
file1= open(filepath, 'w')
file1.write('I got better.')
file1.close()

# print out the contents of the file again
file1= open(filepath, 'r')
print(file1.read())


# Challenge: Writing a text file

# Get the filepath from the command line
import sys
I= sys.argv[1] 
O= sys.argv[2] 
S= sys.argv[3]
T= sys.argv[4]

# Your code goes here
file1 = open(I, 'r')
data = file1.read()
newData = re.sub(S, T, data)
file2 = open(O, 'w')
file2.write(newData)
file1.close()
file2.close()


# Fixed length records
# sample data with records 6 characters long
data= '   100  1000     1999999   700'
print(data)

recordLength= 6
start= 0
records= []

# use the substring function to read all the records
while( (len(data) - start) >= recordLength):
  record= data[start:start + recordLength]
  records.append(record)
  start+= recordLength

# print out all of our records
for i in range(0,len(records)):
  print('Record '+ str(i) +': ('+records[i]+')')

'''
   100  1000     1999999   700
Record 0: (   100)
Record 1: (  1000)
Record 2: (     1)
Record 3: (999999)
Record 4: (   700)
'''


# The String.strip() Function
# It removes white space (gaps) from the beginning and end of a string.
text= '  Words   Other   Words\tTab   '
print(':' + text + ':')
text= text.strip()
print(':' + text + ':')
