# So I know the data comes in .csv format. I need a way to pull in the data into my program
# I can google csv python and there is a python library listed in the official documentation
# that tells me that it is tested and probably works the way it is documented. The documentation
# tells me that I can work use this library to work with csv files.
import csv

import datetime

# This is where I can use my list of things I need to keep track of and start to actually work
# I am creating a variable toy_orders that is an empty array. Now I need to pull in all the orders
# from the csv files that are provided.
toy_orders = []

# I know I need to open the csv file and read each row and add it to my array. I am using the
# Python keyword with which allows us to run try/finally over the rows of the file and ensure
# the file will close when we reach the end of the file. It will read all rows 1 through 
# 1,000,001 and let us do something with those rows and when it reaches a row with no input
# it will close the file for us.
# http://effbot.org/zone/python-with-statement.htm for my information on keyword with
# I am opening the file toys_rev2.csv 'as' variable csvfile. The second parameter is 'rb' which
# is allows us to read the file. Then I use use the reader method to create a reader object
# this allows me to iterate over the object and then add each toy that needs to be made
# to my empty array
with open('toys_rev2.csv', 'rb') as csvfile:
    toy_reader = csv.reader(csvfile)
    for row in toy_reader:
        toy_orders.append(row)

# I can check my own work too! Here I am just checking to ensure that my order array populated
# correctly. I test the first, second, and last items of my array and the length of the array. 
# You should see:
# print toy_orders[0] # ['ToyId', 'Arrival_time', 'Duration'] - heading
# print toy_orders[1] # ['1', '2014 1 1 0 1', '5'] - first toy that needs to be made
# print (toy_orders[-1]) # ['10000000', '2014 12 10 23 59', '697'] - last toy that needs to be made
# print len(toy_orders) # 1000001
# I am pretty comfortable that my array has all the toys that need to be in it now.
# Within this array I have taken care of a few things.
# I have all my Toy Orders, the amount of time to complete an order which can be pulled from the
# array by toy_order[1][2], this also acts as a queue because it looks like the toys are in the file
# in an order to be completed. This takes care of my first 3 variables.

# Here I am setting up an empty array that I can put my complete toys into.
completed_orders = []

# Now I wanted to get my individual laborers.
workers = []

# Here I am iterating over the range of numbers 1 to 901 so I can get 900 laborers
# Then I am adding them to my workers array as an array with the second element being
# their initial productivity and the last element being their next time free
for x in range(1, 901):
    workers.append([x, 1, 900])

# Here I am just printing out workers to make sure I created my workers list correctly.
# print workers

# My next step is to see if I can use these two data structures to actually make a toy.
# I create a function that takes two arguments, the toy to make, and the maker. I know
# these will come in as arrays. I also realize at this point that I need a very good way
# to handle time tracking
def make_toy(toy, worker, completed_toy):
    toy_to_make = toy.pop(1)
    print toy_to_make
    worker_to_make = worker.pop(0)
    print worker_to_make
    # is toy_to_make[1]
    time_to_make = int(toy_to_make[2])
    productivity = int(worker_to_make[1])
    actual_time = time_to_make / productivity
    return completed_toy.append([toy_to_make[0], worker_to_make[0], toy_to_make[1], actual_time])

    worker.append(worker_to_make)
##### So I have hit a road block here. I KNOW I need to implement a methodology for handling time
##### I also know I need to implement classes for Toys and Workers to make it easier to work with them
##### as objects.    

    # print actual_time

make_toy(toy_orders, workers, completed_orders)

# # make a function to check if availability
# def available(workers):
#     if len(workers) > 0:
#         return True
#     else:
#         return False

# if available(workers):
#     cur_worker = workers.pop(0)
# else:
#     pass

# current_toy = toy_array[1]
# print current_toy

# make_toy(current_toy, toy_array[0])