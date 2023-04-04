import tkinter as tk
import datetime
import random as r

#   1. create window
#   2. giving window a title
#   3. setting the dimensions
window = tk.Tk()
window.title("Smart Electricity Application")
window.geometry("1200x800")


#   setting varibals to something to create them
canPause = "False"
canPauseCheck = False
namedevice = ""
devices = 0
setTime = 0
setEndTime = 0
setUsage = 0
fullTime = datetime.datetime.now()
currentTime = int(fullTime.strftime("1%d%H%M"))
usage = []
combinations = []
text = ""
overflow = 0
overflowLOCK = 0
updateTickTime = 1000
removeList = []
factorUsageRange = 0
get_bin = lambda x: format(x, 'b')
currentDevicesOn = False
AmpereOverflow = 0
VoltOverflow = 0
solarPanels = 6
savedDevices = []


textFileAllDevices = open("testTXT", "r")
with open('testTXT') as f:
    for line in f:
        device = line.split('|')
        if int(device[3]) != 0 and int(device[2]) > currentTime:
           savedDevices.append([int(device[0]), False, True if device[1] == 'True' else False, int(device[2]), int(device[3]), device[4]])
allDevices = savedDevices


#   def when u press the button add device
def AddingDevice():
    #   deletes/forgets the button/label/textbox and sets height and width
    buttonAddDevice.place_forget()
    buttonRunningDevices.place_forget()

    #   creates/places button/label/textbox
    buttonGoBack.place(x=30, y=30, height=100, width=300)

    buttonIncreaseTime.place(x=350, y=300, height=75, width=75)
    buttonDecreaseTime.place(x=30, y=300, height=75, width=75)

    buttonIncreaseEndTime.place(x=350, y=550, height=75, width=75)
    buttonDecreaseEndTime.place(x=30, y=550, height=75, width=75)

    buttonIncreaseUsage.place(x=800, y=300, height=75, width=75)
    buttonDecreaseUsage.place(x=480, y=300, height=75, width=75)

    buttonCanPause.place(x=250, y=400, height=100, width=200)

    labelWordUsage.place(x=650, y=300, height=75, width=150)
    labelSetAmountUsage.place(x=575, y=300, height=75, width=75)

    labelWordHours.place(x=200, y=300, height=75, width=150)
    labelWordHours2.place(x=200, y=550, height=75, width=150)
    labelSetAmountTime.place(x=125, y=300, height=75, width=75)

    labelCanPause.place(x=30, y=400, height=100, width=200)

    labelWordName.place(x=30, y=162.5, height=75, width=300)
    textboxSetNameDevice.place(x=350, y=187.5, height=50, width=500)

    buttonSetDevice.place(x=800, y=500, height=100, width= 300)


# defines when u press the back button
def GoBack():
    #   makes it so everywhere you can use this variable
    global currentDevicesOn
    #   makes variable false
    currentDevicesOn = False
    #   places/creates button/label/textbox
    buttonAddDevice.place(x=30, y=30, height=100, width=300)
    buttonRunningDevices.place(x=30, y=160, height=100, width=300)
    #   deletes/forgets the button/label/textbox
    buttonGoBack.place_forget()
    buttonIncreaseTime.place_forget()
    buttonDecreaseTime.place_forget()
    buttonIncreaseEndTime.place_forget()
    buttonDecreaseEndTime.place_forget()
    labelSetAmountTime.place_forget()
    labelSetAmountEndTime.place_forget()
    labelWordHours.place_forget()
    labelWordHours2.place_forget()
    buttonIncreaseUsage.place_forget()
    buttonDecreaseUsage.place_forget()
    labelSetAmountUsage.place_forget()
    labelWordUsage.place_forget()
    labelWordName.place_forget()
    textboxSetNameDevice.place_forget()
    buttonSetDevice.place_forget()
    buttonCanPause.place_forget()
    labelCanPause.place_forget()
    testTextBox.place_forget()

def increaseTime():
    #   makes it so everywhere you can use this variable
    global setTime
    global labelSetAmountTime
    #   ups setTime with 1
    setTime += 1
    #   replaces label
    labelSetAmountTime.place_forget()
    labelSetAmountTime = tk.Label(text=setTime, font=("aharoni", 30))
    labelSetAmountTime.place(x=125, y=300, height=75, width=75)


