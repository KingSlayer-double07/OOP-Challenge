from pet import *

# Create a pet instance
my_pet = Pet("Aidan")

# Check initial status
print("Initial Status:")
my_pet.get_status()
print()

# Feed the pet
print("Feeding the pet...")
my_pet.eat()
my_pet.get_status()
print()

# Let the pet sleep
print("Letting the pet sleep...")
my_pet.sleep()
my_pet.get_status()
print()

# Play with the pet
print("Playing with the pet...")
my_pet.play()
my_pet.get_status()
print()

# Teach the pet a new trick
print("Training the pet...")
my_pet.train("roll over")
my_pet.train("sit")
my_pet.train("roll over")  # Trying a duplicate
print()

# Show all learned tricks
print("Learned Tricks:")
my_pet.show_tricks()
