from concurrent.futures import process
import sys
import time
import psutil
import os

#fucntion for minimum penalty call
def min_penalty(s1, s2, gap, mismatch):
    # initialize pointers
    i = 0
    j = 0
    # lengths of pattern
    m = len(s1)
    n = len(s2)
    # creating tables to store minimum cost of an alignment
    # opt[i,j]: the min cost between s1,s2...si and s1,s2...sj
    opt = [[None for j in range(n + 1)] for i in range(m + 1)]

    # initializing opt[i,0] and opt[0,j]
    for i in range(m + 1):
        opt[i][0] = i * gap
    for j in range(n + 1):
        opt[0][j] = j * gap

    # finding the minimum penalty: recurrence relations
    # skipping the first row which was initialized and starting from index 1
    i = 1
    while i <= m:
        j = 1  # skipping the first column (initialized) and start it from index 1
        while j <= n:
            # comparing the cost of 3 cases and find the minimum:
            # 1. add a mismatch cost
            # 2. add a gap to the second string
            # 3. add a gap to the first string
            opt[i][j] = min(
                opt[i - 1][j - 1] + mismatch[(s1[i - 1], s2[j - 1])],
                opt[i - 1][j] + gap,
                opt[i][j - 1] + gap)

            j += 1
        i += 1

    # Reconstructing the solution
    l = n + m  # maximum possible length of the optimal alignment
    i = m
    j = n

    s1pos = l
    s2pos = l

    # final two strings with gaps and mismatch
    s1_opt = [None for i in range(l + 1)]
    s2_opt = [None for j in range(l + 1)]

    # loop through until either the first pointer or the second pointer moves to the last element (the first element in the list)
    while not (i == 0 or j == 0):
        if (opt[i - 1][j - 1] + mismatch[(s1[i - 1], s2[j - 1])]) == opt[i][j]:
            s1_opt[s1pos] = ord(s1[i - 1])
            s2_opt[s2pos] = ord(s2[j - 1])
            s1pos -= 1
            s2pos -= 1
            i -= 1
            j -= 1
        # gap on the second string
        elif (opt[i - 1][j] + gap) == opt[i][j]:
            s1_opt[s1pos] = ord(s1[i - 1])
            # add gap symbol to the second string element
            s2_opt[s2pos] = ord('_')
            s1pos -= 1
            s2pos -= 1
            i -= 1
        # gap on the first string
        elif (opt[i][j - 1] + gap) == opt[i][j]:
            # add gap symbol to the first string element
            s1_opt[s1pos] = ord('_')
            s2_opt[s2pos] = ord(s2[j - 1])
            s1pos -= 1
            s2pos -= 1
            j -= 1

    while s1pos > 0:
        if i > 0:
            i -= 1
            s1_opt[s1pos] = ord(s1[i])
            s1pos -= 1
        else:
            s1_opt[s1pos] = ord('_')
            s1pos -= 1

    while s2pos > 0:
        if j > 0:
            j -= 1
            s2_opt[s2pos] = ord(s2[j])
            s2pos -= 1
        else:
            s2_opt[s2pos] = ord('_')
            s2pos -= 1

    # Since we have assumed the maximum optimal alignment to be n+m long,
    # we need to remove the extra gaps in the starting
    # idx represents the index from which the arrays
    # x_opt, y_opt are useful

    extra_spaces = 1
    i = l
    while i >= 1:
        if (chr(s2_opt[i]) == '_') and chr(s1_opt[i]) == '_':
            extra_spaces = i + 1
            break

        i -= 1

    # The final alignment after removing the extra gaps
    # X
    i = extra_spaces
    s1_seq = ""
    while i <= l:
        s1_seq += chr(s1_opt[i])
        i += 1

    # Y
    i = extra_spaces
    s2_seq = ""
    while i <= l:
        s2_seq += chr(s2_opt[i])
        i += 1

    return opt[m][n], s1_seq, s2_seq


def process_memory():
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss / 1024)
    return memory_consumed


def string_Generator(line):
    number = list()
    string = list()
    index = list()
    result = list()
    for i in range(len(line)):
        try:
            x = int(line[i].rstrip("\n"))
            number.append(x)
        except ValueError:
            index.append(i)
            x = line[i].rstrip("\n")
            string.append(x)
    number2 = list()
    number2.append(number[index[0]:index[1] - 1])
    number2.append(number[index[1] - 1:])

    x = string[0]
    for j in number2[0]:
        temp = x[0:j + 1] + x + x[j + 1:]
        x = temp
    result.append(x)

    x = string[1]
    for j in number2[1]:
        temp = x[0:j + 1] + x + x[j + 1:]
        x = temp
    result.append(x)

    return result

