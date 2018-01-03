process_queue = []
total_waitingtime = 0
n = int(input('Enter the total no of processes: '))
for i in  range(n):
    process_queue.append([])
    process_queue[i].append(input('Enter process name: '))
    process_queue[i].append(int(input('Enter process arrival: ')))
    total_waitingtime += process_queue[i][1]
    process_queue[i].append(int(input('Enter process burst: ')))
process_queue.sort(key = lambda process_queue:process_queue[1])
print ("ProcessName\tArrivalTime\tBurstTime")
for i in range(n):
    print (process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2])
print ("Total waiting time: ",total_waitingtime)
print ("Average waiting time: ",(total_waitingtime/n))