def decreaseTime():
    #   makes it so everywhere you can use this variable
    global setTime
    global labelSetAmountTime
    #   checks if setTime is bigger than 0
    if setTime > 0:
        #   changes setTime with -1
        setTime -= 1
        #   replaces label
        labelSetAmountTime.place_forget()
        labelSetAmountTime = tk.Label(text=setTime, font=("aharoni", 30))
        labelSetAmountTime.place(x=125, y=300, height=75, width=75)


def increaseEndTime():
    #   makes it so everywhere you can use this variable
    global setEndTime
    global labelSetAmountEndTime
    #   ups setEndTime with 1
    setEndTime += 1
    #   replaces label
    labelSetAmountEndTime.place_forget()
    labelSetAmountEndTime = tk.Label(text=setEndTime, font=("aharoni", 30))
    labelSetAmountEndTime.place(x=125, y=550, height=75, width=75)


def decreaseEndTime():
    #   makes it so everywhere you can use this variable
    global setEndTime
    global labelSetAmountEndTime
    #   checks if setEndTime is bigger than 0
    if setEndTime > 0:
        #   changes setEndTime with -1
        setEndTime -= 1
        #   replaces label
        labelSetAmountEndTime.place_forget()
        labelSetAmountEndTime = tk.Label(text=setEndTime, font=("aharoni", 30))
        labelSetAmountEndTime.place(x=125, y=550, height=75, width=75)


def increaseUsage():
    #   makes it so everywhere you can use this variable
    global setUsage
    global labelSetAmountUsage
    #   increases setUsage with 10
    setUsage += 10 if setUsage < 300 else 100
    #   replaces label
    labelSetAmountUsage.place_forget()
    labelSetAmountUsage = tk.Label(text=setUsage, font=("aharoni", 30))
    labelSetAmountUsage.place(x=575, y=300, height=75, width=100)


def decreaseUsage():
    #   makes it so everywhere you can use this variable
    global setUsage
    global labelSetAmountUsage
    #   checks if setUsage is bigger than 0
    if setUsage > 0:
        #   increases setUsage with -10
        setUsage -= 10 if setUsage <= 300 else 100
        #   replaces label
        labelSetAmountUsage.place_forget()
        labelSetAmountUsage = tk.Label(text=setUsage, font=("aharoni", 30))
        labelSetAmountUsage.place(x=575, y=300, height=75, width=100)


def setDevice():
    #   makes it so everywhere you can use this variable
    global textFileAllDevices
    global devices
    global setTime
    global setUsage
    global labelSetAmountTime
    global labelSetAmountUsage
    global textboxSetNameDevice
    global setEndTime

    #   gets text from textbox and saves it in variable
    nameDevice = textboxSetNameDevice.get("1.0", "end-1c")

    #   if variable nameDevice isn't empty
    if nameDevice != "":
        #   gets current time
        currentTime = int(fullTime.strftime("1%d%H%M"))
        #   makes setTime usable for calculation
        setTime = setTime * 100
        setEndTime += int(str(currentTime)[1] + str(currentTime)[2]) * 10000

        #   allDevices info
        #   0 = electric power per tick
        #   1 = on/off True/False
        #   2 = device can pause True/False
        #   3 = end time 1ddhhmm
        #   4 = needed time ddhhmm
        #   5 = device name str
        allDevices.append([setUsage, False, canPauseCheck, setEndTime * 100 + 1000000, setTime, nameDevice])
        textboxSetNameDevice.delete(1.0,tk.END)

        textFileAllDevices = open("testTXT", "a")
        textFileAllDevices.write(str(setUsage) + "|" + str(canPauseCheck) + "|" + str(setEndTime) + "|" + str(setTime) + "|" + str(nameDevice) + "|" + "\n")
        textFileAllDevices.close()

        #   Sets the variables to 0
        setTime = 0
        setUsage = 0
        #   replaces label
        labelSetAmountTime.place_forget()
        labelSetAmountTime = tk.Label(text=setTime, font=("aharoni", 30))
        labelSetAmountTime.place(x=125, y=300, height=75, width=75)
        #   replaces label
        labelSetAmountUsage.place_forget()
        labelSetAmountUsage = tk.Label(text=setUsage, font=("aharoni", 30))
        labelSetAmountUsage.place(x=575, y=300, height=75, width=75)



