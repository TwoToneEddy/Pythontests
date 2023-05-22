#!/home/lee/.platformio/penv/bin/python3
import calendar
import datetime
import matplotlib.pyplot as plt

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

balance = 238.86
balance = balance + 68
weeklyDeduction = 101.99
monthlyPay = 450
history = list()

today = datetime.date.today()
currentYear = int(today.strftime("%d/%m/%y").split('/')[2])
currentMonth = int(today.strftime("%d/%m/%y").split('/')[1])
currentDay = int(today.strftime("%d/%m/%y").split('/')[0])
#currentDay = 19
# Number of days in a month (october for example)
#print(calendar.monthrange(2020,10)[1])


friday = 4

days = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}



for year in [23,24]:
    if(currentYear < year):
        currentMonth=1
    for month in range(currentMonth,13):
        for day in range(1,calendar.monthrange(year,month)[1]+1):
            dayOfWeek=calendar.weekday(year,month,day)
            if(day == 18):
                if(month == currentMonth) and(year==currentYear) and (day < currentDay):
                    pass
                else:
                    balance = balance + monthlyPay
                    history.append(balance)
                    if( balance >= 100 and balance < 300):
                        print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.OKGREEN}+£{monthlyPay} \t {bcolors.OKBLUE}£{round(balance,2)}")
                    if( balance >= 300):
                        print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.OKGREEN}+£{monthlyPay} \t {bcolors.OKGREEN}£{round(balance,2)}")
                    if( balance >= 0 and balance < 100):
                        print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.OKGREEN}+£{monthlyPay} \t {bcolors.WARNING}£{round(balance,2)}")
                    if( balance < 0):
                        print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.OKGREEN}+£{monthlyPay} \t {bcolors.FAIL}£{round(balance,2)}")
                
            if(dayOfWeek == days.get("Fri") and (day > currentDay or month > currentMonth or year > currentYear) ):
                balance = balance-weeklyDeduction
                history.append(balance)
                if( balance >= 100 and balance < 300):
                    print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.FAIL}-£{weeklyDeduction} \t {bcolors.OKBLUE}£{round(balance,2)}")
                if( balance >= 300):
                    print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.FAIL}-£{weeklyDeduction} \t {bcolors.OKGREEN}£{round(balance,2)}")
                if( balance >= 0 and balance < 100):
                    print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.FAIL}-£{weeklyDeduction} \t {bcolors.WARNING}£{round(balance,2)}")
                if( balance < 0):
                    print(f"{bcolors.ENDC}{day}/{month}/20{year}:\t {bcolors.FAIL}-£{weeklyDeduction} \t {bcolors.FAIL}£{round(balance,2)}")

plt.plot(history,'--bo')
plt.axhline(y=0.0)
plt.ylabel('some numbers')
plt.show()
