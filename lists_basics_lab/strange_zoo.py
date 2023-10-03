#You are at the zoo, and the meerkats look strange.
#You will receive 3 strings on separate lines, representing the tail,
# the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
#    • On the first position is the head;
#    • On the second position is the body;
#    • On the last one is the tail.
animal = []
for i in range(3):
    part_of_body = input()
    animal.append(part_of_body)
animal.reverse()
print(animal)