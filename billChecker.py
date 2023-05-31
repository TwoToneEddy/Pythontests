import calendar
import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Indexed from 1, as seen on spreadsheet
# Starting cells
billsR = 14
billsC = 3
inR = 4
inC = 2
weeklyR = 14
weeklyC = 6


billsR = billsR - 2
billsC = billsC - 1

df = pd.read_excel('Money_baby_inter.xlsx')
print(df.iloc[billsR,billsC])

bills = {key: list() for key in range(0,32)}


for row in range(0,32):
    try:
        desc = df.iloc[row+billsR,1]
        amount = df.iloc[row+billsR,2]
        day = int(df.iloc[row+billsR,3])
        bills[day].append({"desc":desc,"amount":amount})
    except Exception as e:
        break



weeklyConsumables = -101
weeklyDisposable = -118
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

balance = 2895.78
history = list()

#today = datetime.date.today()
today = datetime.date(2023,5,19)
currentYear = int(today.strftime("%d/%m/%y").split('/')[2])
currentMonth = int(today.strftime("%d/%m/%y").split('/')[1])
currentDay = int(today.strftime("%d/%m/%y").split('/')[0])



friday = 4

days = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}

rowFormat = "{}"
rowFormat += "{:<20}{:<20}{:<20}"
lowBalance = balance
for year in [23,24]:
    if(currentYear < year):
        currentMonth=1
    for month in range(currentMonth,13):
        for day in range(1,calendar.monthrange(year,month)[1]+1):
            dayOfWeek=calendar.weekday(year,month,day)
            
            # Friday standing orders
            if(dayOfWeek == days.get("Fri") and (day > currentDay or month > currentMonth or year > currentYear) ):
                balance = balance + weeklyConsumables
                if balance < lowBalance:
                    lowBalance = balance
                if( balance >= 100 and balance < 300):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKBLUE}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyConsumables)}",f"{bcolors.OKBLUE}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance >= 300):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKGREEN}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyConsumables)}",f"{bcolors.OKGREEN}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance >= 0 and balance < 100):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.WARNING}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyConsumables)}",f"{bcolors.WARNING}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance < 0):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.FAIL}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyConsumables)}",f"{bcolors.FAIL}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))

                balance = balance + weeklyDisposable
                if balance < lowBalance:
                    lowBalance = balance
                if( balance >= 100 and balance < 300):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKBLUE}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyDisposable)}",f"{bcolors.OKBLUE}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance >= 300):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKGREEN}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyDisposable)}",f"{bcolors.OKGREEN}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance >= 0 and balance < 100):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.WARNING}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyDisposable)}",f"{bcolors.WARNING}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))
                if( balance < 0):
                    #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.FAIL}£{round(balance,2)}")
                    data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(weeklyDisposable)}",f"{bcolors.FAIL}£{round(balance,2)}"]
                    print(rowFormat.format("",*data))

            if(day in bills.keys()):
                if(month == currentMonth) and(year==currentYear) and (day < currentDay):
                    pass
                else:
                    for bill in bills[day]:
                        if(bill["amount"] > 0):
                            sign='+'
                            color = bcolors.OKGREEN
                        else:
                            sign = '-'
                            color = bcolors.FAIL

                        balance = balance + bill["amount"]
                        if balance < lowBalance:
                            lowBalance = balance
                        if( balance >= 100 and balance < 300):
                            #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKBLUE}£{round(balance,2)}")
                            data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(bill)}",f"{bcolors.OKBLUE}£{round(balance,2)}"]
                            print(rowFormat.format("",*data))
                        if( balance >= 300):
                            #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.OKGREEN}£{round(balance,2)}")
                            data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(bill)}",f"{bcolors.OKGREEN}£{round(balance,2)}"]
                            print(rowFormat.format("",*data))
                        if( balance >= 0 and balance < 100):
                            #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.WARNING}£{round(balance,2)}")
                            data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(bill)}",f"{bcolors.WARNING}£{round(balance,2)}"]
                            print(rowFormat.format("",*data))
                        if( balance < 0):
                            #print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {color}{sign}£{abs(bill)} \t\t {bcolors.FAIL}£{round(balance,2)}")
                            data=[f"{bcolors.ENDC}{day}/{month}/20{year}:",f"{color}{sign}£{abs(bill)}",f"{bcolors.FAIL}£{round(balance,2)}"]
                            print(rowFormat.format("",*data))
                    history.append(balance)

print(f"Lowest = {lowBalance}")
plt.plot(history,'--bo')
plt.axhline(y=0.0)
plt.ylabel('some numbers')
plt.show()
