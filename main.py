"""
Name(s): Charlotte Yih, Aarav Leekha
Name of Project: Escape Quest
"""
#Write the main part of your program here. Use of the other pages is optional.
#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4

import time
import os
inventory=["Bag", "Flashlight", "Candy Bar", "Explosive"]

def start():
  time.sleep(1)
  print ("Escape Quest (by Charlotte Yih and Aarav Leekha)")
  time.sleep(2)
  print ("Or: You Are A Lonely Teenager Forced To Make Many Choices, Many Of Which Result In Your Arrest And Possible Death")
  time.sleep(4)
  print("~")
  time.sleep(1)
  print ("It’s a Friday night, and you and your friends have arranged to go to the local escape room.") 
  time.sleep(3)
  print ("The reviews are great, and everyone says the experience is very realistic.") 
  time.sleep(2)
  print ("It should be a fun night—except, when you arrive, you find that your friends have all ditched you to go bowling instead.")
  time.sleep(3)
  print ("Welp. There are no refunds for the tickets, but it will be hard to do an escape room all by yourself. ")
  time.sleep (3)
  choice1 = input("Do you choose to stay or leave? Enter 1 to stay or 2 to leave: ")
  if choice1 == "1":
    stay()
  elif choice1 == "2":
    leave()


def leave():
  print("~")
  print ("It’s been a long week, and you’re too tired to solve puzzles. There’s a math final next week, and you should catch up on some sleep anyways.")
  time.sleep (4)
  print ("You step outside, letting out a long sigh. There’s an ice cream shop across the street. Maybe you’ll get some before going home.")
  time.sleep(4)
  print ("Entering the store, you’re suddenly faced with a dilemma.")
  time.sleep(2)
  flavor = input("What flavor do you get? Enter 1 for strawberry, 2 for vanilla, and 3 for chocolate: ")
  if flavor == "1":
    flavor = ("strawberry")
  elif flavor == "2":
    flavor = ("vanilla")
  elif flavor == "3":
    flavor = ("chocolate")
  size = input("Size? Enter 1 for small, 2 for medium, 3 for large: ")
  if size == "1":
    size = ("small")
  elif size == "2":
    size = ("medium")
  elif size == "3":
    size = ("large")
  container = input("Cup or cone? Enter 1 for cup, 2 for cone: ")
  if container == "1":
    container = ("cup")
  if container == "2":
    container = ("cone")
  time.sleep(1)
  print ("You pay for your order, and begin the long walk home, enjoying your " + size + " " + container  + " of " + flavor + " ice cream." 
  " Bet they can’t get ice cream in that silly bowling place.")
  time.sleep(3)
  end1()

def stay():
  time.sleep(1)
  print ("There’s no use in letting the tickets go to waste.")
  time.sleep(3)
  print ("Now you get to pick between an easier room and a harder one. It's tempting to just pick the easier one, but just think of how satisfying it would be to brag to your friends about solving the harder one.")
  time.sleep(5)
  room = input("Do you pick the easier room or the harder room? Enter 1 for the easier room and 2 for the harder room: ")
  if room == "1":
    easy()
  elif room == "2":
    hard()
  else:
    print ("That's not a valid input.")

