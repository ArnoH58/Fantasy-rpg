import time


def main():


    def displayintro():

        print("The crackle of burning wood and screams echo through the village of ka'th")
        print("Once a humble and peaceful village, now being plundered and burned by the North Orcs")
        print("You awaken from your sleep in cold sweat after seeing this in a vision")


    displayintro()
    time.sleep(4)


    answer = input("Will you Stand up?: ")


    if answer == "Yes":
        print("You stand up and look to the floor")
        time.sleep(1)
    else:
        print("You get up regardless and look to the floor")
        time.sleep(1)

    print("On the floor you are presented with a {Sword}, a {Staff}, a {Sheild}")
    time.sleep(1)

    answer_1 = input("What will your weapon of choice be? :")
    time.sleep(1)
    if answer_1 == "Sword":
        print("You touch the Sword and remember a time when you once...")
        time.sleep(1)

        answer_1 = input("{Protected} or {Murdered} with it :")
        time.sleep(1)
        if answer_1 == "Protected":
            print("You are a Templar Knight")
            time.sleep(1)
        else:
            print("You are a Dredd Knight")
            time.sleep(1)

    if answer_1 == "Staff":
        print("You touch the Staff and feel a sense of...")
        time.sleep(1)

        answer_1 = input("{Restoration} or {Death} with it :")
        time.sleep(1)
        if answer_1 == "Restoration":
            print("You are a Cleric Mage")
            time.sleep(1)
        else:
            print("You are a Nercomancer")

    if answer_1 == "Shield":
        print("You touch the Shield and feel a rush of...")
        time.sleep(1)

        answer_1 = input("{Strength} or {Power} with it :")
        time.sleep(1)
        if answer_1 == "Strength":
            time.sleep(1)
            print("You are a Royal Sentinel")
        else:
            print("You are a Savage Brute")

    restart = input("Do you wish to play again [yes/no]")
    if restart == "yes":
        main()
    else:
        exit






main()











