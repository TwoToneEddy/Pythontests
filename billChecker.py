import calendar
import datetime
import matplotlib.pyplot as plt

pay = 2903
yukiMeds=-12.5
water=-30
kieraLifeIns=-8.85
councilTax=-190
houseIns=-13.75
carInsCC=-48.56
gasElec=-110
leaf=-230.39
pete=-30
fromMum=6
leeLifeIns=-11.92
nespresso=-25
mortage=-1048
gym=-88
sofa=-16
amazonPrime=-8.99
leePhone=-6.99
petPlan=-11.87
vodafone=-21.5
kieraPhone=-5
youTube=-19.99

bills = {key: list() for key in range(0,32)}

bills[18].append(pay)
bills[18].append(yukiMeds)
bills[20].append(water)
bills[20].append(kieraLifeIns)
bills[20].append(councilTax)
bills[20].append(houseIns)
bills[22].append(carInsCC)
bills[24].append(gasElec)
bills[24].append(leaf)
bills[24].append(pete)
bills[24].append(fromMum)
bills[24].append(leeLifeIns)
bills[28].append(nespresso)
bills[1].append(mortage)
bills[3].append(gym)
bills[4].append(sofa)
bills[6].append(amazonPrime)
bills[9].append(leePhone)
bills[10].append(petPlan)
bills[11].append(vodafone)
bills[12].append(kieraPhone)
bills[15].append(youTube)

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
                        if(bill > 0):
                            sign='+'
                            color = bcolors.OKGREEN
                        else:
                            sign = '-'
                            color = bcolors.FAIL

                        balance = balance + bill
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
