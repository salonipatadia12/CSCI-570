import sys

def readinput(file): #created a function for reading the inputs
    # file = sys.argv[1] #giving the input file as the second argument in the command line 
    f = open(file, "r")
    # f = open("input.txt", "r")
    string_list = []
    num1 = []
    num2 = []
    is_second = True
    for line in f.readlines():
        line = line.strip() #spliting based on spaces
        if not line.isnumeric(): #checking if the line has numbers or strings
            string_list.append(line) 
            if len(string_list) == 2: #since we have to compare only two strings, if the length of the string_list equals 2 if stop appending things in that as we know the rest our all numbers.
                is_second = False
        else:
            if is_second:
                num1.append(int(line)) #when the flag is True meaning we haven't encountered the second string. So we append all the numbbers from the first string till the second string
            else:
                num2.append(int(line)) #append the numbers from the second string till the last 
    f.close() #close the file
    return string_list, num1, num2 # we are returning the 2 strings which are appended one after the other and the respective numbers of the strings.

def String_generator():
    string_list, num1, num2 = readinput(file)
    result = []
    index = 0
    string = string_list[0] #takes the first string
    while index < len(num1):
        string = string[0:num1[index]+1] + string + string[num1[index]+1 :]
        index += 1
    result.append(string)
    
    index = 0
    string = string_list[1]
    while index < len(num2):
        string = string[0:num2[index]+1] + string + string[num2[index]+1 :]
        index += 1
    result.append(string)
        
    return result
  
def write_output():
    result = String_generator()
    ofile = file_name[2]
    f = open(ofile, 'wt')
    f.write('\n'.join(result))
    f.close()
    return result

# write_output()
if __name__ == "__main__":
  file_name = sys.argv
  file = file_name[1]
  output_file_path = file_name[2]
  # input_file_path = "../Project/SampleTestCases/input2.txt"
  # lines = open(input_file_path,'r').readlines()
  strings = readinput(file)
  c=write_output()
  # print(c)
