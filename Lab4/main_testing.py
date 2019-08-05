import main
import turtle

print("==== Menu ==== ")
print("[1] banana")
print("[2] mario")
print("[3] ghost")
print("[4] alien")
print("[5] mushroom")
print("[6] lmao")
print("[7] pichu")
print("[8] agumon\n")
print("TYPE IN NAME OF IMAGE")
user_choice = input("Art File Location: ")
insert = 'art/'+ user_choice + '.txt'

def art_loader(insert):
    pallet, pixels = main.load_art(insert)
    print(pallet)
    print(pixels)

def art_drawer(insert):
    pallet, pixels = main.load_art(insert)
    main.draw(pallet, pixels)
    turtle.done()

print("==== Test Options ====")
print("[1] Loading")
print("[2] Draw")
print("TYPE IN OPTION NUMBER")
user_command = eval(input("Which one do you want to test?"))
if user_command == 1:
    art_loader(insert)
if user_command == 2:
    art_drawer(insert)
