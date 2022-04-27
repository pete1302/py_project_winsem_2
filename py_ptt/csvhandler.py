import csv
from datetime import datetime

listinp = []
listout = []
list1 = ["1", "2" , "3" , "4"]
listatt = [1  for x in range(len(list1))]
# listinp = list1 



with open('csv_1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

for i in data:
    print(i[0])

for i in data:
    listinp.append(i[0])

print(listinp)

def importcsv():
    return listinp

def exportcsv(csv):
    listout = csv
    print(listout)
    # chk(csv)
    absent = new(csv)
    writer(absent)
    return absent


def chk(csv):
    print("checker")
    print(listatt , csv)
    for i in listatt:
        if i in csv:
            print("checker")
            print(i)

def new(csv):
    absent = []
    for i  in range(len(csv)):
        if csv[i] == 1 :
            # print(i)
            print(listinp[i] , "absent")
            absent.append(listinp[i])

    return absent

def writer(absent):
    time = datetime.now().time()
    time = str(time)[:8]
    filepath = "csv-{}.csv".format(time)

    with open("csv_archive/{}".format(filepath), 'x') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(absent)