def easy():
  time.sleep(1)
  print ("After that biology test earlier, your brain isn’t working very well. Perhaps it would be better to try the easier room.")
  time.sleep(3)
  print ("The escape room employee gives you the premise.")
  time.sleep(2)
  print ("~")
  time.sleep(1)
  print ("-Circus of Clowns-")
  time.sleep(2)
  print ("The circus is in town.")
  time.sleep(2)
  print ("This mysterious exhibition shows up only once a year at the end of summer—always for a single day, arriving at sunset and disappearing before dawn. It’s a big hit with the kids, especially since admission is free, but there was always something strange about it—what kind of business makes admissions free?")
  time.sleep(7)
  print ("Oh yeah, and the fact that there have been multiple strange disappearances coinciding with the circus's arrival. That too. One year ago, your friend went missing, and they were last seen running to the circus late at night. They’re not the greatest friend, always wanting to go bowling during your time together. But they do owe you $20, and you’re going to get that back, whatever it takes.")
  time.sleep(8)
  print ("If it’s truly nothing, at least you can get some cotton candy!")
  time.sleep(3)
  print("It’s past midnight, and you’ve just arrived at the circus to investigate for an hour or so. Tiptoeing your way through—god, that’s a lot of clown wigs—you’ve just entered the backroom, when you hear a loud honk behind you.")
  time.sleep(6)
  print ("You turn around immediately, and notice that the entrance has disappeared. Crap.")
  time.sleep(3)
  print ("Your objective:  Solve the mystery of the circus and escape within an hour, before the circus master comes back and turns you into a clown too.")
  time.sleep(4)
  print ("~")
  time.sleep(1)
  print ("You open the door to the escape room, fully prepared to immerse yourself into the game as if you were really someone investigating a creepy circus where their friend had disappeared, before—")
  time.sleep(4)
  print ("*CRASH*")
  time.sleep(2)
  print("Something in the room crashes to the ground.") 
  time.sleep(2)
  print ("You blink. Is that supposed to happen?")
  time.sleep(2)
  print("As if to answer your question, the escape room employee curses, and quickly ushers you to the other room—the harder one. Before you can open your mouth to protest, you’re shoved in there. Have fun!")
  time.sleep(5)
  hard()
  
def hard():
  time.sleep(3)
  print ("The employee gives you the premise.") 
  time.sleep(2)
  print ("~")
  time.sleep(1)
  print ("-Hidden Heist-")
  time.sleep(2) 
  print ("Renovations on your city's largest bank have begun.")
  time.sleep(2)
  print ("It’s a terrible bank. The interest rate is high as hell, and they don’t even give out free pens.")
  time.sleep(3)
  print ("To keep the bank’s funds safe during the construction process, the money has been moved to a less secure vault in a nearby building. That building, however, is open to the public, and so you wonder: how hard could it really be to steal all that money?")
  time.sleep(6)
  print ("You know that nobody has yet tried to rob the building, as it has become complacent with its security measures—there's only three guards in the morning, and a single guard at night. Somewhere in there lies several thousand dollars in cold hard cash, waiting for you.")
  time.sleep(7)
  print("So, in the dead of night, you and your friends drive to the bank. You will be the one sneaking into the vault while they wait for you in the car. From the second you enter, you’ll have two hours before the morning guards arrive to get the money and make away with as much as you can without getting caught.")
  time.sleep(9)
  print("Your objective: Find and break into the vault containing the cash as fast as possible without alerting the night guard.")
  time.sleep(5)
  print("~")
  print("With you, you've brought:")
  print(inventory)
  time.sleep(4)
  print("To use an item, enter its name when prompted.")
  time.sleep(3)
  print("Now, back to the heist: you enter the bank. The hallway you’re walking down has a room to its left and right, and you suddenly realize that you don’t know the layout of the building at all, much less where the guard will be. There are signs on both rooms, but turning on your flashlight to get a better look might alert the guard.")
  time.sleep(5)
  hard1 = input(" Do you go to the left room, the right room, keep on walking straight ahead, or turn on your flashlight to take a look at the signs? Enter 1 to go left, 2 to go right, 3 to keep on walking, 4 to turn on your flashlight: ")
  if hard1 == ("1"):
    leftoff()
  elif hard1 == ("2"):
    rightroom()
  elif hard1 == ("3"):
    straight()
  elif hard1 == ("4"):
    print("You turn on your flashlight. The door to your left reads: “Storage Room”. The door to your right reads: “Janitor’s Closet.”")
    time.sleep(3)
    hard2 = input ("Do you go to the left room, the right room, or keep on walking ahead? Enter 1 to go left, 2 to go right, 3 to keep on walking: ")
  if hard2 == ("1"):
    lefton()
  elif hard2 == ("2"):
    rightroom()
  elif hard2 == ("3"):
    straight()
def leftoff():
  print("~")
  print ("The room is very dimly lit, but you can see a little if you squint really hard.")
  time.sleep(2)
  flashlight = input("Do you turn on your flashlight? Enter 1 to turn on your flashlight, 2 to keep it off: ")
  if flashlight == ("1"):
    lefton()
  elif flashlight == ("2"):
    print("You decide to keep your flashlight off. You get the sense that this is a large room.") 
    time.sleep(2)
  leftA = input("Do you go left, right, walk straight, or exit the room? Enter 1 to go left, 2 to go right, 3 to go straight, and 4 to exit the room: ")
  if leftA == ("1"):
    leftleft()
  elif leftA == ("2"):
    leftright()
  elif leftA == ("3"):
    leftstraight()
  elif leftA == ("4"):
    leftleave()
