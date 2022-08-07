flag=0
found=1
c=0

while(flag==0 and found==1):
 if(c<1): #for first move of the game
  list = ["tiger","rhinoceroses","snake","dolphin","nilgai","elephant","turtle"] #list of animals
  user=input("enter animal name:")                           #taking input from user 1st time in game
  if(user in list):                                          #if user input in list
   luser=len(user)                                           #length of user input
   k=user[luser-1]
   list.remove(user)                                         #removing from list so that can't be repeated
#    print(list)
  else:                                                      
      flag=1                                                 #if user input not in list break pc won
      break

  for r in list:
      if(r[0]==k):                                      #if any item in list starts with last alphabet of user input
          found=1                                       #found item
          pc=r
          list.remove(pc)                               #removing from list so that can't be repeated
          lpc=len(pc)
          q=pc[lpc-1]                                   #finding last alphabet of pc output generated
          break
      else:
          found=0                                       #not found user won

  print(pc)
#   print(list)
  c=c+1                                                 #for next steps to play user input must be taken unlike first time

 else:
     user=input("enter animal name:")
     for r in list:
         if(user==r):

          if(user[0]==q):
              luser=len(user)
              k=user[luser-1]
              list.remove(user)
              print(list)
              flag=0
              break
         else:
             flag=1
     if(flag==1):
         break        
     for r in list:
      if(r[0]==k):
          found=1
          pc=r
          list.remove(pc)
          lpc=len(pc)
          q=pc[lpc-1]
          break
      else:
          found=0

     print(pc)
     print(list)        

if(flag==1 and found==1):           #if user input not correct
    print("You lost never mind")
elif(found==0 and flag==0):         #if output not found by pc
    print("You won congratulations madam")