#petplan         27  -15.85
#sky             25  -25.91
#phone           24  -10
#KieraCarins     22  -24.88
#homeIns         20  -12.81
#car             18  -320
#carins          18  -33.28
#pete            18  -30
#washerDryer     18  -11.18
#lifeIns         18  -11.92
#pay             18  463.73
#gym             3   -83
#contacts        1   -11
#kiera           1   124.88


import calendar
import datetime
import matplotlib.pyplot as plt


petplan=-15.85
sky=-25.91
phone=-10
KieraCarins=-24.88
homeIns=-12.81
car=-320
carins=-33.28
pete=-30
washerDryer=-11.18
lifeIns=-11.92
pay=464.95
gym=-83
contacts=-11
kiera=124.88

# Frozen gym membership atm
pay = pay + gym

bills = {key: list() for key in range(0,32)}

bills[27].append(petplan)
bills[25].append(sky)
bills[24].append(phone)
bills[22].append(KieraCarins)
bills[20].append(homeIns)
bills[18].append(pay)
bills[18].append(car)
bills[18].append(carins)
bills[18].append(pete)
bills[18].append(washerDryer)
bills[18].append(lifeIns)
#bills[3].append(gym)
bills[1].append(contacts)
bills[1].append(kiera)



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

balance = 11.51
weeklyDeduction = 140
monthlyPay = 617.70
history = list()

today = datetime.date.today()
currentYear = int(today.strftime("%d/%m/%y").split('/')[2])
currentMonth = int(today.strftime("%d/%m/%y").split('/')[1])
currentDay = int(today.strftime("%d/%m/%y").split('/')[0])
#currentDay+=1
# Number of days in a month (october for example)
#print(calendar.monthrange(2020,10)[1])


friday = 4

days = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}

rowFormat = "{}"
rowFormat += "{:<20}{:<20}{:<20}"

for year in [21,22]:
    if(currentYear < year):
        currentMonth=1
    for month in range(currentMonth,13):
        for day in range(1,calendar.monthrange(year,month)[1]+1):
            dayOfWeek=calendar.weekday(year,month,day)
            if(day in bills.keys()):
                if(month == currentMonth) and(year==currentYear) and (day < currentDay):
                    pass
                else:
                    for bill in bills[day]:
                        if(bill > 0):
                            sign='+'
                            color = bcolors.OKGREEN
                        else:
                            sign = '-'
                            color = bcolors.FAIL

                        balance = balance + bill
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

plt.plot(history,'--bo')
plt.axhline(y=0.0)
plt.ylabel('some numbers')
plt.show()
