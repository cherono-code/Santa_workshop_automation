import time

print("HO HO HO, Welcome to Santa's Workshop!!!")
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")


class GetsantasList:
    def __init__(self):
        self.santas_db = {}
        self.elf_production_db = {}
#creating liist for santa
    def santas_list(self):
        while True:
            #taking the list of kids from the letters they wrote for Santa
            kid_name = input("Child's Name: ").lower()
            behavior = input("Child's Behavior: ").lower()
            toy = input("Child's Toy: ").lower()
            city = input("City: ").lower()

            #add the child with good behavior in the new db
            self.santas_db[kid_name] = {'behavior': behavior, 'toy': toy, 'city': city}
            
            #adding more kiids to santa's db
            another_child = input("Add another child? (yes/no): ").lower()
            if another_child != 'yes':
                break
        #santa's list
        print("Santa's list for production: ", self.santas_db, end="")

        self.elf_production_db = self.production_db(self.santas_db)
        return self.santas_db
    #new db with good kids
    def production_db(self, santas_db):
        elf_production_db = {}
        
        for kid_name, data in santas_db.items():
            behavior = data['behavior']
            toy = data['toy']
            city = data['city']
            print("\n")
        #filtering out the good kids and adding them to the production 
            if behavior == 'good':
                print(f"{kid_name} has been {behavior} and gets a {toy} from Santa...")

                #new database for santa
                elf_production_db[kid_name] = {'toy': toy, 'city' : city}
            else:
                print(f"Sorry, {kid_name} has been {behavior}. No gift from Santa for {kid_name}...")
        print("\n")

        print("Elves' Production database: ", elf_production_db)
        return elf_production_db

class ToyProductionManager:
    def acquire_production_list(self, elf_production_db):
        self.elf_production_db = elf_production_db
    #toy production process
    def produce_toys(self):
        for kid_name, toy in self.elf_production_db.items():
            print(f"{kid_name}'s {toy['toy']} is in the factory and being produced...")
            time.sleep(2)
            print(f"Painting {kid_name}'s {toy['toy']} in festive colors...")
            time.sleep(2)
            print(f"Wrapping {kid_name}'s {toy['toy']} with holiday cheer...")
            time.sleep(2)
            print(f"{kid_name}'s {toy['toy']} is ready for delivery...")
        print("\n")
#santa's delivery
class SleighSantaGiftDelivery:
    def __init__(self):
        self.toys_delivered_db = {}

    def toys_delivered_database(self, elf_production_db):
        for kid_name, data in elf_production_db.items():
            city = data['city']
            toy = data['toy']

            # Check if the city is already in the delivered database
            if city not in self.toys_delivered_db:
                self.toys_delivered_db[city] = {'kids': []}

            # Add the delivered toy information
            self.toys_delivered_db[city]['kids'].append({'kid_name': kid_name, 'toy': toy})

    def display_toys_delivered(self):
        for city, data in self.toys_delivered_db.items():
            print("Santa is delivering the gift....")
            time.sleep(3)
            print("Santa is almost done....")
            time.sleep(3)
            print(f"Santa has delivered gifts in {city} to the following kids:")
            for kid_info in data['kids']:
                print(f"{kid_info['kid_name']}'s gift: {kid_info['toy']}")
            print("\n")


if __name__ == "__main__":
    # instance of GetSantasList
    santas_list_instance = GetsantasList()
    santas_list_instance.santas_list()

    # instance of ToyProductionManager
    toy_manager_instance = ToyProductionManager()
    toy_manager_instance.acquire_production_list(santas_list_instance.elf_production_db)
    toy_manager_instance.produce_toys()

    # instance of sleigh
    sleigh_instance = SleighSantaGiftDelivery()
    sleigh_instance.toys_delivered_database(toy_manager_instance.elf_production_db)
    sleigh_instance.display_toys_delivered()
