print("==========================")
print("     GRATITUDE JOURNAL    ")
print("==========================")

running=True
while running:
    print("1. Add Gratitude")
    print("2. View Entries")
    print("3. Exit")
    option=int(input("Choose: "))
    if option==1:
        gratitude=[]
        for i in range (1,4):
            grateful=input(f"I am grateful for #{i}: ")
            gratitude.append(grateful)
            

    elif(option==2):
        print(gratitude)

    elif(option==3):
        running=False
    else:
        print("Invalid Choice")



