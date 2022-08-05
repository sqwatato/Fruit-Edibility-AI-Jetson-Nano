# Faster way to choose which fruits go where

#Categories
like = []
hate = []
new = []

choice = 0
file = []
with open("labels.txt", "r") as f:
    file = f.readlines()


for fruit in list(map(str.strip, file)):
    choice = 0
    while choice not in ['1','2','3']:
        choice = input(f"Do you like(1), hate(2) or never tried(3) a {fruit}: ")
        
        if choice == '1':
            like.append(fruit)
        elif choice == '2':
            hate.append(fruit)
        elif choice == '3':
            new.append(fruit)
        

print("Liked Fruits: ", like)
print("Hated Fruits: ", hate)
print("New Fruits: ", new)


