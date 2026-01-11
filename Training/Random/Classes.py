class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def feed_dog(self):
        print("feeding dog", self.name)


dog1 = dog("milo", "German")
dog2 = dog("Marty", "Collie")

print("dog 1 name", dog1.name)
print("dog 2 name", dog2.name)


dog1.feed_dog()
dog2.feed_dog()


