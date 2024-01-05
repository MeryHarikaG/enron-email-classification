import os
import mailparser
import pandas as pd
import csv

csvFd = open('data.csv','w',newline='')
csvWriter = csv.writer(csvFd)
csvWriter.writerow(['From','To','Subject','Date','Message'])
persons = os.listdir('./enron/')
# list of all directories inside enron dataset print(persons)
count = 0
errorsCount = 0
filesList = []
for (root,dirs,files) in os.walk('./enron',topdown=True):
    for file in files:
        filesList.append(os.path.join(root,file))
        try:
            count = count +1
            mail = mailparser.parse_from_file(os.path.join(root,file))
            fromMailAddress = mail.from_[0][1]
            toMailAddresses = []
            for toMailAdd in mail.to:
                toMailAddresses.append(toMailAdd[1])
            message = mail.body
            date = mail.date
            subject = mail.subject
            print("writing to csv ",count) 
            csvWriter.writerow([fromMailAddress,toMailAddresses,subject,date,message])
        except:
            errorsCount = errorsCount+1
            print("error parsing email")

csvFd.close()
