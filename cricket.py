import random
l=[0,1,7,2,4,6,8,1,4,2,0,10,6,4,6,9,7,8,"wide"]
runs=0
t=[27,37,50,55,73,100]
target=random.choice(t)
n=int(input("\nEnter choice\n1)batting\n2)bowling\n->"))
tw=10
w=1
if n==1:
 print(f"\n[Target score is:{target}]\n")
 while w<11:
  print(f"->[ Wickets left: {tw-(w-1)} ]<-\n")
  d=random.choice(l)
  i=input("Enter 'bt' to bat:")
  if i=='bt':
   print("Bowling is done!\n")
   if d in l and d!=7 and d!=8 and d!=9 and d!=10:
     if d=='wide':
      print("wide")
      wide=1
      d=wide 
     print("You hit!!\n") 
     print("->",d)
     print(f"\nYou got {d} runs.\n")
     runs=runs+d
     print(f"->[ Current Score: {runs} ]<-\n")
     if runs>target and runs<=target+6:
      print(f"Target is:{target}\n")
      print(f"You scored {runs} runs\n")
      print("You won the match by",tw-(w-1),"wickets!\n","","\nSo they lost the match.")
      print("\n.......Game over.......")
      exit()
   else:
     if d==7:
       print("Bold......")
     elif d==8:
       print("Catch out......")
     elif d==9:
       print("lbw out......")
     elif d==10:
       print("Run out......")
     print("\nYou got out!")
     print("\nYou lose one wicket\n")
     print(f"->[ Current Score: {runs} ]<-\n")
     w+=1
  else:
   print("Enter only 'bt' to start batting.")
   exit()
 print("Target =",target,"\n")
 if runs<target:
  print("\nAll Out!!\n")
  print("<<<","Total runs you scored is only :",runs,">>>\n")
  print("So you lost the game..\n","\nThey won the match by",target-runs,"runs.\n")
  print(".......Game over.......")
 elif runs==target:
  print("<<<","Total runs you scored is:",runs,">>>\n")
  print("Match draw!!\n")
  print(".......Game over.......")
 else:
  print("<<<","Total runs you scored is:",runs,">>>\n")
  print("You won the match by",tw-(w-1),"wickets!\n","","\nSo they lost the match.")
 print("\n.......Game over.......")
 if runs==0 and tw==10:
  print("Your score is zero!!!!\n")
elif n==2:
 print(f"\n[Target score is:{target}]\n")
 while w<11:
  print(f"->[ Wickets left: {tw-(w-1)} ]<-\n")
  d=random.choice(l)
  i=input("Enter 'bl' to bowl:")
  if i=='bl':
   print("Batting is done by opposite team!\n")
   if d in l and d!=7 and d!=8 and d!=9 and d!=10:
     if d=='wide':
      print("wide")
      wide=1
      d=wide 
     print("They hit!!\n") 
     print("->",d)
     print(f"\nThey got {d} runs.\n")
     runs=runs+d
     print(f"->[ Current Score:{runs} ]<-\n")
     if runs>target and runs<=target+6:
      print(f"Target is:{target}\n")
      print(f"They scored {runs} runs\n")
      print("They won the match by",tw-(w-1),"wickets!\n","","\nSo you lost the match.")
      print("\n.......Game over.......")
      exit()
   else:
     if d==7:
       print("Bold......")
     elif d==8:
       print("Catch out......")
     elif d==9:
       print("lbw out......")
     elif d==10:
       print("Run out......")
     print("\nThey got out!")
     print("\nThey lose one wicket\n")
     print(f"->[ Current Score: {runs} ]<-\n")
     w+=1
  else:
   print("Enter only 'bl' to start bowling.")
   exit()
 print("Target =",target,"\n")
 if runs<target:
  print("\nAll Out!!\n")
  print("<<<","Total runs They scored is only :",runs,">>>\n")
  print("So They lost the game..\n","\nYou won the match by",target-runs,"runs.\n")
  print(".......Game over.......")
  exit()
 elif runs==target:
  print("<<<","Total runs They scored is:",runs,">>>\n")
  print("Match draw!!\n")
  print(".......Game over.......")
 else:
  print("<<<","Total runs They scored is:",runs,">>>\n")
  print("They won the match by",tw-(w-1),"wickets!","\nSo you lost the match.")
 print("\n.......Game over.......")
 if runs==0 and tw==10:
  print("Their score is zero!!!!\n")
else:
 print("Enter only 1 or 2 _ 1 for batting and 2 for bowling! ")

 
 