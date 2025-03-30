##Project1: Generate random names



# Import necessary libraries
import random
import csv
import names

# Create word concatenation of consonant and vowels letters
Vowels = ["A", "E", "I", "O", "U"]
Cons = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

def builtword():  
    randomNumber = random.randint(2, 4)
    name = ""  # Fixed the issue (removed leading space)
    for _ in range(randomNumber):
        randomVowels = random.choice(Vowels)
        randomCons = random.choice(Cons)
        name += randomVowels + randomCons
    return name

print(builtword())

# Store the built word in a CSV file  
def writeTocsv():
    with open("names.csv", "a", newline="") as file:  # Changed to append mode
        writer = csv.writer(file)
        name = builtword()
        writer.writerow([name])

writeTocsv()

# Generate random names
def generate_random_name(gender=None):
    """
    Generates a random full name based on specified gender.
    """
    if gender:
        return names.get_full_name(gender=gender)
    return names.get_full_name()

def save_names_to_file(filename, num_names):
    """
    Generates random names and saves them to a file.
    """
    with open(filename, "w") as file:
        for _ in range(num_names):
            name = generate_random_name()
            file.write(name + "\n")

def fantasy_name_generator():
    """
    Generates a random full name with fantasy-themed title and suffix.
    """
    fantasy_titles = ["Lord", "Lady", "High Mage", "Knight", "Enchantress", "Archdruid"]
    fantasy_suffixes = ["of the Silverwood", "the Magnificent", "Stormbringer", "the Eternal"]

    title = random.choice(fantasy_titles)
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    suffix = random.choice(fantasy_suffixes)

    return f"{title} {first_name} {last_name} {suffix}"

def generate_random_surname():
    """
    Generates a random fantasy-themed surname.
    """
    fantasy_surnames = ["Darkbrand", "Silverwood", "Stormweaver", "Moonshadow", "Fireforge"]
    return random.choice(fantasy_surnames)

def save_surnames_to_file(filename, num_surnames):
    """
    Generates random surnames and saves them to a file.
    """
    with open(filename, "w") as file:
        for _ in range(num_surnames):
            surname = generate_random_surname()
            file.write(surname + "\n")

# Main execution
if __name__ == "__main__":
    # Save fantasy names
    save_names_to_file("fantasy_names.txt", 10)
    save_surnames_to_file("fantasy_surnames.txt", 10)
    print("Fantasy names and surnames saved successfully.")
