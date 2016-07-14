import csv
import numpy as np

test_file = open('./test.csv', 'rb') # open file
test_file_object = csv.reader(test_file) #decalre object
header = test_file_object.next()#get rit of header

prediction_file = open("genderbasedmodel.csv", "wb") #open new file to write to
prediction_file_object = csv.writer(prediction_file) # make an objetc for the file

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:       # For each row in test.csv
    if row[3] == 'female':         # is it a female, if yes then        
        prediction_file_object.writerow([row[0],'1'])    # predict 1
    else:                              # or else if male,       
        prediction_file_object.writerow([row[0],'0'])    # predict 0
test_file.close()
prediction_file.close()


