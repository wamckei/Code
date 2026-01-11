# Polymorphism enables the same method name to produce different behaviors based on the object type, 
# often via inheritance or duck typing. Python relies on duck typing—if it walks like a duck and quacks like a duck, 
# treat it as a duck—rather than strict interfaces. This supports runtime decisions without explicit type checks

class dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def feed_dog(self):
        print("feeding dog", self.name)


class color(dog):
    pass

class size(dog):
    pass

dog1 = color("milo", "German")
dog2 = size("Marty", "collie")


dog1.feed_dog()
dog2.feed_dog()
