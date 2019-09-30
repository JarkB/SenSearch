"""
Using dictionaries, create a simple database of states and their senators by reading input from a text file
"""
"""
Create a dictionary from the file
"""
import pdb;
import random;

def createDict():#creates a dictionary from text file
   with open("senators.txt","r") as file:
      index = 0
      senlist = {}
      for key in file:#parse 3 lines each loop
         try:#try catch to avoid errors if file isnt divisible by 3
            senlist[key.replace('\n','')] = [next(file).replace('\n',''), next(file).replace('\n','')]  
         except StopIteration:
            pass
   return senlist;
   
def stateMode():#User enters a state, and program outputs the senators from that state
   mode = 0
   while mode == 0:#run until user quits
      state = str(input("You have selected State Lookup. Please enter a U.S. State, or enter 'q' to quit\n"))
      if state.lower() == 'q':
         mode = -1 
      else:
         sens = database.get(state.lower())#state.lower so user can enter any capitalization of the state
         if sens != None:
            print("The senators for {0} are {1}".format(state.lower().title(), " and ".join(sens)))#print.format is pythons form of printf
         else:
            print("State not found. Please check your spelling and try again.")
 
   return;

def senMode():#User enters the name of a senator, and program outputs the state (s)he is from and his/her party
   mode = 1
   while mode == 1:
      sen = str(input("You have selected Senator Lookup. Please enter a senator's name, or enter 'q' to quit\n"))
      #pdb.set_trace()
      if sen.lower() == 'q':
         mode = -1 
      else:
         for states, sens in database.items():#for state name and senator list in a list of keys and values.
            for names in sens:
               if names.lower()[0:-3] == sen.lower():#names.lower[0:-3] omits the party of the senator to allow for search
                  print(names[-3:], states.title(), sep = " from ")#print sep makes output pretty. "[Party] from [State]
   return;
   
def partyMode():#not as fun as it sounds. Input a political party and output all members of that party in the Senate
   mode = 2
   while mode == 2:
      party = str(input("You have selected Party Lookup. Please enter the party you wish to search for:\nD = Democrat\nR = Republican\nI = Independent\nor, enter 'q' to quit\n"))
      if party.lower() == 'q':
         mode = -1
      else:
         partymembers = []#Create a list
         if party.lower() == 'd': #Assign each letter a full name for pretty output
            properparty = 'Democrats'
         elif party.lower() == 'r':
            properparty = 'Republicans'
         elif party.lower() == 'i':
            properparty = 'Independents'
         else:
            properparty = party+'s'
                     
         for states, sens in database.items():#Traverse through all values in dict
            for names in sens:
               if names[-2:-1] == party.upper():#If senator is in party, add to list
                  partymembers.append(names)
         print("There are {0} {1} in the U.S. senate".format(len(partymembers), properparty))#Prints the number of party members
         partymembers.sort()#alphabetical to improve readability
         count = 0
         txt = ''
         for s in partymembers:#Print 5 party members per line
            if count%5== 0:
               txt+='\n'
            txt+= s + ', '
            count+=1
         print(txt[0:-2])
   return;
   
def gameMode():#Module for games, dont bother defining methods until they will be used
      
   def stateGame():#Game to guess the senators for a random state
      again = 1
      score = 0
      while again == 1:
         state, senator = random.choice(list(database.items()))#state is the key, senator is the list of values
         #prompt for 1 senator of a state
         senguess = str(input("Name one of the senators from {0}\n".format(state.title())))
         if senguess == senator[0][0:-3] or senguess == senator[1][0:-3]:#If they get it right, the senator they guessed must be revealed
            score += 1
            print("Correct! Score:{0}".format(score))
            sencorrect = senguess
            if senguess == senator[0][0:-3]:#remove the guessed senator from the list
               senator.remove(senguess+senator[0][-3:])
            else:
               senator.remove(senguess+senator[1][-3:])  
            senguess = str(input('One of the senators from {0} is {1}. Name the other.\n'.format(state.title(),sencorrect)))#prompt for other senator
            if senguess == senator[0][0:-3]:
               score += 1
               print('Correct! Score:{0}'.format(score))
            else:
               score -= 1
               print('Incorrect! Score:{0}'.format(score))
               
            print("The Senators from {0} are {1} and {2}".format(state.title(), sencorrect, senator[0][0:-3]))#finally reaveal all senators
         
         else:#If they get it wrong, any of the senators can be revealed
            score -= 1
            print("Incorrect! Score:{0}".format(score))
            #reveal one senator, and ask for the other
            senguess = str(input("One of the senators from {0} is {1}. Name the other.\n".format(state.title(), senator[0][0:-3])))
            if senguess == senator[1]:#compare to senator[1] to prevent guessing of the revealed name
               score += 1
               print('Correct! Score:{0}'.format(score))
            else:
               score -= 1
               print('Incorrect! Score:{0}'.format(score))
            print("The Senators from {0} are {1} and {2}".format(state.title(), senator[0][0:-3], senator[1][0:-3])) 
            
         again = int(input("Play again?\n1)Yes\n0)No\n")) 
         
      return;
      
   def senGame():
   
      return;
      
   def partyGame():
    
      return;
      
   selection = 4
   while selection >= 0:
      selection = int(input("Please pick a game!\n0)States' Senators\n1)Quit\n"))#\n1)Senators' States\n2)Senators' Parties\n3)Quit\n"))
       
      if selection == 0:
         stateGame()
      if selection == 1:
         selection = -1
      if selection == 2:
         partyGame()
      if selection == 3:
         selection = -1
      
   return;
   
      
runagain = 1
mode = -1
while runagain==1:
   database = createDict()
   
   mode = int(input("Welcome to the State Senators Database(tm)! Please select a mode!\n0)State lookup\n1)Senator Lookup\n2)Party Lookup\n3)Games\n4)Quit\n"))
         
   if mode == 0:
      stateMode()
                          
   if mode == 1:
      senMode()
      
   if mode == 2:
      partyMode()
      
   if mode == 3:
      gameMode()
         
   if mode == 4:
      runagain = 0
      print("Thank you for using the State Senators Database(tm)! Goodbye!")
 
   
         
         
     
     