# Space efficient alignment, which caculates the length of the
# shortest path from (0,0) to (i,j) and only returns the optimal value.
def space_eff(s1, s2, gap, mismatch):
    m, n = len(s1), len(s2)
    T = [[None for j in range(2)] for i in range(m+1)]
    for i in range(m+1):
        T[i][0] = gap * i
    for j in range(1, n+1):
        T[0][1] = gap * j
        for i in range(1, m+1):
            T[i][1] = min(T[i][0] + gap,
                          T[i-1][1] + gap,
                          T[i-1][0] + mismatch[(s1[i-1],s2[j-1])])
        for i in range(m+1):
            T[i][0] = T[i][1]
    T = [t[1] for t in T]
    memory_eff.append(process_memory())

    return T

# Backward space efficient alignment, which caculates the length of the
# shortest path from (i,j) to (m,n) and only returns the optimal value.

def backspace_eff(s1, s2, gap, mismatch):
    m, n = len(s1), len(s2)
    S = [[None for i in range(2)] for j in range(m+1)]
    for i in range(m+1):
        S[i][0] = gap * i
    for j in range(1, n+1):
        S[0][1] = gap * j
        for i in range(1, m+1):
            S[i][1] = min(S[i][0] + gap,
                          S[i-1][1] + gap,
                          S[i-1][0] + mismatch[(s1[m-i],s2[n-j])])
        for i in range(m+1):
            S[i][0] = S[i][1]
    S = [s[1] for s in S]
    memory_eff.append(process_memory())
    return S

# divide and conquer algorithm
def dc(s1, s2, gap, mismatch):
    m, n = len(s1), len(s2)
    
    if m<=2 or n<=2:
        return min_penalty(s1, s2, gap, mismatch)
    
    else:
        s2left = s2[:n//2]
        s2right = s2[n//2:]
        F, B = space_eff(s1, s2left, gap, mismatch), backspace_eff(s1, s2right, gap, mismatch)
        #partition = [F[j] + B[m-j] for j in range(m+1)]
        #cut = partition.index(min(partition))
        cut = 0
        opt = F[0] + B[m]
        for i in range(1, m+1):
            if F[i] + B[m-i] < opt:
                opt = F[i] + B[m-i]
                cut = i
        callLeft = dc(s1[:cut], s2left, gap, mismatch)
        callRight = dc(s1[cut:], s2right, gap, mismatch)

        
        return callLeft[0]+callRight[0], callLeft[1]+callRight[1], callLeft[2]+callRight[2]


if __name__ == "__main__":
    # list that stores memory for each call on DC function
    memory_eff = list()

    start = time.time()
    # dictionary that stores all alpha values (mismatch costs)
    mismatch = {
        ('A', 'A'): 0,
        ('C', 'C'): 0,
        ('G', 'G'): 0,
        ('T', 'T'): 0,
        ('A', 'C'): 100,
        ('C', 'A'): 100,
        ('A', 'G'): 48,
        ('G', 'A'): 48,
        ('A', 'T'): 94,
        ('T', 'A'): 94,
        ('C', 'G'): 118,
        ('G', 'C'): 118,
        ('C', 'T'): 48,
        ('T', 'C'): 48,
        ('G', 'T'): 110,
        ('T', 'G'): 110
    }
    # delta (gap cost) value
    gap = 30

    # list that stores all system argument
    files_name = sys.argv
    input_file_path = files_name[1]
    output_file_path = files_name[2]
    # input_file_path = "../Project/SampleTestCases/input1.txt"
    # input_file_path = "../Project/datapoints/in4.txt"
    line = open(input_file_path, 'r').readlines()
    strings = string_Generator(line)

    s1 = strings[0]  # the first sequence
    s2 = strings[1]  # the second sequence

    # min_cost = space_efficient(x, y, gap, mismatch)
    # min_cost2 = backspace_efficient(x, y, gap, mismatch)

    # print(minimum_penalty(x, y, gap, mismatch))
    # p = []  # keep track of all the half point that the shortest path passes through
    min_cost, first_seq, second_seq = dc(s1, s2, gap, mismatch)
    # print(min_cost)
    # print(first_seq)
    # # print(second_seq)
    # time_eff = (time.time()-start)*1000
    # print((time.time()-start)*1000)
    # # print(str(process_memory()) + '\n')
    # print(str(max(mem_eff))+'\n')

    f = open(output_file_path, 'w')
    f.write(str(min_cost)+'\n')
    f.write(first_seq+'\n')
    f.write(second_seq+'\n')
    f.write(str((time.time()-start)*1000)+'\n')
    f.write(str(max(memory_eff)))
    f.close()