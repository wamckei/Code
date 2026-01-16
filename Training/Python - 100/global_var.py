# Modify global scope

enemies = 1

# It's not best practices to modify global variables locally, instead use the method in the next code block 
def increase_enemies():
    global enemies  # Without this statement you can not modify or reference gloab variables with in a local scope
    enemies += 1
    print(f"Enemies inside of function: {enemies}")


increase_enemies()
print(f"Enemies outside of functions: {enemies}")

# prefered method to modify a global var in a local scope
enemies = 1

# It's not best practices to modify global variables locally, instead use the method in the next code block 
def increase_enemies(enemy):
    print(f"Enemies inside of function: {enemy}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"Enemies outside of functions: {enemies}")

# Global Constants - defined in all upper case, ex. 
PI = 3.14159
GOOGLE_URL = "https://www.google.com"
