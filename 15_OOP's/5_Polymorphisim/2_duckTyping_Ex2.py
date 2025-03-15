def PetLover(pet):

    pet.talk()

    if hasattr(pet, "walk"):
        pet.walk()


class Duck:
    def talk(self):
        print("Duck is talking")

    def walk(self):
        print("Duck is walking")


class Dog:
    def talk(self):
        print("Dog is talking")


d1 = Duck()
PetLover(d1)

# Duck is talking
# Duck is walking

print()

dg1 = Dog()
PetLover(dg1)

"""
When we run this dg1 object we'll be getting an error:

🔸 AttributeError: 'Dog' object has no attribute 'walk'. Did you mean: 'talk'?

🔸 To avoid this error we'll inserting an conditon in our PetLover() function.
"""

# Now after putting condition in our function we received this proper output " Dog is talking  "
