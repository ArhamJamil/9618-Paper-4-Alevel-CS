global Jobs
global NumberOfJobs

def Initialise():
    global Jobs
    global NumberOfJobs

    NumberOfJobs = 0

    Jobs = [[-1, -1] for _ in range(100)]


def AddJob(Jnum, Priority):
    global Jobs
    global NumberOfJobs

    if NumberOfJobs < 100:
        Jobs[NumberOfJobs] = [Jnum, Priority]
        NumberOfJobs += 1
        print("Added")
    else:
        print("Not Added")


Initialise()

AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


def InsertionSort():
    global NumberOfJobs
    global Jobs

    for count in range(1, NumberOfJobs):
        currentJobPriority = Jobs[count][1]
        currentJob = Jobs[count][0]
        index = count - 1

        while index >= 0 and currentJobPriority < Jobs[index][1]:
            Jobs[index + 1][1] = Jobs[index][1]
            Jobs[index + 1][0] = Jobs[index][0]
            index -= 1

        Jobs[index + 1][1] = currentJobPriority
        Jobs[index + 1][0] = currentJob


def PrintArray():
    global NumberOfJobs
    global Jobs

    for i in range(0, NumberOfJobs):
        print(Jobs[i][0], " priority ", Jobs[i][1])


InsertionSort()
PrintArray()