def leftleft():
  leftleftA = input("You feel boxes. Do you try to investigate the boxes further? Enter 1 for yes or 2 for no: ")
  if leftleftA == ("1"):
    leftboxes()
  elif leftleftA == ("2"):
    leftA = input("Do you go left, right, walk straight, or exit the room? Enter 1 to go left, 2 to go right, 3 to go straight, and 4 to exit the room: ")
    if leftA == ("1"):
      leftleft()
    elif leftA == ("2"):
      leftright()
    elif leftA == ("3"):
      leftstraight()
    elif leftA == ("4"):
      leftleave()
  elif leftleftA != ("1") or ("2"):
    print("That's not a valid input.")
    leftleftA()
def leftboxes():
  leftboxnum = input("Which box would you like to open? Enter 1 for box 1, 2 for box 2, etc, and 5 to investigate another part of the room: ")
  if leftboxnum == ("1"):
    print("There’s a metal plaque, but it’s so rusted over that you can’t tell what it says.")
    time.sleep(2)
    openinv = input("Enter 1 to open your inventory or 2 to keep looking at boxes: ")
    if openinv == ("2"):
      leftboxnum()
    elif openinv == ("1"):
      print(inventory)
      useinv = input("Enter the lowercase name of any item to use it: ")
      if useinv == ("metal polish"):
        metalpolish = input("Do you try to polish the box? Enter 1 for yes, 2 for no: ") 
        if metalpolish == ("1"): 
          print("You polish the plaque using the metal polish. The rust slowly disappears, and in the dim lighting of the room, you can finally read what it says: “Employee of the Month: Jim, 2007.” ")
          time.sleep(4)
          inventory.append("Metal plaque")
          print("Item Obtained: ‘Metal plaque.’")
      elif useinv != ("metal polish"):
        print("You don't think that will work here.")
    leftboxes()
  elif leftboxnum == ("2"):
    print("Well, you try to open it. The lid is somehow partially stuck. You’d need some sort of strong stick to get this open.")
    time.sleep(3)
    openinv1 = input("Enter 1 to open your inventory or 2 to keep looking at boxes: ")
    if openinv1 == ("1"):
      print(inventory)
      useinv = input("Enter the lowercase name of any item to use it: ")
      if useinv == ("mop"):
        openmop = input("Do you try to open the box using the mop? Enter 1 for yes or 2 for no: ")
        if openmop == ("1"):
          print("You stick the handle of the mop into the small space between the lid and the box, and get it to fully open. In the box are a bunch of guard outfits.")
          time.sleep(4)
        guardoutfit = input("Do you put on a guard outfit? Enter 1 for yes or 2 for no: ")
        if guardoutfit == ("1"):
          print("You quickly put on the guard outfit.")
        if guardoutfit == ("2"): 
          print("You don't put on the guard outfit.")
          if openmop == ("2"):
            print("You don't try to open the box.")
      elif useinv == ("candy bar"):
        candybar = input("Do you eat the candy bar? Enter 1 for yes, 2 for no: ")
        if candybar == ("1"):
          print("You eat the candy bar. Yum!")
          inventory.remove("Candy Bar") 
        if candybar == ("2"):
          print("You put it away. Maybe later.")
          leftboxes()
      elif useinv == ("explosive"):
        print("You use the explosive. The door explodes, but so do you.")
        time.sleep(2)
        end2()
      else:
        print("That's not a valid input.")
      leftboxes()
  elif leftboxnum == ("3"):
    print("Nothing.")
    leftboxes()
  elif leftboxnum == ("4"):
    print("...Bowling pins.")
    leftboxes()
def leftright():
  print("You start walking right. You trip over somethin strange…and you realize all too late that it’s a leg—the leg of the guard. Though they seem to have just been snoozing on a chair, they’re now fully awake. You hurriedly back up, trying to hide, but it’s too late—the guard yells, and the lights in the room turn on. The guard tackles you to the floor.")
  time.sleep(7)
  end2()
