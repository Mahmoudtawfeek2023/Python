items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list!")
for item in items_on_sale:
  if item == "knit dress":
    break
print("End of Search! No need to full list scanning")

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        break
print("They have the dog I want!")