def canPause():
    #   makes it so everywhere you can use this variable
    global canPause
    global canPauseCheck
    global buttonCanPause
    #   if its false
    if canPauseCheck == False:
        #   replaces false button with true button
        buttonCanPause.place_forget()
        buttonCanPause = tk.Button(window, text="True", font=("aharoni", 30), command=lambda: canPause())
        buttonCanPause.place(x=250, y=400, height=100, width=200)
        canPauseCheck = True
    #   if its true
    elif canPauseCheck == True:
        #   replaces false button with false button
        buttonCanPause.place_forget()
        buttonCanPause = tk.Button(window, text="False", font=("aharoni", 30), command=lambda: canPause())
        buttonCanPause.place(x=250, y=400, height=100, width=200)
        canPauseCheck = False


def currentDevices():
    #   makes it so everywhere you can use this variable
    global allDevices
    global text
    global testTextBox
    global timeNeeded
    global currentDevicesOn

    currentDevicesOn = True
    #   deletes addDevices and runningDevices
    buttonAddDevice.place_forget()
    buttonRunningDevices.place_forget()
    #   places back button
    buttonGoBack.place(x=30,y=30, height=100, width=300)
    timeList = []
    #   list with times
    for i in range(len(allDevices)):
        timeNeeded = allDevices[i][4] + 1000000
        timeList.append([list(int(x) for x in str(allDevices[i][3])), list(int(x) for x in str(timeNeeded))])
    text = str("\n".join(f"{allDevices[i][5]} {'on' if allDevices[i][1] else 'off'}\n{timeList[i][0][1]}{timeList[i][0][2]}:{timeList[i][0][3]}{timeList[i][0][4]}:{timeList[i][0][5]}{timeList[i][0][6]}\n{timeList[i][1][1]}{timeList[i][1][2]}:{timeList[i][1][3]}{timeList[i][1][4]}:{timeList[i][1][5]}{timeList[i][1][6]}" for i in range(len(allDevices))))
    testTextBox = tk.Label(window, text=text, font=("aharoni", 30))

    testTextBox.place(x=30, y=150, height=(200 * len(allDevices)), width=300)


def useOverflow():
    #   makes it so everywhere you can use this variable
    global usage
    global combinations
    global overflow
    global currentTime
    global priorityCalculation
    global factorUsageRange
    global optimalCombination
    global removeList
    overflow = r.randint(0, 100)
    #   making list for calculating combination
    #   usage
    #   0 = device index
    #   1 = device electric usage
    #   2 = can pause (1 = true/ 0 = false)
    #   3 = priority
    combinations.clear()
    usage.clear()
    removeList.clear()


    for i in range(len(allDevices)):
        if not allDevices[i][2] and not allDevices[i][1]:
            if (allDevices[i][3] - allDevices[i][4]) - currentTime < updateTickTime:
                allDevices[i][1] = True
                overflow -= allDevices[i][0]
            else:
                usage.append([i, allDevices[i][0], 0, (((currentTime - 1000000) - ((allDevices[i][3] - 1000000) - allDevices[i][4])) / allDevices[i][4])])
        elif allDevices[i][2]:
            if (((allDevices[i][3] - 1000000) - allDevices[i][4] + (allDevices[i][4] - 1000000)) - (currentTime - 1000000))  < updateTickTime:
                allDevices[i][1] = True
                overflow -= allDevices[i][0]
            else:
                usage.append([i, allDevices[i][0], 1, ((((allDevices[i][3] - 1000000) - allDevices[i][4] - (allDevices[i][4] - 1000000)) - (currentTime - 1000000)) / allDevices[i][4])])
        else:
            if allDevices[i][1]:
                overflow -= allDevices[i][0]

    for i in range(2 ** len(usage)):
        on_off = [int(x) for x in str(get_bin(i))]
        on_off.reverse()
        for _ in range(len(usage) - len(on_off)):
            on_off.append(0)
        on_off.reverse()
        use = sum(usage[i][1] if on_off[i] == 1 else 0 for i in range(len(usage)))
        priorityCalculation = sum(usage[i][3] if on_off[i] == 1 else (0 - usage[i][3]) for i in range(len(usage)))
        combinations.append([use, on_off, priorityCalculation])

    for i in range(len(combinations)):
        if (overflow - factorUsageRange) < combinations[i][0] < (overflow + factorUsageRange):
            if combinations[i][0] > overflow:
                combinations[i][2] = combinations[i][2] / (combinations[i][0] - overflow)
            elif combinations[i][0] < overflow:
                combinations[i][2] = combinations[i][2] / (overflow - combinations[i][0])
        else:
            removeList.append(i)

    if len(combinations) != len(removeList):
        removeList.reverse()
        for i in range(len(removeList)):
            combinations.pop(removeList[i])
        combinations.sort(key=lambda x: x[2])
    else:
        combinations.sort(key=lambda x: x[0])
    optimalCombination = min(combinations, key=lambda x: abs(x[0] - overflow))
    for i in range(len(usage)):
        allDevices[i][1] = True if optimalCombination[1][i] == 1 else False

    removeList.clear()


