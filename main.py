import random

class Star:
    def __init__(self, initial_mass,star_name):
        self.star_name = star_name
        self.initial_mass = initial_mass
        self.current_mass = initial_mass
        self.age = 0
        self.stage = "Main Sequence"
        self.is_alive = True
        self.die = ""
    
    def evolve(self):
        """Simulate star evolution based on initial mass"""
        # Increase age
        self.age += 1
        
        # Mass loss mechanism this equation is wrong
        mass_loss_rate = 0.001 * (self.initial_mass ** 0.5)
        self.current_mass -= mass_loss_rate
        
        # Track stages
        
        
        # Determine star stages and potential death scenarios
        if self.current_mass <= 0:
            self.is_alive = False
            self.die = "Complete Mass Dissipation"
            self.stage = "After death"
            


    def display(self):
        print(self.star_name)
        print(self.initial_mass)
        print(self.current_mass)
        print(self.age)    
        print(self.stage)
        print(self.is_alive)
        print(self.die)
    


def main():
    # Run simulation
    star1 = Star(7,"TR HYPOTHESIS - 1")
    for i in range(12000):
        star1.evolve()
    star1.display()
    
    
    

if __name__ == "__main__":
    main()
