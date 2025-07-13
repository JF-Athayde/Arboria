import plants

class User:
    def __init__(self, username):
        self.name = username
        self.plants = []

    def generate_new_plant(self, max_bounds=10, automatic=False, cutoff_ovr=0, inc=5):
        plant = plants.Plant()
        plant.build_names()
        plant.build_numbers_attributs(max_bounds=max_bounds, inc=inc)
        ovr = plant.overall()

        if not automatic:
            print('Overall:', ovr)
            inp = input('you would like to save? (Y or N)')
            inp.lower()

            if inp == 'y':
                plant.display()
                self.plants.append(plant)
                print('Saved!')
        
        if automatic and ovr >= cutoff_ovr:
            plant.display()
            self.plants.append(plant)
            print('Saved!')
        
        return ovr
    
    def multi_generate_plants(self, max_bounds=10, epochs=10, inc=5):
        record = -1
        for _ in range(epochs):
            ovr = self.generate_new_plant(max_bounds=max_bounds, automatic=True, cutoff_ovr=record, inc=inc)
            if ovr >= record:
                record = ovr
        
        if epochs == 0:
            record = -1
            while True:
                ovr = self.generate_new_plant(max_bounds=max_bounds, automatic=True, cutoff_ovr=record, inc=inc)
                if ovr >= record:
                    record = ovr
        
user = User('Jf')
user.multi_generate_plants(max_bounds=10, epochs=0, inc=10)