def leftstraight():
  print("Moving slowly across the floor, you bump into what seems to be a cardboard box. You bend down, waving your arms around, and feel that there are more large boxes all in a pile. Judging by the ease in which you can push them, they all seem to be empty.")
  time.sleep(7)
  cardboardboxesnum()
def cardboardboxesnum():
  cardboardboxes = input("You feel 5 boxes. Which box would you like to open? Enter 1 for box 1, 2 for box 2, etc, and 6 to investigate another part of the room: ")
  if cardboardboxes == ("6"): 
    leftA = input("Do you go left, right, walk straight, or exit the room? Enter 1 to go left, 2 to go right, 3 to go straight, and 4 to exit the room: ")
    if leftA == ("1"):
      leftleft()
    elif leftA == ("2"):
      leftright()
    elif leftA == ("3"):
      leftstraight()
    elif leftA == ("4"):
      leftleave()
  if cardboardboxes == ("1"):
    print("Nothing, not even dust.")
    time.sleep(1)
    cardboardboxesnum()
  if cardboardboxes == ("2"):
    print("There's a spider—you close the box as quickly as you can.")
    time.sleep(1)
    cardboardboxesnum()
  if cardboardboxes == ("3"):
    print("There's a photograph in there. It depicts…8 cats? It’s captioned: “My cats! Meowmeow, Penelope, Gucci, Boss, Ophelia, Willow, Leo, and Clover!” All of the cats are wearing sunglasses.")
    inventory.append("Photograph")
    time.sleep(8)
    print("Item Obtained: Photograph.")
    time.sleep(1)
    cardboardboxesnum()
  if cardboardboxes == ("4"):
    print("A large amount of dust billows up—ACHOO!")
    time.sleep(1)
    cardboardboxesnum()  
  if cardboardboxes == ("5"):
    print("Nothing, not even dust.")
    time.sleep(1)
    cardboardboxesnum()

def lefton():
  print ("You slowly move your flashlight around the room, trying to get a better sense of your surroundings. To your left, several large, plastic boxes—unsurprising, since this is a storage room. In front of you, cardboard boxes, though those seem to be empty. And to your right—")
  time.sleep(7)
  print ("You’ve shone your flashlight directly into the face of the guard, who blinks sleepily at you. Though they seem to have just been snoozing on a chair, they’re now fully awake. You hurriedly turn off the flashlight, but it’s too late—the guard yells, and the lights in the room suddenly turn on.")
  time.sleep(8)
  print("The guard tackles you to the floor.")
  time.sleep(1)
  end2()

def leftleave():
  leave = input("Do you go to the left room, the right room, or keep on walking ahead? Enter 1 to go left, 2 to go right, 3 to keep on walking: ") 
  if leave == ("1"):
    leftoff()
  elif leave == ("2"):
    rightroom()
  elif leave == ("3"):
    straight()
  
def rightroom():
    print("It’s locked. Darn it. There’s a keyhole, though.")
    time.sleep(1)
    unlock = input("Do you try to unlock the door? Enter 1 to try to unlock the door, 2 to not: ")
    if unlock == ("1"):
      print (inventory)
      usekey = input("Enter the lowercase name of the item you'd like to use to unlock the door, or 2 to go back: ")
      if usekey == ("2"):
        print("You don't unlock the door.")
        rightleave = input("Do you go to the left room or continue down the hallway? Enter 1 to go left or 2 to continue down the hallway: ")
        if rightleave == ("1"):
          leftoff()
        elif rightleave == ("2"):
          straight()
      if usekey == ("gold key"):
        print ("The door unlocks!")
        time.sleep(4)
        flashlightright = input("Do you turn on your flashlight? Enter 1 to turn on your flashlight, 2 to keep it off: ")
        if flashlightright == ("1"):
          righton()
        elif flashlightright == ("2"):
          rightoff()
      elif usekey == ("explosive"):
        print("You use the explosive. The door explodes, but so do you.")
        time.sleep(2)
        end2()
      elif usekey != ("gold key") or ("explosive"):
        print("You don't think that would work here.")
        rightroom()
    elif unlock == ("2"):
      print("You don't unlock the door.")
      rightleave = input("Do you go to the left room or continue down the hallway? Enter 1 to go left or 2 to continue down the hallway: ")
      if rightleave == ("1"):
        leftoff()
      elif rightleave == ("2"):
        straight()
  
def rightoff():
  print ("You can’t see anything. ")
  rightofflight = input("Do you turn on your flashlight? Enter 1 to turn on your flashlight, 2 to keep it off: ")
  if rightofflight == ("1"):
    righton()
  elif rightofflight == ("2"):
    print (" You blindly fumble your way around the room into a closet. Nearly tripping over what’s probably a mop, you spread out your arms to catch yourself. Your hand closes around something small and metal on the shelf you’ve caught yourself on—a key. You tuck it in your pocket.")
    time.sleep(8)
    inventory.append("Small Key")
  shelves = input("Do you investigate the shelves further, or continue feeling your way into the room? Enter 1 to investigate the shelves, 2 to continue into the room: ")
  if shelves == ("1"): 
    print ("You carefully move your hand along the shelves. There are bottles of what must be cleaning products, but you can’t read their labels in the dark.") 
    time.sleep(4)
    closet = input("Do you come out of the closet or go deeper in? Enter 1 to come out of the closet, 2 to continue exploring: ")
    if closet == ("1"):
      print("Congratulations!") 
      rightoffleave = input("Do you go to the left room or continue down the hallway? Enter 1 to go left or 2 to continue down the hallway: ")
      if rightoffleave == ("1"):
        leftoff()
      elif rightoffleave == ("2"):
        straight()
    elif closet == ("2"):
      print("You take a step forward, hands held out in front of you to prevent crashing into anything. There’s something large in front of you. You’re not quite sure what it is. Moving around it, your hand closes around the mop that almost tripped you, and you push it aside.")
      time.sleep(7)
      mop = input("Do you take the mop? Enter 1 to take the mop and 2 to leave it: ")
      if mop == ("1"):
        inventory.append("Mop")
      elif mop == ("2"):
        print("You leave the mop behind.")
      print("Walking further, your foot nudges something. It feels like a trash can.")
      time.sleep(2)
      investigate = input("Do you choose to investigate the trash can? Press 1 to investigate or 2 to move on: ")
      if investigate == ("1"):
        print("There’s something strange inside…something furry…that just bIT YOU—Ouch! You jump back, crashing into the shelves. Double ouch! What the hell—was that a rat? However, you have no time to wonder, as the door to the closet bursts open, the guard standing there: “What are you doing—come out, hands in the air!”")
        time.sleep(8)
        end2()
      elif investigate == ("2"):
        print("You don’t try to investigate the trash can. Which is probably a smart decision, as you don’t know what kind of trash is in there.")
        time.sleep(4)
      rightleave = input("Do you go to the left room or continue down the hallway? Enter 1 to go left or 2 to continue down the hallway: ")
      if rightleave == ("1"):
        leftoff()
      elif rightleave == ("2"):
        straight()

