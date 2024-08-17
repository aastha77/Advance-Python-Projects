#!/usr/bin/env python
# coding: utf-8

# # Advance python

# # 1.Importing Package:

# In[1]:


import random
import csv
import names


# In[2]:


#create word concatenation of consonant  and vowels letters
Vowels=["A","E","I","O","U"]
Cons=["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"]
def builtword():  
    randomNumber=random.randint(2,4)
    name=" "
    for _ in range(randomNumber):
        randomVowels=random.choice(Vowels)
        randomCons=random.choice(Cons)
        name=name+randomVowels+randomCons
    return name
print(builtword())


# In[3]:


#store the buitword function  in csv file  
def writeTocsv():
    with open("names.csv","w") as file:
        writer=csv.writer(file)
        name=builtword()
        writer.writerow([name])
writeTocsv()


# # 2.1. Generate Random Names:

# In[4]:


#using names package function 
names.get_full_name() #get random full_names


# In[5]:


names.get_first_name() #get random first_name


# In[6]:


names.get_last_name()  #get random last_names


# In[9]:


#generate random first_name in range using for loop
for i in range(0,5):
    print(names.get_first_name())


# In[10]:


#generate random last_name in range
for i in range(0,5):
    print(names.get_last_name())


# In[11]:


#genrate random full_names in range
for i in range(0,10):
    print(names.get_full_name())


# In[34]:


full_name=[] #store names in the list
for i in range(10):
    temp=names.get_full_name()
    full_name.append(temp)
print(full_name)


# # 2.2 Create a function that generates random names based on specified criteria (e.g., gender).

# In[12]:


def generate_random_name(gender=None):
    """
    Generates a random full name based on specified gender.
    """
    if gender:
        return names.get_full_name(gender=gender)
    else:
        return names.get_full_name()

def main():
    num_names = 15 # Change this to the desired number of names

    # Generate and print random names
    for _ in range(num_names):
        print(generate_random_name())

if __name__ == "__main__":
    main()


# In[15]:


def save_names_to_file(filename, num_names):
    """
    Generates random names and saves them to a file.
    """
    with open(filename, "w") as file:
        for _ in range(num_names):
            name = generate_random_name()
            file.write(name + "\n")

def main():
    num_names = 20  # Change this to the desired number of names
    output_filename = "random_names.txt"  # Specify the output filename

    save_names_to_file(output_filename, num_names)
    print(f"Generated names saved to : {output_filename}")

if __name__ == "__main__":
    main()


# # 3.Fantasy-Themed Names:

# Define a list of fantasy titles (e.g., “Lord,” “Lady,” “High Mage”) and suffixes (e.g., “of the Silverwood,” “the Magnificent”).
# Combine these elements creatively with first names and last names.

# In[14]:


def generate_random_name(gender=None):
    """
    Generates a random full name with fantasy-themed title and suffix.
    """
    fantasy_titles = [
        "Lord", "Lady", "High Mage", "Knight", "Enchantress", "Archdruid"
    ]
    fantasy_suffixes = [
        "of the Silverwood", "the Magnificent", "Stormbringer", "the Eternal"
    ]

    title = random.choice(fantasy_titles)
    first_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()
    suffix = random.choice(fantasy_suffixes)

    full_name = f"{title} {first_name} {last_name} {suffix}"
    return full_name.strip()

def main():
    num_names = 10  

    # Generate and print random fantasy-themed names
    for _ in range(num_names):
        print(generate_random_name())

if __name__ == "__main__":
    main()


# # 4.Save Names to a File:

# using the with open(filename, "w") syntax to write names to a file.

# In[16]:


def save_names_to_file(filename, num_names):
    """
    Generates random names and saves them to a file.
    """
    with open(filename, "w") as file:
        for _ in range(num_names):
            name = generate_random_name()
            file.write(name + "\n")

def main():
    num_names = 10  # Change this to the desired number of names
    output_filename = "fantasy_names.txt"  # Specify the output filename

    save_names_to_file(output_filename, num_names)
    print(f"Generated names saved to {output_filename}")

if __name__ == "__main__":
    main()


# # 5. Genrate Random Surnames and save surnames to a file:

# In[17]:


def generate_random_surname():
    """
    Generates a random fantasy-themed surname.
    """
    fantasy_surnames = [
        "Darkbrand", "Silverwood", "Stormweaver", "Moonshadow", "Fireforge"
    ]
    return random.choice(fantasy_surnames)

def save_surnames_to_file(filename, num_surnames):
    """
    Generates random surnames and saves them to a file.
    """
    with open(filename, "w") as file:
        for _ in range(num_surnames):
            surname = generate_random_surname()
            file.write(surname + "\n")

def main():
    num_surnames = 10  # Change this to the desired number of surnames
    output_filename = "fantasy_surnames.txt"  # Specify the output filename

    save_surnames_to_file(output_filename, num_surnames)
    print(f"Generated surnames saved to {output_filename}")

if __name__ == "__main__":
    main()


# In[ ]:




