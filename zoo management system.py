class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.species},{self.age} years old)"


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} - {self.role}"


class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        return [str(animal) for animal in self.animals]


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []
        self.enclosures = []

    def add_animal(self, name, species, age):
        animal = Animal(name, species, age)
        self.animals.append(animal)
        print(f"Added animal: {animal}")

    def add_staff(self, name, role):
        member = Staff(name, role)
        self.staff.append(member)
        print(f"Added staff: {member}")

    def create_enclosure(self, name):
        enclosure = Enclosure(name)
        self.enclosures.append(enclosure)
        print(f"Created enclosure: {name}")

    def assign_animal_to_enclosure(self, animal_name, enclosure_name):
        animal = next((a for a in self.animals if a.name == animal_name), None)
        enclosure = next((e for e in self.enclosures if e.name == enclosure_name), None)

        if animal and enclosure:
            enclosure.add_animal(animal)
            print(f"Assigned {animal.name} to {enclosure.name}")
        else:
            print("Animal or enclosure not found.")

    def list_all_animals(self):
        print("All Animals in Zoo:")
        for animal in self.animals:
            print(f" - {animal}")

    def list_all_staff(self):
        print("All Staff:")
        for member in self.staff:
            print(f" - {member}")

    def list_all_enclosures(self):
        for enclosure in self.enclosures:u
            print(f"{enclosure.name}:")
            for animal in enclosure.list_animals():
                print(f"   - {animal}")

# Simulated user database (for now, hardcoded)
users = {
    "admin": {"password": "zooadmin", "role": "admin"},
    "swathi": {"password": "zoozee", "role": "staff"}
}

def login():
    print("=== Zoo Management Login ===")
    username = input("Username: ")
    password = input("Password: ")

    user = users.get(username)
    if user and user["password"] == password:
        print(f"Login successful! Welcome, {username} ({user['role']})")
        return user["role"]
    else:
        print("Invalid credentials. Try again.")
        return None


# Sample CLI
def main():
    role = None
    while not role:
        role = login()
        
    zoo = Zoo()

    while True:
        print("\nZoo Management System")
        print("1. Add Animal")
        print("2. Add Staff")
        print("3. Create Enclosure")
        print("4. Assign Animal to Enclosure")
        print("5. List Animals")
        print("6. List Staff")
        print("7. List Enclosures")
        print("8. Exit")

        choice = input("Enter your choice(in numbers): ")
        
        if role != "admin" and choice in ['2', '3']:
            print("Access denied. Only admins can perform this action.")
            continue

        if choice == '1':
            name = input("Animal Name: ")
            species = input("Species(mammals/fish/birds/reptiles/amphibians): ")
            age = int(input("Age: "))
            zoo.add_animal(name, species, age)
        elif choice == '2':
            name = input("Staff Name: ")
            role = input("Role: ")
            zoo.add_staff(name, role)
        elif choice == '3':
            name = input("Enclosure Name: ")
            zoo.create_enclosure(name)
        elif choice == '4':
            animal_name = input("Animal Name: ")
            enclosure_name = input("Enclosure Name: ")
            zoo.assign_animal_to_enclosure(animal_name, enclosure_name)
        elif choice == '5':
            zoo.list_all_animals()
        elif choice == '6':
            zoo.list_all_staff()
        elif choice == '7':
            zoo.list_all_enclosures()
        elif choice == '8':
            print("Exiting Zoo Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