def righton(): 
  print("It’s what you’d expect of a janitor's closet. Not very big, and filled with cleaning supplies. You look around to see if you can find anything useful. There’s one of those janitor carts, next to a bunch of shelves on the left wall. There’s a vacuum in the back, along with a trash can. And there’s a long mop, resting against the right wall.")  
  time.sleep(9)
  explore = input("Do you investigate the janitor’s cart, the shelves, the vacuum, the trash can, the mop, or exit the room? Enter 1 to investigate the janitor’s cart, 2 for the shelves, 3 for the vacuum, 4 for the trash can, 5 for the mop, 6 to exit: ")
  if explore == ("1"):
    print("There are a few bottles of cleaning solutions on the cart, but they’re all mostly empty, so it wouldn’t do you any good to take them. There’s also a bucket. A label on it reads, “Property of Stanley.” Strangely, the bucket gives you an odd sense of comfort.You bend down, trying to see if the cart has anything else, and notice a binder sitting on the bottom of the cart. It’s filled with datasheets about cleaning products, but in the very back, there's a slip of paper with sketches of stylized animals on it. There’s an elephant, a camel, a lizard, and a bird, labeled 1-4 respectively. You pick it up.") 
    time.sleep(12)
    inventory.append("Paper Slip")
  elif explore == ("2"):
    print ("There are many bottles of cleaning products on the shelves—disinfectants, floor cleaning solution, glass cleaning solution, metal polish, toilet bowl cleaner, etc. You suppose you could bring one of them with you, but you can’t think of a use for anything now.")
    time.sleep(7)
    take = input("Do you bring one of the cleaning products with you? You only have room for one, and you can always switch them. Enter 1 for the disinfectant, 2 for the floor cleaning solution, 3 for the glass cleaning solution, 4 for the metal polish, 5 for the toilet bowl cleaner, 6 to not get anything: ")
    if take == ("1"):
      inventory.append("Disinfectant")
    elif take == ("2"):
      inventory.append("Cleaning Solution")
    elif take == ("3"):
      inventory.append("Glass Cleaning Solution")
    elif take == ("4"):
      inventory.append("Metal Polish")
    elif take == ("5"):
      inventory.append("Toilet Bowl Cleaner")
  print (inventory)
  if explore == ("3"):
    print("It’s a vacuum. Old, and incredibly dusty, which is ironic.")
    time.sleep(2)
    vacuumon = input("Do you turn it on? Enter 1 to turn it on, 2 to keep it off: ")
    if vacuumon == ("1"):
      print ("You turn the vacuum on. The noise is incredibly loud, but before you have a chance to turn it off, the guard comes rushing into the room, and says: “You’re not supposed to be here!”")
      time.sleep(3)
      end2()
    elif vacuumon == ("2"):
      print ("You don't turn it on. Smart")
  elif explore == ("4"):
    print ("You peer into the trash can, and—is that a rat? The rat is sitting on top of something you can’t quite see clearly. Perhaps if you could somehow lure the rat away from the object with something in your inventory…")
    feedrat = input("Do you try to feed the rat with the candy bar? Enter 1 to feed the rat, 2 to put it away: ")
    if feedrat == ("1"): 
      print("You unwrap the candy bar and drop it in the trash can, next to the rat. The rat eats it. The rat, Gerald, is now your best friend. He wouldn’t ditch you to go bowling.")  
      time.sleep(3)
      print("Gerald then climbs to the top of the trash can, with a lock pick in his teeth, handing it to you.")
      inventory.append("Basic lock pick")
    if feedrat == ("2"):
      print("You don't feed the rat.")
    explore()
  elif explore == ("5"):
    print ("Is a long, sturdy mop. It might be a hindrance to carry around.")
    time.sleep(1)
    mop = input("Do you take the mop? Enter 1 to take the mop and 2 to leave it: ")
    if mop == ("1"):
      inventory.append("Mop")
    elif mop == ("2"):
      print("You leave the mop behind.")
  rightleave = input("Do you go to the left room or continue down the hallway? Enter 1 to go left or 2 to continue down the hallway: ")
  if rightleave == ("1"):
    leftoff()
  elif rightleave == ("2"):
    straight()

def straight():
  print("You keep on walking, and realize there are stairs up ahead.")
  flashlight2 = input("Do you turn on your flashlight? Enter 1 to turn on your flashlight and 2 to turn it off: ")
  if flashlight2 == ("1"):
    print("You’re in a large room. There’s a couple filing cabinets to your left, as well as a door to the restroom. To your right, a desk. Just a foot front of you, a large potted plant. Thank goodness your flashlight is on, or you might have crashed into it. And on the other side of the room—the vault.")
    time.sleep(5)
    explore2()
  elif flashlight2 == ("2"):
    print("You keep your flashlight off and continue walking into the room… *CRASH* …and walk straight into something, toppling onto the floor. A second later, the guard rushes into the room, turning the lights on and yelling “Stop!”")
    time.sleep(5)
    end2()
def explore2():
  explore2 = input("Enter 1 to investigate the filing cabinets, 2 to enter the restroom, 3 to investigate the desk, 4 to inspect the plant, 5 to look at the vault, and 6 to go back up the stairs: ")
  if explore2 == ("1"):
    cabinets()
  elif explore2 == ("2"):
    restroom()
  elif explore2 == ("3"):
    desk()
  elif explore2 == ("4"):
    plant()
  elif explore2 == ("5"):
    vault()
  elif explore2 == ("6"):
    back = input(" Do you go to the left room, the right room, or keep on walking straight ahead? Enter 1 to go left, 2 to go right, 3 to keep on walking: ")
  if back == ("1"):
    leftoff()
  elif back == ("2"):
    rightroom()
  elif back == ("3"):
    straight()
