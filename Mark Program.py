totalMarkWeight = 0
totalRawMark = 0
totalMark = 0
while(True):
    print("type add to add a mark, current to see you're current mark and future to see what mark you need to get your ideal mark")
    command = str(input())
    if(command == "add"):
        print("type in your mark (without the % sign)")
        addMark = int(input())
        print("On a scale of 1 - 5 how much does this mark weigh (if you don't know type 3)")
        addMarkWeight = int(input())
        totalRawMark += addMark*addMarkWeight
        totalMarkWeight += addMarkWeight
        totalMark = totalRawMark/totalMarkWeight
    if(command == "current"):
        print("Your current mark is", totalMark)
    if(command == "future"):
         print("What mark do you want to get after the next assigment")
         goal = int(input())
         print("What is the weight of the next assigment")
         NextWeight = int(input())
         futureWeight = totalMarkWeight + NextWeight
         goalMark = goal*futureWeight - totalRawMark
         goalMark = goalMark/NextWeight
         print("You need a ", goalMark, "to meet you're goal")