def mainLoop():
    #   makes it so everywhere you can use this variable
    global overflow
    global allDevices
    global removeList
    global overflowLOCK
    global labelOverflow
    global fullTime
    global currentTime
    removeList.clear()
    overflow = measureOverflow()
    useOverflow()
    overflowLOCK = overflow
    fullTime = datetime.datetime.now()
    currentTime = int(fullTime.strftime("1%d%H%M"))

    labelOverflow.place_forget()
    labelOverflow = tk.Label(text=f"Overflow:   {overflowLOCK.__round__(5)} Wh", font=("aharoni", 30))
    labelOverflow.place(x=400, y=35, height=75, width=500)

    #   Update used time
    for i in range(len(allDevices)):
        if allDevices[i][1]:
            time = "11111" + str(allDevices[i][4])
            if time[-1] == time[-2] == "0":
                allDevices[i][4] -= 41
                if time[-3] == time[-4] == "0":
                    allDevices[i][4] -= 4100
            else:
                allDevices[i][4] -= 1

            if allDevices[i][4] == 0:
                removeList.append(i)

    #   Remove Devices that are done
    for i in range(len(removeList) - 1, -1, -1):
        allDevices.pop(removeList[i])

    if currentDevicesOn:
        GoBack()
        currentDevices()
    window.after(updateTickTime, mainLoop)



def measureOverflow():
    #   the amount of Watts provided by the solar-panels etc.
    #   this will be replaced with hardware
    return r.random() * solarPanels

#   defines and places button/label/textbox
buttonAddDevice = tk.Button(window, text="Add Device", font=("aharoni", 30), command=lambda: AddingDevice())
buttonAddDevice.place(x=30, y=30, height=100, width=300)

buttonRunningDevices = tk.Button(window, text="Running Devices", font=("aharoni", 30), command=lambda: currentDevices())
buttonRunningDevices.place(x=30, y=160, height=100, width=300)

#   defines button/label/textbox
buttonGoBack = tk.Button(window, text="Back", font=("aharoni", 30), command=lambda: GoBack())

buttonIncreaseTime = tk.Button(window, text="+", font=("aharoni", 30), command=lambda: increaseTime())
buttonDecreaseTime = tk.Button(window, text="-", font=("aharoni", 30), command=lambda: decreaseTime())

buttonIncreaseEndTime = tk.Button(window, text="+", font=("aharoni", 30), command=lambda: increaseEndTime())
buttonDecreaseEndTime = tk.Button(window, text="-", font=("aharoni", 30), command=lambda: decreaseEndTime())

buttonIncreaseUsage = tk.Button(window, text="+", font=("aharoni", 30), command=lambda: increaseUsage())
buttonDecreaseUsage = tk.Button(window, text="-", font=("aharoni", 30), command=lambda: decreaseUsage())

buttonSetDevice = tk.Button(window, text="Set", font=("aharoni", 30), command=lambda: setDevice())

buttonCanPause = tk.Button(window, text="False", font=("aharoni", 30), command=lambda: canPause())

labelCanPause = tk.Label(window, text="Can Pause:", font=("aharoni", 30))

labelWordHours = tk.Label(text="Hour(s)", font=("aharoni", 30))
labelWordHours2 = tk.Label(text="Hour(s)", font=("aharoni", 30))
labelSetAmountTime = tk.Label(text=setTime, font=("aharoni", 30))
labelSetAmountEndTime = tk.Label(text=setEndTime, font=("aharoni", 30))
labelWordUsage = tk.Label(text="W", font=("aharoni", 30))
labelSetAmountUsage = tk.Label(text=setUsage, font=("aharoni", 30))
labelWordName = tk.Label(text="Name Device:", font=("aharoni", 30))

labelOverflow = tk.Label(text=f"Overflow:   {overflowLOCK} Wh", font=("aharoni", 30))

textboxSetNameDevice = tk.Text(window, font=("aharoni", 30))

testLabel = tk.Label()

testTextBox = tk.Label(window, text=text, font = ("aharoni", 30))

#   makes update loop
window.after(updateTickTime, mainLoop)


#   opens the window with the application
window.mainloop()
