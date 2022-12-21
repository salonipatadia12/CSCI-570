import sys
# import sys
from resource import *
import time
import psutil

def string_generator(line):
    n = list()
    s = list()
    ind = list()
    result = list()
    for i in range(len(line)):
        try:
            x = int(line[i].rstrip("\n"))
            n.append(x)
        except ValueError:
            ind.append(i)
            x = line[i].rstrip("\n")
            s.append(x)
    number2 = list()
    number2.append(n[ind[0]:ind[1] - 1])
    number2.append(n[ind[1] - 1:])

    x = s[0]
    for j in number2[0]:
        temp = x[0:j + 1] + x + x[j + 1:]
        x = temp
    result.append(x)

    x = s[1]
    for j in number2[1]:
        temp = x[0:j + 1] + x + x[j + 1:]
        x = temp
    result.append(x)

    return result
  # readinput(line)

  # def readinput(line): #created a function for reading the inputs
  #     # file = sys.argv[1] #giving the input file as the second argument in the command line 
  #     f = open(line, "r")
  #     # f = open("input.txt", "r")
  #     string_list = []
  #     num1 = []
  #     num2 = []
  #     is_second = True
  #     for line in f.readlines():
  #         line = line.strip() #spliting based on spaces
  #         if not line.isnumeric(): #checking if the line has numbers or strings
  #             string_list.append(line) 
  #             if len(string_list) == 2: #since we have to compare only two strings, if the length of the string_list equals 2 if stop appending things in that as we know the rest our all numbers.
  #                 is_second = False
  #         else:
  #             if is_second:
  #                 num1.append(int(line)) #when the flag is True meaning we haven't encountered the second string. So we append all the numbbers from the first string till the second string
  #             else:
  #                 num2.append(int(line)) #append the numbers from the second string till the last 
  #     f.close() #close the file
  #     return string_list, num1, num2 # we are returning the 2 strings which are appended one after the other and the respective numbers of the strings.

  # def String_generator():
  #     string_list, num1, num2 = readinput(file)
  #     result = []
  #     index = 0
  #     string = string_list[0] #takes the first string
  #     while index < len(num1):
  #         string = string[0:num1[index]+1] + string + string[num1[index]+1 :]
  #         index += 1
  #     result.append(string)
      
  #     index = 0
  #     string = string_list[1]
  #     while index < len(num2):
  #         string = string[0:num2[index]+1] + string + string[num2[index]+1 :]
  #         index += 1
  #     result.append(string)
          
  #     return result
    
  # def write_output():
  #     result = String_generator()
  #     ofile = file_name[2]
  #     f = open(ofile, 'wt')
  #     f.write('\n'.join(result))
  #     f.close()
  #     return result

  # write_output()
    # print(c)



def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed
  
# def time_wrapper():
#     start_time = time.time()
#     call_algorithm()
#     end_time = time.time()
#     time_taken = (end_time - start_time)*1000
#     return time_taken
def min_penalty(s1,s2,gap,mismatch):
  i=0 #pointers initialization
  j=0 #pointers initialization
  m=len(s1)
  n=len(s2)
  opt=[[None for j in range(len(s2)+1)]for i in range(len(s1)+1)]
  
  for i in range(m+1):
        opt[i][0] = i * gap
    # print("M row length: ",len(M))
  for j in range(n+1):
        opt[0][j] = j * gap
  i=1
  while i<=m:
    j=1
    while j<=n:
      opt[i][j]=min(mismatch[(s1[i-1],s2[j-1])] + opt[i-1][j-1] ,
                  gap + opt[i-1][j] , 
                  gap + opt[i][j-1])
      j+=1
    i+=1
  
  l=m+n
  i=m
  j=n
  s1p=l
  s2p=l
  s1f=[None for i in range(l+1)]
  s2f=[None for i in range(l+1)]
  
  while not (i==0 or j==0):
    if(opt[i-1][j-1]+mismatch[(s1[i-1],s2[j-1])])==opt[i][j]:
      s1f[s1p]=ord(s1[i-1])
      s2f[s2p]=ord(s2[j-1])
      s1p-=1
      s2p-=1
      i-=1
      j-=1
    elif (gap + opt[i-1][j])==opt[i][j]:
      s1f[s1p]=ord(s1[i-1])
      s2f[s2p]=ord('_')
      s1p-=1
      s2p-=1
      i-=1
    
    elif (gap + opt[i][j-1])==opt[i][j]:
      s1f[s1p]=ord('_')
      s2f[s2p]=ord(s2[j-1])
      s1p-=1
      s2p-=1
      j-=1
  
  while s1p>0:
    if i>0:
      i-=1
      s1f[s1p]=ord(s1[i])
      s1p -= 1
    else:
      s1f[s1p] = ord('_')
      s1p -= 1
  
  while s2p>0:
    if j>0:
      j-=1
      s2f[s2p]=ord(s2[j])
      s2p -= 1
    else:
      s2f[s2p] = ord('_')
      s2p -= 1  
  
  extra_spaces=1
  i=l
  while i >= 1:
      if (chr(s2f[i]) == '_') and chr(s1f[i]) == '_':
          extra_spaces = i + 1
          break
         
      i -= 1
    
  i = extra_spaces
  s1_sequence = ""
  while i <= l:
      s1_sequence += chr(s1f[i])
      i += 1
    
    # Y
  i = extra_spaces
  s2_sequence = ""
  while i <= l:
      s2_sequence += chr(s2f[i])
      i += 1
  memory=process_memory()
  return opt[m][n], s1_sequence, s2_sequence,memory
      
  
  
  
if __name__ == "__main__":
  start = time.time()
  mismatch = {
        ('A','A'):0,
        ('C','C'):0,
        ('G','G'):0,
        ('T','T'):0,
        ('A','C'):100,
        ('C','A'):100,
        ('A','G'):48,
        ('G','A'):48,
        ('A','T'):94,
        ('T','A'):94,
        ('C','G'):118,
        ('G','C'):118,
        ('C','T'):48,
        ('T','C'):48,
        ('G','T'):110,
        ('T','G'):110
    }
  gap=30
  # alpha[0][1] = alpha[1][0] = 110
  # alpha[0][2] = alpha[2][0] = 48 
  # alpha[0][3] = alpha[3][0] = 94        
  # alpha[1][2] = alpha[2][1] = 118            
  # alpha[1][3] = alpha[3][1] = 48        
  # alpha[2][3] = alpha[3][2] = 110
  file_name = sys.argv
  file = file_name[1]
  output_file_path = file_name[2]
    # input_file_path = "../Project/SampleTestCases/input2.txt"
    # lines = open(input_file_path,'r').readlines()
  line = open(file,'r').readlines()
  s = string_generator(line)
  # strings = readinput(file)
  # c=write_output()
  s1=s[0]
  s2=s[1]
  min_cost, first_seq, second_seq,mem = min_penalty(s1,s2,gap,mismatch)
  
  f = open(output_file_path, 'w')
  f.write(str(min_cost)+'\n')
  f.write(first_seq+'\n')    
  f.write(second_seq+'\n')
  f.write(str((time.time()-start)*1000)+'\n')
  f.write(str(mem)+'\n')


  f.close()
  
