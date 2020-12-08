# Student : Jignesh Chaudhary and Aliakber Yusufali
# Final Project for Data Structure and algoritm
# Car Service Centre Booking System

import linklist # Importing Linklist data sturcutre

bookings=linklist.LinkedList()#creating object to store booking
refs=linklist.LinkedList()#creating object to store reference Numbers

def getdate():# take user input and return date in int format
    b_date = str(input("Booking Date(dd-mm-yyyy):"))
    x=b_date.split("-")
    return x[2]+x[1]+x[0]

def gettime(): # take user input and return booking time in int
    a = str(input("Booking Time (HH:MM) :"))
    x=a.split(":")
    return x[0]+x[1]

def getservicetype():#take user input and return service type in int
    type = str(input("Service Type (1, 2 or 3):"))
    if 4 < int(type) < 1:
        print("Service Type Error....")
        getservicetype()
    return type

def add_booking():# To add new booking
    tmp = []
    b_date = getdate()
    name = str(input("Customer First and Last name Name:"))
    phone = int(input("Customer Contact Number:"))
    car = str(input("Car Make and Model:"))
    service = getservicetype()
    time_in = gettime()
    tmp.append(b_date + str(service) + time_in)
    tmp.append(b_date)
    tmp.append(time_in)
    tmp.append(name)
    tmp.append(phone)
    tmp.append(car)
    tmp.append("Service-"+str(service))
    tmp.append(tmp[-1][-1])
    bookings.add(tmp)
    refs.add(tmp[0])
    print("Your Booking Ref. No. is ",tmp[0])

def cancelbooking():
    booking = int(input("Enter ref no.:"))
    refs.remove(booking)

def is_available():# Return True if customer booked with user input ref no else false
    a = getdate()
    b = gettime()
    c = getservicetype()
    x = a+c+b
    refs.sort()
    if refs.find(x) == x :
        print("Slot is not available or busy...Try other little later or earlier..")
    else:
        print("Slot is available, You can book service....")
        x = int(input("Press: 1 If you wants to add booking"))
        if x == 1:
            add_booking()

def modify():# Delete old booking and add new booking if yuse would like to book
    booking = int(input("Enger ref no.:"))
    refs.remove(booking)
    print("Old booking deleted... you can add new booking now")
    print("Press : 1 to add new booking")
    com = int(input("Type : 1 to add new Booking"))

def searchbooking():#Search Booking and return true or false
    booking = int(input("Enger ref no.:"))
    print(refs.find(booking))

def partition(refs):  # method to devide list
    length = refs.get_size
    lower = []
    higher = []
    pivot = refs.index(refs[-1])
    for i in range(length - 1):  # loop to compare each element with pivot
        item = refs.index(i)
        if item < pivot:
            lower += [item]
        else:
            higher += [item]
    return lower, pivot, higher

def quicksort(refs):  # Quick sort devided lists and concatenate them
    length = refs.get_size
    if length <= 1:  # base case
        return list
    else:  # recursive case
        (lower, pivot, higher) = partition(list)
        sort_lower = quicksort(lower)
        sort_higher = quicksort(higher)
    return sort_lower + [pivot] + sort_higher

def binarySearch(x):
    global refs
    low = 0
    high = len(refs) - 1
    while low <= high:
        mid = (low + high) / 2
        if int(refs[int(mid)]) == int(x):
            return int(mid)
        if int(refs[int(mid)]) > int(x):
            high = int(mid) - 1
        else:
            low = int(mid) + 1
    return int(mid)

if __name__ == '__main__':
    a = [('2019010111000','20190101','1000','Mr. A','234534234','HONDA','Service-1','1'),
        ('2019010111030','20190101','1030','Mr. B','234543123','HONDA','Service-1','1'),
        ('2019010211100','20190102','1100','Mr. C','234552012','HONDA','Service-1','1'),
        ('2019010411130','20190104','1130','Mr. D','234560901','HONDA','Service-1','1'),
        ('2019010211200','20190102','1200','Mr. E','234569790','HONDA','Service-1','1'),
        ('2019010411230','20190104','1230','Mr. F','234578679','HONDA','Service-1','1'),
        ('2019010111300','20190101','1300','Mr. G','234587568','HONDA','Service-1','1'),
        ('2019010211330','20190102','1330','Mr. H','234596457','HONDA','Service-1','1'),
        ('2019010511400','20190105','1400','Mr. I','234605346','HONDA','Service-1','1'),
        ('2019010211430','20190102','1430','Mr. J','234614235','HONDA','Service-1','1'),
        ('2019010111500','20190101','1500','Mr. K','234623124','HONDA','Service-1','1'),
        ('2019010311530','20190103','1530','Mr. L','234632013','HONDA','Service-1','1'),
        ('2019010411600','20190104','1600','Mr. M','234640902','HONDA','Service-1','1'),
        ('2019010211630','20190102','1630','Mr. N','234649791','HONDA','Service-1','1'),
        ('2019010111700','20190101','1700','Mr. O','234658680','HONDA','Service-1','1'),
        ('2019010311730','20190103','1730','Mr. P','234667569','HONDA','Service-1','1'),
        ('2019010121000','20190101','1000','Mr. Q','234676458','HONDA','Service-2','2'),
        ('2019010221100','20190102','1100','Mr. R','234685347','HONDA','Service-2','2'),
        ('2019010121200','20190101','1200','Mr. S','234694236','HONDA','Service-2','2'),
        ('2019010321300','20190103','1300','Mr. T','234703125','HONDA','Service-2','2'),
        ('2019010121400','20190101','1400','Mr. U','234712014','HONDA','Service-2','2'),
        ('2019010321500','20190103','1500','Mr. V','234720903','HONDA','Service-2','2'),
        ('2019010121600','20190101','1600','Mr. W','234729792','HONDA','Service-2','2'),
        ('2019010121700','20190101','1700','Mr. X','234738681','HONDA','Service-2','2'),
        ('2019010531000','20190105','1000','Mr. Y','234747570','HONDA','Service-3','3'),
        ('2019010231200','20190102','1200','Mr. Z','234756459','HONDA','Service-3','3'),
        ('2019010331400','20190103','1400','Mr.AA','234765348','HONDA','Service-3','3')]

    for i in a:
        bookings.add(i)
        refs.add(i[1])
    print("Welcome to Service Centre")
    def mainmanu():
        print("We offer Oil Change         Service Cost : $ 50     Service Time : 30 min")
        print("We offer Basic Service      Service Cost : $ 100    Service Time : 60 min")
        print("We offer Full Service       Service Cost : $ 200    Service Time : 120 min")
        print("please read service manual for other details....")
        print("Type : 1 for Book Service")
        print("Type : 2 To check All the bookings ")
        print("Type : 3 for Check if Service center is available for service")
        print("Type : 4 To Check if refnumber is booked or not")
        print("Type : 5 To Cancel Booking")
    mainmanu()
    command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if command == 1:
        add_booking()
        command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if command == 2:
        bookings.print_list()
        command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if command == 3:
        is_available()
        command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if command == 4:
        searchbooking()
        command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if command == 5:
        cancelbooking()
        command = int(input("Please type your choice (1, 2, 3, 4 or 5): "))
    if 1 > command > 5:
        print("Sorry... You pressed the Wrong Command")
        mainmanu()
