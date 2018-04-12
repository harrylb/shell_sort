import random
from random import sample
import math
import time

def generate_random_numbers(n):
    random_number_list = random.sample(range(n), n) #Generates list of non repeating integers
    return random_number_list

def shellSort(num_list):
    gap = len(num_list) // 2 #Calculates the gap (i)
    while gap > 0: #Ensures the gap is above 0, otherwise program sort would fail
        for i in range(gap, len(num_list)):
            var = num_list[i] #Define var
            b = i #Set to new variable
            while b >= gap and num_list[b - gap] > var: #Identifies if integer needs to be moved
                num_list[b] = num_list[b - gap] #Sets intger to new location in list
                b -= gap #Decreases gap size
            num_list[b] = var #Resets for next loop
        gap //= 2 #Decreases gap and discards remainder
    return num_list #Sends back sorted list to main function

def main():
    filename = "shellsortresults.csv"
    outfile = open(filename, "w")
    for n in range(1,50002,500): #Size of data set
        random_number_list = generate_random_numbers(n) #Calls function that generates random integers
        t1 = time.time()
        shellSort(random_number_list) #Calls shell sort function
        t2 = time.time()
        print("Time for sorting",n,"Seconds: ",t2-t1,"nlog(n)^2: ",n*(math.log(n))**2) #Visual representation in runner
        outfile.write(str(n) + "," + str(t2-t1) + "," + str(n*(math.log(n))**2) + "\n") #Places data in specified file name
    outfile.close()
    print("shellsortresults.csv successfully written")
if __name__ == "__main__":
    main()
