intro="\nHey there, happy to see you're using this (very) small Egg Inc. calculator\nNow ... what I need is for you to check your earning rate, wait a few hours, then check it again\nRemember both numbers well, other numbers you will just have to check when asked\n"
not_clear="\nSorry that it's not clear, why don't you send me a mail ?? I'll explain to you in more details: danidani.negreanu@gmail.com"
print(intro)
u = input("Hope that's clear, is it ? ('y' or Enter / 'n')\t")
if u != "y" and u != "yes" and u != "Y" and u != "YES" and u != "":
    print(not_clear)
    input("[Press any key to quit]")
    input("\n[Do it again, just for fun]")
    exit(1)

while (1):
    time = int(input("\nHow many hours do you have left ?\n"))
    money = float(input("How many eggs have you earned already ?\n"))
    needed = float(input("How many eggs are you aiming for ?\n"))
    now = float(input("What is your current egg rate/hour ?\n"))
    howlong = int(input("How many hours ago did you check your egg earning rate ?\n"))
    before = float(input("How much was your earning rate " + str(howlong) + " hours ago ?\n"))
    perhour = (now - before) / howlong
    total = money
    for i in range(1, time + 1):
        now += perhour
        total += now
        if total >= needed:
            print("\n\nYES, you'll complete the contract in less than " + str(i) + " hours")
            print("Meaning " + str(time - i) + " hour(s) before the deadline")
            break
        ##    print(i, total)
    if total < needed:
        print("\n\nNOPE, sorry you'll be short by " + str(needed - total) + " eggs when the deadline hits ...")
    input("")
