

import matplotlib.pyplot as plt

xOrigin = 5.76
yOrigin = 0

leftToMidX = 5.25
leftToMidY = -2.91

leftToRightX = 10.39
leftToRightY = 0.18

colDX = 17.38
rowDY = 7.44

transistorDX = 0
transistorDY = -5

#old:
#baseRDX = 4.826 - xOrigin
#baseRDY = -8

baseRDX = 7.030-5.67
baseRDY = -4

emRDX = 6.731 - xOrigin
emRDY = -8

xCoords = list()
yCoords = list()

xTicks = list()
yTicks = list()

ledComponentNo = 1
transComponentNo = 101
baseResComponentNo = 1
emResComponentNo = 201

lookup = {1:1,2:5,3:9,4:2,5:6,6:10,7:3,8:7,9:11,10:4,11:8,12:12,13:13,14:16,15:19,16:14,17:17,18:20,19:15,20:18,21:21,22:22,23:26,24:30,25:23,26:27,27:31,28:24,29:28,30:32,31:25,32:29,33:33,34:34,35:37,36:40,37:35,38:38,39:41,40:36,41:39,42:42,43:43,44:47,45:51,46:44,47:48,48:52,49:45,50:49,51:53,52:46,53:50,54:54,55:55,56:58,57:61,58:56,59:59,60:62,61:57,62:60,63:63,64:64,65:68,66:72,67:65,68:69,69:73,70:66,71:70,72:74,73:67,74:71,75:75}

globalComponentPrefix = "L"

output = """
var canvasConfig = api('editorCall', {cmd:'canvas_config'});


console.clear();
var s = api('getSource', {type: "json"});
var LEDs = [];
for (let x in s.FOOTPRINT){
	for(let i in s.FOOTPRINT[x].TEXT){
		var id = s.FOOTPRINT[x].TEXT;
		var name = s.FOOTPRINT[x].TEXT[i].text;
		if(name.slice(0,1)=="R"){
			LEDs.push([name,x]);
		}
	}
}

LEDs.forEach(myFunc);

function myFunc(value,index){
    if(value[0] == "R201"){
        api('moveObjsTo', {objs:[{gId:value[1]}], x:s.canvas.originX + api('valConvert', {type:'real2canvas',val:'6.731mm'}), y:s.canvas.originY+api('valConvert', {type:'real2canvas',val:'10.0mm'})});
    }
}
"""



def formatPrint(prefix,componentNo,x,y):
    y = y*-1
    print(f'if(value[0] == "{prefix}{lookup[componentNo]}"){{')
    print(f"\tapi('moveObjsTo', {{objs:[{{gId:value[1]}}], x:s.canvas.originX + api('valConvert', {{type:'real2canvas',val:'{x}mm'}}), y:s.canvas.originY+api('valConvert', {{type:'real2canvas',val:'{y}mm'}})}});")
    print("}")
    #print(f"{prefix}{componentNo}\n{x}\n{y*-1}")

def printCoords(x,y):
    global ledComponentNo
    global transComponentNo
    global baseResComponentNo
    global emResComponentNo
    #formatPrint("L",ledComponentNo,x,y)
    #formatPrint("Q",transComponentNo,x+transistorDX,y+transistorDY)
    formatPrint("R",baseResComponentNo,x+baseRDX,y+baseRDY)
    #formatPrint("R",baseResComponentNo,x,y+baseRDY)
    #formatPrint("R",emResComponentNo,x+emRDX,y+emRDY)

    """
    print(f"L{ledComponentNo} -> X:{x} Y:{y}")
    print(f"Q{transComponentNo} -> X:{x+transistorDX} Y:{y+transistorDY}")
    print(f"R{baseResComponentNo} -> X:{x+baseRDX} Y:{y+baseRDY}")
    print(f"R{emResComponentNo} -> X:{x+emRDX} Y:{y+emRDY}")
    """
    ledComponentNo+=1
    transComponentNo+=1
    baseResComponentNo+=1
    emResComponentNo+=1

def printCluster(col,row):
    global ledComponentNo
    ledLX = (col*colDX)+xOrigin
    ledLY = (row * -7.44)+yOrigin
    xCoords.append(ledLX)
    xTicks.append(ledLX)
    yCoords.append(ledLY)
    yTicks.append(ledLY)
    printCoords(ledLX,ledLY)

    ledMX = ledLX + leftToMidX
    ledMY = ledLY + leftToMidY
    xCoords.append(ledMX)
    yCoords.append(ledMY)
    printCoords(ledMX,ledMY)

    ledRX = ledLX + leftToRightX
    ledRY = ledLY + leftToRightY
    xCoords.append(ledRX)
    yCoords.append(ledRY)
    printCoords(ledRX,ledRY)


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
#plt.show()

