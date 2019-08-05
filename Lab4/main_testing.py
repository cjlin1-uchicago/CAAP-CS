import main

print("==== Menu ==== ")
print("[1] BANANA")
print("[2] MARIO")
print("[3] GHOST")
print("[4] ALIEN")
print("[5] MUSHROOM")
print("[6] LMAO")
print("[7] PICHU")
print("[8] AGUMON")
choice = eval(input("Type in picture number: "))
if choice == 1:
    insert = 'art/banana.txt'
elif choice == 2:
    insert = 'art/mario.txt'
elif choice == 3:
    insert = 'art/ghost.txt'
elif choice == 4:
    insert = 'art/alien.txt'
elif choice == 5:
    insert = 'art/mushroom.txt'
elif choice == 6: 
    insert = 'art/lmao.txt'
elif choice == 7:
    insert = 'art/pichu.txt'
else:
    insert = 'art/agumon.txt'


pallet, pixels = main.load_art(insert)

main.draw(pallet, pixels)
