

import matplotlib.pyplot as plt

xOrigin = 5.76
yOrigin = 0

leftToMidX = 5.25
leftToMidY = -2.91

leftToRightX = 10.39
leftToRightY = 0.18

colDX = 17.38
rowDY = 7.44

xCoords = list()
yCoords = list()

xTicks = list()
yTicks = list()
def printCluster(col,row):
    ledLX = (col*colDX)+xOrigin
    ledLY = (row * -7.44)+yOrigin
    xCoords.append(ledLX)
    xTicks.append(ledLX)
    yCoords.append(ledLY)
    yTicks.append(ledLY)

    ledMX = ledLX + leftToMidX
    ledMY = ledLY + leftToMidY
    xCoords.append(ledMX)
    yCoords.append(ledMY)

    ledRX = ledLX + leftToRightX
    ledRY = ledLY + leftToRightY
    xCoords.append(ledRX)
    yCoords.append(ledRY)
    print(f"***** Col {col}, row {row} ******")
    print(f"{ledLX},{ledLY}")
    print(f"{ledMX},{ledMY}")
    print(f"{ledRX},{ledRY}")
    print(f"*********************************")
    print()


printCluster(0,0)
printCluster(0,2)
printCluster(0,4)
printCluster(0,6)

printCluster(1,1)
printCluster(1,3)
printCluster(1,5)

printCluster(2,0)
printCluster(2,2)
printCluster(2,4)
printCluster(2,6)

printCluster(3,1)
printCluster(3,3)
printCluster(3,5)

printCluster(4,0)
printCluster(4,2)
printCluster(4,4)
printCluster(4,6)

printCluster(5,1)
printCluster(5,3)
printCluster(5,5)

printCluster(6,0)
printCluster(6,2)
printCluster(6,4)
printCluster(6,6)
#plt.scatter(xCoords,yCoords)
#plt.xlim(-5,30)
#plt.ylim(-5,30)
#plt.gca().invert_yaxis()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_ticks_position('top')
ax.yaxis.grid(linestyle = '-', color = 'gray')
#ax.invert_yaxis()
ax.scatter(xCoords,yCoords)

#xticks = [5.76,23.14,40.52,57.9,75.28,92.66,110.04]
#yticks = [0,7.44,14.88]
ax.set_xticks(xTicks)
ax.set_yticks(yTicks)
plt.xlim(0,125)
plt.ylim(-60,1)
plt.show()