def vault():
  print("It’s a dual lock—there’s both a keypad and large combination lock. Ew. You’re tempted to just use the explosive you brought.")
  time.sleep(3)
  vault1 = input(" Do you try to unlock the vault, use the explosive, or continue searching the room? Enter 1 to try to unlock the vault, 2 to use the explosive, 3 to continue searching: ")
  if vault1 == ("1"):
    vaultunlock()
  elif vault1 == ("2"):
    print("You use the explosive. The vault door opens, and in front of you are mountains and mountains of cash. You step in, practically salivating, then—")
    time.sleep(3)
    print("The guard runs at you, pointing their gun. “Hands up! Aw, snickerdoodles.")
    end2()
  elif vault1 == ("3"):
    explore2()
def vaultunlock():
  print("Inspecting the keypad, you find that the screen has room for 7 characters—a symbol and 6 numbers. Inspecting the combination lock, you see that there are only the numbers 1-4.")
  time.sleep(4)
  print("You try to unlock the keypad.  For the symbols, you’re given a choice between a circle ◯, triangle △, square ▢, and diamond ♢. The numbers are the typical 0-9.")
  time.sleep(4)
  keypad = input("Enter your choice of a symbol (by copy pasting) followed by 6 letters here: ")
  while keypad != ("♢451015"):
    keypad = input("Enter your choice of a symbol followed by 6 letters here: ")
  if keypad == ("♢451015"):
    print("The keypad flashes green, and you can faintly hear something moving in the mechanism of the vault door. Yay!")
    time.sleep(3)
    print ("You try to unlock the combination lock. Looking closer, you can see that there are four motifs right above the lock—wind, water, earth, and fire, in that order. Four symbols…hm.")
    time.sleep(4)
    print(inventory)
    useinv = input("Enter the lowercase name of the item you'd like to use: ")
    while useinv != ("paper slip"):
      useinv = input("Enter the lowercase name of the item you'd like to use: ")
    if useinv == ("paper slip"):
      print(" It’s filled with datasheets about cleaning products, but in the very back, there's a slip of paper with sketches of stylized animals on it. There’s an elephant, a camel, a lizard, and a bird, labeled 1-4 respectively.")
      time.sleep(5)
  comblock = input("Which numbers do you spin the lock to? Enter a 4 digit number using the number 1-4, no repeats: ")
  while comblock != ("4132"):
    comblock = input("Which numbers do you spin the lock to? Enter a 4 digit number using the number 1-4, no repeats: ")
  if comblock == ("4132"):
    print("The door to the vault swings open. You open your mouth in disbelief—you didn’t think you’d actually complete this! You hurriedly stuff the bag you have with as much money as you can, then set off. As you’re running down the hallway towards the exit, you spot Gerald walking towards you. They haven’t seemed to notice you yet, but they’re about to. If you go back down the stairs, the chances they’ll see you are high.")
    time.sleep(7)
    escape = input("Quick, do you hide in the left or right room? Enter 1 for the left room, 2 for the right room: ")
    if escape == ("1"):
      print("You hide in the left room. You hear Gerald walking down the hallway, entering the left room—shoot. The guard spots you immediately.") 
      time.sleep(3)
      end2()
    if escape == ("2"):
      print("You hide in the right room. You hear Gerald walking down the hallway, entering the left room—oh thank whatever’s watching that you didn’t choose to hide there. As soon as you hear Gerald’s footsteps fade, you dash out of the janitor’s closet, and out the front door. In the game, with several thousand dollars in your hand, you jump into the getaway car, and ride away into the dawn. In the real world, you burst out of the door you came in, with a smile on your face.")
      time.sleep(8)
      end3()

def plant():  
  print(" You inspect the potted plant. …It turns out to be a fake plant. Bummer.")
  time.sleep(2)
  explore2()
