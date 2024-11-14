l=[]
l1=[['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],['1','2','3','4','5','6','7','8','9'],['🍓','🍊','🍍','🍎','🍉'],['🍅','🍆','🥕','🥔','🫑'],
['😊','🥳','🙁','🥺','😠','😮','😴','🙁','😊'],['🌲','🌳','🌴','🪵','🌿'],['🐶','🐱','🐰','🐬','🐴'],['🍔','🍟','🍕','🎂','🍧'],['🏸','🏑','🏏','🏹','⚽'],['🚙','🚌','🏍','✈','🚅'] ]
print("\n*****FILL THE LIST BOX-l->[] GAME*****\n")
for ls in l1:
  print(ls)
  print()
names=['Alphabets','Numbers','Fruits','Vegetables','Emojis','Trees','Animals','Food','Games','Vechciles']
print(f"\nYou have different types of lists above {names} ")
print("\nYou have to store different types of elements in the LIST BOX-L->[] from different types of lists to win this game...")
print("\nEmpty LIST-BOX-L is there below :\n\n__________LIST BOX-L->[]__________\n")
from random import choice as ch
r1,r2,r3,r4,r5,r6,r7,r8,r9,r10=ch(l1[0]),ch(l1[1]),ch(l1[2]),ch(l1[3]),ch(l1[4]),ch(l1[5]),ch(l1[6]),ch(l1[7]),ch(l1[8]),ch(l1[9])
print("\n-ENTER WHAT TYPE OF LEVEL YOU WANT TO PLAY.\n\n1)Easy level-(5 elements are to be stored in 7-chances!)\n\n2)Medium level-(7 elements are to be stored in 11-chances!)\n\n3)Hard level-(9 elements are to be stored in 15-chances!)")
n1=0
while n1==0:
  n=input("Enter choice:")
  if n=='1' or n=='2' or n=='3':
    n1=1
  else:
    print("Invalid choice!\n")
    n1=0
chance=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,17]
choose=[1,2,3]
store=[5,7,9]
tc=[7,11,15]
levels=['Easy','Medium','Hard']
r=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
def game(n2,chance,choose,levels,store,r):
 names=['Alphabets','Numbers','Fruits','Vegetables','Emojis','Trees','Animals','Food','Games','Vechciles']
 chc=tc[(int(n2)-1)]
 i=0
 if int(n2)==choose[int(n2)-1]:
    print(f"\nYou have choosen {levels[int(n2)-1]} level! So you will get {chc} chances to play this game in {levels[int(n2)-1]} level . \n\nYou will have to store {store[int(n2)-1]} differnt types of elements from any of the 10 lists given in the beginning of the game ,to win this game")
    print("\nNOTE: From each list only 1 element is taken (for ex: if you got an element from vegetables further if you again get an elment from vegetables list that element willnot be taken to store in the LIST BOX-L->[])")
    while chc>0:
      print(f"\n[ Chances left are {chc} ]")
      z=input(f"\n\n~ Enter {chance[i]} to get an element in {chance[i]} st/nd/rd/th chance: ")
      if z==str(chance[i]):
       pt=ch(r)
       ind=r.index(pt)
       print(f"\n-->You got an element {pt} from -->{[names[ind]]}<-- list")
       c=0
       for j in l:
         if j in l1[ind]:
           c+=1
       if c==0:  
         l.append(pt)
         print(f"\n-->You stored an element {[pt]} in the LIST BOX-L->[]")
         print(f"\n\n            __________LIST BOX-L : {l}__________\n\n")
         i+=1
         chc-=1
         if len(l)==store[int(n2)-1]:
           print(f"\n[ Chances left are {chc} ]\n")
           print(f"You stored {store[int(n2)-1]} differnt elements in the LIST BOX-l->[] : {l}.\n\n*****YOU WON THE GAME*****")
           print("\n..........GAME OVER..........")
           exit()
       else:
           print(f"\n-->You cannot store the element {pt} from -->{[names[ind]]}<-- as an element from the -->{[names[ind]]}<-- list is already prsent!")
           print(f" \n\n           __________LIST BOX-L : {l}__________\n\n")
           i+=1
           chc-=1
      else:
        print(f"\nInvalid! press only {chance[i]} to get an element.....")
    if chc==0:
       print(f"\n[ Chances left are {chc} ]")
       print(f"\n\nYou could'nt store {store[int(n2)-1]} differnt elements in the LIST BOX-L->[] in given chances!\nYou could store only {len(l)} elements in the LIST BOX-l->[]:{l}")
       print("\n<<<< YOU LOST THE GAME >>>>")
       print("\n..........GAME OVER..........")
game(n,chance,choose,levels,store,r)