#for Inheritence
import time
import os

class Pet:
    def __init__(self,name):
        self.name = name
        self.food = 0
        self.love = 0
        self.happiness = 0 #for happiness meter
        self.alive = True #for alive or dead

    def introduce(self):
        print(f"Hello. I am {self.name} and your virtual pet")

    def feed(self):
        while True:
            feed = input("Will you feed me hooman y/n:  ").strip() .lower()
            if feed != 'y':
                print("Okkk hooman.. may be later")
                break
        
            feed= input("You can feed me 1. Pizza🍕 2. Sushi🍣 3. Croissant🥐 and 4. Bubble Tea🧋  ").strip()
            if feed == '1':
                print("Yayyyy.. You feed me pizza🍕")
                self.food += 30

            elif feed == '2':
                print("Yayyyy.. You feed me sushi🍣")
                self.food += 30
            elif feed == '3':
                print("Yayyyy.. You feed me Croissant🥐")
                self.food += 20
            elif feed == '4': 
                print("Yayyyy.. Bubble tea is delicious🧋")
                self.food += 15
            else:
                print("That's not in the menu")
    
    def pet(self):
        
        while True:
            feed = input("Will you pet me hooman🥺 y/n:  ").strip() .lower()
            if feed != 'y':
                print("Okkk hooman.. may be later")
                break
            else:
                print ("Happi❤️")
                self.love += 10
          
    def decay(self):
        self.food = max(0,self.food - 5)
        self.love = max(0,self.love - 2)
        self.love = max(0,self.food - 1)

    def about(self):
        print(f"Name: {self.name}")
        print(f"Happiness: {self.happiness}%")
        print(f"Energy: {self.food}%")
        print(f"Love: {self.love}%")
        if self.food <= 15:
            print ("I'm about to die. Feed me more🥺")
        elif self.food >=20 or self.food <150:
            print ("I'm ok hooman but still hungry")
        else:
            print("Full energy")

class Dog(Pet):
    def make_sound(self):
        print("Woof")
    
    def fetch(self):
        while True:
            play = input("Will you play with me hooman y/n:  ").strip() .lower()
            if play != 'y':
                print("Okkk hooman.. may be later")
                break
            print("fetching the ball...⚽")
            self.happiness +=10

class Cat(Pet):
    def make_sound(self):
        print("Meow")
    
    def nap(self):
        while True:
            nap = input("Will you let me nap y/n:  ").strip() .lower()
            if nap != 'y':
                print("Okkk hooman.. may be later")
                break
            print("Purrrr....😸😴")
            self.happiness +=10

        

class Penguin(Pet):
    def slide(self):
        while True:
            slide = input("Let's slide on the ice! y/n:  ").strip() .lower()
            if slide != 'y':
                print("Okkk hooman.. may be later")
                break
            print("🐧Wheee! I'm sliding on the ice⛸️")
            self.happiness +=10
#Game setup
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Choose your virtual pet:")
print("1. Penguin 🐧")
print("2. Dog 🐶")
print("3. Cat 🐱")
pet_choice = input("Enter your pet (1/2/3): ").strip()

if pet_choice == '1':
    name = input("Name your penguin: ")
    pet = Penguin(name)
elif pet_choice == '2':
    name = input("Name your dog: ")
    pet = Dog(name)
elif pet_choice == '3':
    name = input("Name your cat: ")
    pet = Cat(name)
else:
    print("Invalid choice. Defaulting to Cat named Tom.")
    pet = Cat("Tom")
# Game loop
pet.introduce()
while True:
    pet.decay()
    print("\nWhat would you like to do?")
    print("1. Feed 🍽️")
    print("2. Pet 🥰")
    if isinstance(pet, Dog):
        print("3. Play Fetch ⚽")
    elif isinstance(Pet, Cat):
        print("3. Nap 😴")
    elif isinstance(Pet, Penguin):
        print("3. Slide ❄️")
    print("4. View Current State ")
    print("5. Exit 🚪")

    action = input("Choose an action (1-5): ").strip()

    if action == '1':
        pet.feed()
    elif action == '2':
        pet.pet()
    elif action == '3':
        if isinstance(pet, Dog):
            pet.fetch()
        elif isinstance(Pet, Cat):
            pet.nap()
        elif isinstance(Pet, Penguin):
            pet.slide()
    elif action == '4':
        pet.about()
    elif action == '5':
        print(f"Goodbye! {pet.name} will miss you 💔")
        break
    else:
        print("Invalid action.")

    time.sleep(2)
    clear()
