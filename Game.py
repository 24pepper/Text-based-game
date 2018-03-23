print('                             \'Game\' (working title)\n                           created by Kevin Beshears\n        For instructions on how to play the game, type \'help\' at any time\n')
print('You awaken in a strange room. To your left you see a door.\nTo your right you see a window. Ahead of you, you see an old looking dresser.\nBehind you is a small hole in the wall. A small light above you dimly lights the room, flickering every couple of seconds.')
Help = 'Your basic controls while in the middle of the room are \'go\' followed by either \'forward\',\'backward\',\'left\' or \'right\'. Ex: \'go forward\'. Once you have approached something you can either examine it, take it, open it, close it, or break it. To do one of these things, you type in one of the four commands that were just mentioned followed by the object that you wish to interact with. Ex: \'open door\'. You can go back into the middle of the room by typing in \'go back\'. You have an inventory which you can access at any time by typing in \'open inventory\'. You can use somthing from your inventory by typing in \'use\' followed by what you want to use from your inventory. You do not need to type what you want to use your item on, simply approach somthing and then use your item. You have health which starts at 100 hitpoints. You can check the status of your health by typing in \'status\'.'
lst_inventory = ['there is nothing in your inventory']
user_input = input()
health = 100
found_object = False
open_window = False
bird = False
examined_hole = False
found_razor_blade = False
sliced_wood = False
input_needed = 'no'
skip_print = False
open_door = False
door_unlocked = False
a = 0
while open_door != True:
    if user_input == 'go left':
        if found_object == False:
            print('You approach the door. It is very old and battered looking. You notice a keyhole above the brass doorknob and mumble to yourself to remember that.')
        elif found_object == True:
            print('You approach the door. It is very old and battered looking. You notice a keyhole, maybe you should try using your new key.')
        if bird == True and open_window == False:
            health = health - 5
            print('The bird projectile poops in your direction and nails you right in the mouth! - 5 hitpoints.')
            if health < 1:
                print('You are dead')
                break
        user_input = input()
        while user_input != 'go back':
             if found_object == False:
                 if user_input == 'examine door':
                     print('It is very old and battered looking. You notice a keyhole above the brass doorknob and mumble to yourself to remember that.')
                 elif user_input == 'take door':
                     print('Its just a little bit to big to take.')
                 elif user_input == 'open door':
                     print('Its locked. You try every known way of getting the door open, but nothing works.')
                 elif user_input == 'break door':
                     print('You are not nearly strong enough to do that and even if you were, who knows whats on the other side of that door waiting for you after all that noise.')
                 elif user_input == 'open inventory':
                      print(lst_inventory)
                 elif user_input == 'help':
                      print(Help)
                 elif user_input == 'status':
                      print('%d hitpoints.' % health)
                 elif user_input == 'close door':
                     print('The door is already closed')
                 elif user_input == 'use razor blade':
                     if 'razor blade' in lst_inventory:
                         print('Come on, you and I both know that this little razor blade isnt cutting through this door.')
                     else:
                         print('what?')
                 else:
                     print('what?')
                 user_input = input()
             elif found_object == True:
                  if user_input == 'examine door':
                      print('It is very old and battered looking. You notice a keyhole, maybe you should try using your new key.')
                  elif user_input == 'take door':
                     print('Its just a little bit to big to take.')
                  elif user_input == 'open door':
                      if door_unlocked == False:
                          print('Its locked. You try every known way of getting the door open, but nothing works.')
                      elif door_unlocked == True:
                          print('The door creaks as you open it and you proceed to the next room.')
                          open_door = True
                          break
                  elif user_input == 'break door':
                     print('You are not nearly strong enough to do that and even if you were, who knows whats on the other side of that door waiting for you after all that noise.')
                  elif user_input == 'use gold key':
                      if 'gold key' in lst_inventory:
                          print('It doesnt seem to fit. It must be used for somthing else.')
                      else:
                          print('what?')
                  elif user_input == 'use brass key':
                      if 'brass key' in lst_inventory:
                          door_unlocked = True
                          print('The key fits perfectly and you unlock the door.')
                      else:
                          print('what?')
                  elif user_input == 'open inventory':
                     print(lst_inventory)
                  elif user_input == 'help':
                     print(Help)
                  elif user_input == 'status':
                      print('%d hitpoints.' % health)
                  elif user_input == 'close door':
                      print('The door is already closed.')
                  elif user_input == 'use razor blade':
                     if 'razor blade' in lst_inventory:
                         print('Come on, you and I both know that this little razor blade isnt cutting through this door.')
                     else:
                         print('what?')
                  else:
                     print('what?')
                  user_input = input()
        if open_door == False:
            print('You are back in the middle of the room.')
        elif open_door == True:
            a = 1
        if bird == True and open_window == False:
            print('The bird soars by your head, narrowlly missing!')
    elif user_input == 'go right':
        if open_window == False:
            print('You approach the window. You look out it and see its the middle of the night. Its pitch black and you cant see anything except for the full moon, hope the werewolfs arent hungry.')
        elif open_window == True:
            print('You approach the window. You feel a cool breeze coming from the window because it is open. You stick your head out the window to see that its the middle of the night and you are several stories up.')
        if bird == True and open_window == False:
            health = health - 5
            print('The bird slams into your back leaving scratches everywhere! - 5 hitpoints.')
            if health < 1:
                print('You are dead')
                break
        user_input = input()
        while user_input != 'go back':
              if open_window == False:
                  if user_input == 'open window':
                      if bird == True:
                          bird = False
                          open_window = True
                          print('The bird immediately flys out the window and out of sight as it is to dark outside to track the bird. You are just glad that its gone.')
                      elif bird == False:
                          open_window = True
                          print('You are suprised to find that the window easily opens. You stick your head out and realize you are several stories up. Looks like you arent escaping this way anytime soon.')
                  elif user_input == 'examine window':
                      print('Standard looking window, you might be able to open it even.')
                  elif user_input == 'take window':
                      print('Or you could just try to open it.')
                  elif user_input == 'break window':
                      print('Or you could just try to open it.')
                  elif user_input == 'open inventory':
                      print(lst_inventory)
                  elif user_input == 'help':
                      print(Help)
                  elif user_input == 'status':
                      print('%d hitpoints.' % health)
                  elif user_input == 'close window':
                      print('The window is already closed.')
                  elif user_input == 'use key' or user_input == 'use gold key' or user_input == 'use brass key':
                      if 'gold key' in lst_inventory or 'brass key' in lst_inventory:
                          print('There isnt a key hole to use the key on.')
                      else:
                          print('what?')
                  elif user_input == 'use razor blade':
                      if 'razor blade' in lst_inventory:
                          print('Now why would you do that?')
                      else:
                          print('what?')
                  else:
                      print('what?')
                  user_input = input()
              elif open_window == True:
                  if user_input == 'open window':
                      print('The window is already open.')
                  elif user_input == 'examine window':
                      print('Standard looking window that is open. You feel a cool breeze from the night air.')
                  elif user_input == 'take window':
                      print('Or you could just try to open it.')
                  elif user_input == 'break window':
                      print('Or you could just try to open it.')
                  elif user_input == 'open inventory':
                      print(lst_inventory)
                  elif user_input == 'help':
                      print(Help)
                  elif user_input == 'status':
                      print('%d hitpoints.' % health)
                  elif user_input == 'close window':
                      print('You close the window')
                      open_window = False
                  elif user_input == 'use key' or user_input == 'use gold key' or user_input == 'use brass key':
                      if 'gold key' or 'brass key' in lst_inventory:
                          print('There isnt a key hole to use the key on.')
                      else:
                          print('what?')
                  elif user_input == 'use razor blade':
                      if 'razor blade' in lst_inventory:
                          print('Now why would you do that?')
                      else:
                          print('what?')
                  else:
                      print('what?')
                  user_input = input()
        print('You are back in the middle of the room.')
        if bird == True and open_window == False:
            health = health - 10
            print('The bird somehow finds its way into your shirt and gets stuck for a couple seconds! - 10 hitpoints.')
            if health < 1:
                print('You are dead')
                break
    elif user_input == 'go forward':
        break_while = False
        break_while2 = False
        print('You approach the dresser. It is very old and antique looking. There appears to be three drawers.')
        if bird == True and open_window == False:
            print('The birds flying right at you but you expertly matrix style dodge the bird!')
        user_input = input()
        while user_input != 'go back':
            break_input = 0
            break_input2 = 0
            skip_input = False
            if break_input2 == 2:
                break_input2 = 0
                user_input = input()
            if user_input == 'open first drawer' or user_input == 'open top drawer':
                print('You open the drawer to find dust. Nothing interesting here.')
                break_input = 1
                user_input = input()
                while user_input:
                    break_input = 1
                    if break_input2 == 1:
                        user_input = input()
                    if user_input == 'examine drawer' or user_input == 'examine first drawer' or user_input == 'examine top drawer':
                        print('The drawer appears to be real wood and very sturdy. Back when they built things to last!')
                    elif user_input == 'use razor blade':
                        if 'razor blade' in lst_inventory:
                            print('The wood is to solid. This little razor blade isnt cutting it.')
                        else:
                            print('what?')
                            break_input2 = 1
                            continue
                    elif user_input == 'break drawer' or user_input == 'break first drawer' or user_input == 'break top drawer':
                        print('This is real solid wood! You dont want to break your hand trying to break this!')
                    elif user_input == 'take drawer' or user_input == 'take first drawer' or user_input == 'take top drawer':
                        print('It wont come out all to take it')
                    elif user_input == 'close drawer' or user_input == 'close first drawer' or user_input == 'close top drawer':
                        print('The drawer is now closed')
                        break_input = 0
                        input_needed = 'yes'
                        break
                    else:
                        print('You close the drawer')
                        break
                    user_input = input()
            elif user_input == 'open second drawer' or user_input == 'open middle drawer':
                while break_while == False:
                    if found_object == False:
                        print('You open the second drawer to find a gold key laying inside of it.')
                        break_input = 1
                        user_input = input()
                        while user_input:
                            break_input = 1
                            if break_input2 == 1:
                                user_input = input()
                            if user_input == 'take key' or user_input == 'take gold key':
                                print('You take the key and place it into your inventory.')
                                if lst_inventory[0] == 'there is nothing in your inventory':
                                    del lst_inventory[0]
                                    lst_inventory.append('gold key')
                                    found_object = True
                                    skip_print = True
                                    break
                                else:
                                    lst_inventory.append('gold key')
                                    found_object = True
                                    skip_print = True
                                    break
                            elif user_input == 'examine drawer' or user_input == 'examine second drawer' or user_input == 'examine middle drawer':
                                print('The drawer appears to be real wood and very sturdy. Back when things were built to last!')
                            elif user_input == 'use razor blade':
                                if 'razor blade' in lst_inventory:
                                    print('The wood is to solid. This little razor blade isnt cutting it.')
                                else:
                                    print('what?')
                                    break_input2 = 1
                                    continue
                            elif user_input == 'break drawer' or user_input == 'break second drawer' or user_input == 'break middle drawer':
                                print('This is real solid wood! You dont want to break your hand trying to break this!')
                            elif user_input == 'take drawer' or user_input == 'take second drawer' or user_input == 'take middle drawer':
                                print('It wont come out all to take it')
                            elif user_input == 'close drawer' or user_input == 'close second drawer' or user_input == 'close middle drawer':
                                print('The drawer is now closed')
                                break_while = True
                                break_input = 3
                                break
                            else:
                                break_while = True
                                print('You close the drawer.')
                                break
                            user_input = input()
                    elif found_object == True:
                         if skip_print == False:
                             print('You open the second drawer to find nothing.')
                         skip_print = False
                         user_input = input()
                         while user_input:
                             break_input = 1
                             if break_input2 == 1:
                                 user_input = input()
                             if user_input == 'examine drawer' or user_input == 'examine second drawer' or user_input == 'examine middle drawer':
                                 print('The drawer appears to be real wood and very sturdy. Back when they built things to last!')
                             elif user_input == 'use razor blade':
                                 if 'razor blade' in lst_inventory:
                                     print('The wood is to solid. This little razor blade isnt cutting it.')
                                 else:
                                     print('what?')
                                     break_input2 = 1
                                     continue
                             elif user_input == 'break drawer' or user_input == 'break second drawer' or user_input == 'break middle drawer':
                                print('This is real solid wood! You dont want to break your hand trying to break this!')
                             elif user_input == 'take drawer' or user_input == 'take second drawer' or user_input == 'take middle drawer':
                                print('It wont come out all to take it')
                             elif user_input == 'close drawer' or user_input == 'close second drawer' or user_input == 'close middle drawer':
                                print('The drawer is now closed')
                                break_while = True
                                break_input = 3
                                break
                             else:
                                 break_while = True
                                 print('You close the drawer.')
                                 break
                             user_input = input()
                break_while = False
                continue
            elif user_input == 'open third drawer' or user_input == 'open bottom drawer':
                while break_while2 == False:
                    if sliced_wood == True and 'brass key' not in lst_inventory:
                        print('The fake wood drawer has been sliced open which reveals a brass key laying underneath it.')
                        user_input = input()
                        while user_input:
                            if user_input == 'take brass key' or user_input == 'take key':
                                print('You take the brass key and place it in your inventory.')
                                if lst_inventory[0] == 'there is nothing in your inventory':
                                    del lst_inventory[0]
                                    lst_inventory.append('brass key')
                                    found_object = True
                                else:
                                    lst_inventory.append('brass key')
                                    found_object = True
                            elif user_input == 'examine drawer' or user_input == 'examine third drawer' or user_input == 'examine bottom drawer':
                                print('You should probably take that key now.')
                            elif user_input == 'break drawer' or user_input == 'break third drawer' or user_input == 'break bottom drawer':
                                print('No reason too now.')
                            elif user_input == 'take drawer' or user_input == 'take bottom drawer' or user_input == 'take third drawer':
                                print('The drawer wont come out all the way for you to take it.')
                            else:
                                break_while2 = True
                                print('You close the drawer.')
                                break
                            user_input = input()
                    elif sliced_wood == True:
                         print('The fake wood drawer has been sliced open. There is nothing else to see.')
                         user_input = input()
                         while user_input:
                            if user_input == 'examine drawer' or user_input == 'examine third drawer' or user_input == 'examine bottom drawer':
                                print('The fake woods been cut and the key has been taken. Nothing else about this drawer appears out of the ordinary.')
                            elif user_input == 'break drawer' or user_input == 'break third drawer' or user_input == 'break bottom drawer':
                                print('There is no reason too now.')
                            elif user_input == 'take drawer' or user_input == 'take bottom drawer' or user_input == 'take third drawer':
                                print('The drawer wont come out all the way for you to take it.')
                            else:
                                break_while2 = True
                                print('You close the drawer.')
                                break
                            user_input = input()
                    elif sliced_wood == False:
                        print('Nothing interesting here, just an empty drawer.')
                        user_input = input()
                        while user_input:
                            if user_input == 'use razor blade':
                                if 'razor blade' in lst_inventory:
                                    print('You slice open the thin piece of fake wood that was the bottom of the drawer to find a brass key laying underneath it.')
                                    sliced_wood = True
                                    user_input = input()
                                    if user_input == 'take brass key' or user_input == 'take key':
                                        print('You take the brass key and place it in your inventory.')
                                        if lst_inventory[0] == 'there is nothing in your inventory':
                                            del lst_inventory[0]
                                            lst_inventory.append('brass key')
                                            found_object = True
                                        else:
                                            lst_inventory.append('brass key')
                                            found_object = True
                                    else:
                                        continue
                                else:
                                    continue
                            elif user_input == 'examine drawer' or user_input == 'examine third drawer' or user_input == 'examine bottom drawer':
                                print('At first, the drawer appeared to be just like the others, but then you notice that the bottom of the drawer is actually much more fragile looking then the other two. It doesnt even look like real wood.')
                            elif user_input == 'break drawer' or user_input == 'break third drawer' or user_input == 'break bottom drawer':
                                print('You decide not to use your bare hands for such a brute task. Using somthing sharp to cut it open would do the trick.')
                            elif user_input == 'take drawer' or user_input == 'take bottom drawer' or user_input == 'take third drawer':
                                print('The drawer wont come out all the way for you to take it.')
                            else:
                                break_while2 = True
                                print('You close the drawer.')
                                break
                            user_input = input()
                break_while2 = False
                continue
            elif user_input == 'open inventory':
                  print(lst_inventory)
                  input_needed = 'yes'
            elif user_input == 'examine dresser':
                print('An antique wooden dresser with three drawers.')
                input_needed = 'yes'
            elif user_input == 'break dresser':
                print('But its an antique!')
                input_needed = 'yes'
            elif user_input == 'take dresser':
                print('Its a little to heavy to take.')
                input_needed = 'yes'
            elif user_input == 'open dresser':
                print('There appears to be multiple drawers to choose from.')
                input_needed = 'yes'
            elif user_input == 'use razor blade':
                if 'razor blade' in lst_inventory:
                    print('The dresser is made of solid wood. Its not going to cut through it.')
                    input_needed = 'yes'
                else:
                    print('what?')
                    input_needed = 'yes'
            elif user_input == 'use key' or user_input == 'use gold key' or user_input == 'use brass key':
                      if 'gold key' in lst_inventory or 'brass key' in lst_inventory:
                          print('Lucky for you a key is not required to open this dresser!')
                          input_needed = 'yes'
                      else:
                          print('what?')
                          input_needed = 'yes'
            elif user_input == 'help':
                print(Help)
                input_needed = 'yes'
            elif user_input == 'status':
                print('%d hitpoints.' % health)
                input_needed = 'yes'
            else:
                if break_input == 0:
                    print('what?')
                    user_input = input()
                elif break_input == 1:
                     print('what?')
                     break_input2 = 2
                     continue
                elif break_input == 3:
                    user_input = input()
            if input_needed == 'yes':
                input_needed = 'no'
                user_input = input()
        print('You are back in the middle of the room.')
        if bird == True and open_window == False:
            health = health - 5
            print('The bird knicks you in the arm as it flys by! - 5 hitpoints.')
            if health < 1:
                print('You are dead')
                break
    elif user_input == 'go backward':
        if found_razor_blade == True:
            print('You approach the small hole in the wall.')
        elif examined_hole == False:
            print('You approach the small hole in the wall. You hear something rustling in there.')
        elif examined_hole == True:
            print('You approach the small hole in the wall. Now that the birds gone maybe you can actually take a look in it.')
        user_input = input()
        while user_input != 'go back':
            if user_input == 'examine hole' or user_input == 'examine small hole':
                if found_razor_blade == True:
                    print('You stick your hand into the hole and dont find anything else.')
                elif examined_hole == False:
                    print('You try to look into the hole but you dont see anything. You still hear rustling so you know theres somthing in there.')
                    print('Do you want to stick your hand in there to try to see whats in it? (Answer with \'yes\' or \'no\')')
                    user_input = input()
                    while user_input:
                        if user_input == 'yes':
                            bird = True
                            examined_hole = True
                            if open_window == True:
                                print('You slowly stick your hand in the hole. You hear a loud squack from a startled bird and you instinctively draw your hand out as a terrified bird flys out of the hole and straight out the open window.')
                                break
                            elif open_window == False:
                                print('You slowly stick your hand in the hole. You hear a loud squack from a startled bird and you instinctively draw your hand out as a terrified bird flys out of the hole and madly flys around the room looking for a way out. This bird is going to hurt you if you dont let it out!')
                                break
                        elif user_input == 'no':
                            print('You are still at the hole in the wall.')
                            break
                        else:
                            print('Answer with \'yes\' or \'no\'.')
                        print('Do you want to stick your hand in there to try to see whats in it? (Answer with \'yes\' or \'no\')')
                        user_input = input()
                elif examined_hole == True:
                    print('With the bird gone and no more noises coming from the hole, you dont hesitate to stick your hand in there to see what you can find. You find somthing and pull it out to realize its the birds nest. You see a razor blade in the nest. The bird must of liked the shininess of it.')
                    user_input = input()
                    if user_input == 'take razor blade':
                        print('You take the razor blade and place it in your inventory.')
                        found_razor_blade = True
                        if lst_inventory[0] == 'there is nothing in your inventory':
                            del lst_inventory[0]
                            lst_inventory.append('razor blade')
                        else:
                            lst_inventory.append('razor blade')
                    else:
                        continue
            elif user_input == 'take hole' or user_input == 'take small hole':
                 print('That doesnt make much sense now does it?')
            elif user_input == 'break hole' or user_input == 'break small hole':
                 print('Why would you break the hole?')
            elif user_input == 'open hole' or user_input == 'open small hole':
                 print('Its a hole, its already open.')
            elif user_input == 'use razor blade':
                 if 'razor blade' in lst_inventory:
                     print('You cant seem to push the razorblade through the wall. That idea is out the window. (Not literally).')
                 else:
                     print('what?')
            elif user_input == 'use key' or user_input == 'use gold key' or user_input == 'use brass key':
                      if 'gold key' or 'brass key' in lst_inventory:
                          print('There isnt a key hole to use the key on.')
                      else:
                          print('what?')
            elif user_input == 'open inventory':
                 print(lst_inventory)
            elif user_input == 'help':
                 print(Help)
            elif user_input == 'status':
                 print('%d hitpoints.' % health)
            else:
                 print('what?')
            user_input = input()
        print('You are back in the middle of the room')
        if bird == True and open_window == False:
            health = health - 5
            print('The bird hits you across the head as its flying by and scratchs you in the process! - 5 hitpoints.')
            if health < 1:
                print('You are dead')
                break
                
                     
    elif user_input == 'open inventory':
        print(lst_inventory)
    elif user_input == 'help':
        print(Help)
    elif user_input == 'status':
        print('%d hitpoints.' % health)
    elif user_input == 'examine room':
        print('To your left you see a door. To your right you see a window. Ahead of you, you see an old looking dresser. Behind you is a small hole in the wall.') 
    else:
        print('what?')
    user_input = input()



            

                
              
        
   
