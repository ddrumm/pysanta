import csv

toy_array = []

# opens the toy data and creates a multidimenional that has [toyID, date, time to complete]


with open('toys_rev2.csv', 'rb') as csvfile:
    toy_reader = csv.reader(csvfile)
    for row in toy_reader:
        toy_array.append(row)


# print toy_array

print type(toy_array[0][2])
int(toy_array[0][2])
# create a multidimentional array that hads [workerID, productivity]
workers = []

for x in range(1, 901):
    workers.append([x, 1])

# make a function to check if availability
def available(workers):
    if len(workers) > 0:
        return True
    else:
        return False

if available(workers):
    cur_worker = workers.pop(0)
else:
    pass

current_toy = toy_array[1]
# print current_toy

# def make_toy(toy, maker):
#     time_to_make = int(toy[2])
#     productivity = int(maker[1])
#     actual_time = time_to_make / productivity
#     print actual_time

# make_toy(current_toy, toy_array[0])