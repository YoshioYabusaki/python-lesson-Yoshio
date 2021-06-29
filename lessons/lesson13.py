class Dog: # クラス　抽象の概念
    name = ""
    age = 0
    weight = 0
    breed = ""
    image_path = "/path/to/image"

# クラスの例　具体的な情報
my_dog = Dog()
my_dog.name = "Ted"
my_dog.age = 1
my_dog.weight = 18
my_dog.breed = "French buldog"
my_dog.image_path = "ted.png"
print(my_dog.image_path)

# print(my_dog.name, my_dog.age, my_dog.breed)

neighbor_dog = Dog()
neighbor_dog.name = "Arch"
print((neighbor_dog.image_path))
# print(neighbor_dog.name)










