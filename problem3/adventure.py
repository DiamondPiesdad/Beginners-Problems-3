print("You are exploring a rainforest in search of treasure. ")
print("Legend has it that there are some buried on a nearby island.")
print("You come across a lake.")
a=str(input("Do you want to swim across, or wait for a boat? (swim/wait):"))
if a=="swim":
    print("You get eaten by a hungry shark. Game over.")
if a=="wait":
    print("A boat arrives and you arrive at the island safely. ")
    print("You come to a cave.")
    b=str(input("Do you want to venture inside or walk on? (venture/walk):"))
    if b=="venture":
        print("You are squished by boulders never to be seen again. Game over.")
    if b=="walk":
        print("You’re at a crossroads.")
        c=input("Do you go left, right, or straight? (left/right/straight):")
        if c=="left":
            print("You are trampled by a herd of wildebeest. Game over.")
        if c=="straight":
            print("You get stung by a poisonous wasp. Game over.")
        if c=="right":
            print("You march on and find the buried treasure!")
print("THE END")