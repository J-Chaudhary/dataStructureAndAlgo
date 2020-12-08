# __Author__: Student : Jignesh Chaudhary (id.197320)
# Assignemnt 4 (c) Schedule (Greedy)
class Schedule_greedy:
    '''the scheduling with deadlines algorithm to determine the schedule with maximum
    total profit. Only one job can be scheduled at a time, each job lasts one unit,
    and profit can only be obtained if the job is scheduled before or on deadline.'''
    def __init__(self, array):
        ''' It will only take array as a input which content [job order, dedline, profit]'''
        self.array = array

    def run(self):
        '''Run Greedy algorithm to get and print result'''
        max_deadline = 0
        for x in self.array: # loop to find maximum deadline
            if(max_deadline < x[1]):
                max_deadline = x[1]
        max_array = [] # define array to store job profit
        job_array = [] # define array to store job sequence
        for i in range(max_deadline+1): # using i as a index of array's object
            max_array.append(0) # append 0 in max_array which will replace with maximum profit
            job_array.append(0) # append 0 in job_array which will replace with feasible job number
            for x in self.array:
                if x[1] == i: # condition statement to get feasible job by checking deadline
                    if x[2] > max_array[i]: # find maximum profit job if array has more than 1 job with same deadline
                        job_array[i] = x[0] # job_array index [i] value will replace with job number
                        max_array[i] = x[2] # max_array index[i] value will replace with job profit

        print("Optimal feasible job sequence :", job_array[1:]) # print job_array
        totalprofit=0
        for i in max_array: # to add job profits to total profit
            totalprofit += i
        print("Total Profit :", totalprofit)

if __name__ == '__main__':
    job_dedline_profit= [[1, 2, 40],
                        [2, 4, 15],
                        [3, 2, 20],
                        [4, 3, 50],
                        [5, 1, 55],
                        [6, 2, 10],
                        [7, 1, 45]]
    print("======Assignment 4(c) Schedule (Greedy)")
    array = Schedule_greedy(job_dedline_profit)
    array.run()