def desk():
  print("You investigate the desk—it’s beautiful, being made of mahogany. On the surface of the desk, there are stacks and stacks of boring paperwork. There’s too much for any of it to be of use to you. However, on top of one of the stacks is a pink, heart-shaped sticky note. It reads, “Hey <3! Won’t be home tonight, so remember to feed the cats later! Love, V.” You check out the rest of the desk. There’s a single drawer on it. You try opening it, but it seems to be locked. Upon closer inspection, there are small buttons on the drawer, numbered 1-10.")
  time.sleep(10)
  button = input("Which button do you press? Enter a number between 1 & 10: ")
  if button == ("8"):
    print("The drawer opens. Inside, a little crocheted cat, along with a gold key. You’d feel bad for taking the cat, so you only take the key.")
    time.sleep(3)
    inventory.append("Gold Key")
  elif button != ("8"):
    print("It doesn't work.")   
  explore2()

def restroom():
  print("Though you don’t feel like using it, you enter the restroom. Looking around, you spot a giant mirror, some sinks, and five stalls.")
  time.sleep(3)
  explore3()

def explore3():
  restroom1 = input("Do you investigate the mirror, the sinks, the stalls, or leave? Enter 1 for the mirror, 2 for the sinks, 3 for the stalls, and 4 to leave: ")
  if restroom1 == ("1"):
    print ("You investigate the mirror, fixing up your hair in the process. The mirror’s a little grimy, but that’s all.")
    time.sleep(3)
    explore3()
  elif restroom1 == ("2"):
    print ("You investigate the sinks. They all seem to work fine, except for one that spews out some strange, orangy water. Ew.")
    time.sleep(3)
    explore3()
  elif restroom1 == ("3"):
    print("You open the door to each of the five stalls. Each has more graffiti than the last. You try cleaning the graffiti off each of the stalls.")
    time.sleep(4)
    print("You clean the first stall. There’s…nothing behind the graffiti")
    time.sleep(1)
    print("You clean the second stall. There’s a diamond symbol etched into the wall.")
    time.sleep(1)
    print("You clean the third stall. There’s a little drawing of a bunny on it. Aw!")
    time.sleep(1)
    print("You clean the fourth stall. There’s a triangle symbol etched into the wall.")
    time.sleep(1)
    print("You clean the fifth stall. There’s…nothing behind the graffiti.")
    explore3()
  elif restroom1 == ("4"):
    explore2()


def cabinets():
  print("You investigate the filing cabinets. There are three, and each of them has three sections.You can’t find anything in the first cabinet.In the second cabinet, you find a lone duck plushie in the first drawer. The drawer is labeled: “Gregory the 1st.” There’s nothing in the other two drawers. The third cabinet is completely locked. It needs a key to open.")
  print (inventory)
  unlock2 = input("Enter the lowercase name of the item you would like to use to unlock the cabinet: ")
  if unlock2 == ("small key"):
    print("The cabinet unlocks! In the first drawer of the cabinet, you find a rubber duck. Squeak! The second drawer is empty. In the third drawer, you find a file. It seems to be a file about some employees in the building.")
    time.sleep(5)
    print("It reads: Employee #1: Harold, Employee #2: Mike, Employee #3: Ted, Employee #4: Stanley, Employee #5: Gerald Employee #6: Jane, Employee #7: Paul, Employee #8: Stephanie, Employee #9: Zack, Employee #10: Vincent, Employee #11: Lindsey, Employee #12: Chris, Employee #13: Larry, Employee #14: Henry, Employee #15: Jim, Employee #16: John Employee #17: Steve, Employee #18: Doug. ")
    inventory.append("Employee Sheet")
  else:
    explore2()
  explore2()
        
  
  


def end1():
  time.sleep(2)
  print("Hope you had fun!") 
  restart = input("To restart this game, enter 'restart':")
  if restart == "restart":
    os.system('clear')
    start()

def end2():
  time.sleep(2)
  print("Hope you had fun!")
  restart = input ("To restart this room, enter 'room'. To restart the game, enter 'restart': ")
  if restart == "room":
    os.system('clear')
    hard()
  elif restart == "restart":
    os.system('clear')
    start()

def end3():
  time.sleep(2)
  print("Congratulations on beating the room! Hope you had fun!")
  
start()
