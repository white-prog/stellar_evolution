import random
#import matplotlib.pyplot as plt

class Star:
    def __init__(self, initial_mass):
        self.initial_mass = initial_mass
        self.current_mass = initial_mass
        self.age = 0
        self.stage = "Main Sequence"
        self.is_alive = True
        self.stages_history = []
    
    def evolve(self):
        """Simulate star evolution based on initial mass"""
        # Increase age
        self.age += 1
        
        # Mass loss mechanism
        mass_loss_rate = 0.001 * (self.initial_mass ** 0.5)
        self.current_mass -= mass_loss_rate
        
        # Track stages
        self.stages_history.append(self.stage)
        
        # Determine star stages and potential death scenarios
        if self.current_mass <= 0:
            self.die("Complete Mass Dissipation")
        elif self.initial_mass < 8:  # Low mass star path
            if self.age > 10000:
                self.stage = "Red Giant"
                if self.age > 12000:
                    self.die("Planetary Nebula")
        else:  # High mass star path
            if self.age > 5000:
                self.stage = "Red Supergiant"
                if self.age > 6000:
                    self.die("Supernova")
    
    def die(self, death_type):
        """Handle star death scenarios"""
        self.is_alive = False
        self.stage = death_type
        
        # Different remnant possibilities based on mass
        if death_type == "Supernova":
            if self.initial_mass < 20:
                self.remnant = "Neutron Star"
            else:
                self.remnant = "Black Hole"
            print(f"Star (Mass: {self.initial_mass:.2f}) died as {death_type}, Remnant: {self.remnant}")
        else:
            print(f"Star (Mass: {self.initial_mass:.2f}) died as {death_type}")

def simulate_stellar_population(num_stars=10, max_iterations=15000):
    """Simulate a population of stars"""
    stars = [Star(random.uniform(1, 30)) for _ in range(num_stars)]
    
    # Simulation tracking
    alive_stars = []
    dead_stars = []
    
    # Simulate evolution
    for iteration in range(max_iterations):
        current_alive_stars = []
        
        for star in stars:
            if star.is_alive:
                star.evolve()
                current_alive_stars.append(star)
        
        alive_stars.append(len(current_alive_stars))
        
        # If no stars are alive, end simulation
        if not current_alive_stars:
            break
        
        # Optionally track dead stars
        dead_stars = [s for s in stars if not s.is_alive]
    
    return stars, alive_stars

"""def visualize_simulation(alive_stars):
    #Visualize star population over time
    plt.figure(figsize=(10, 6))
    plt.plot(alive_stars, label='Living Stars')
    plt.title('Stellar Population Evolution')
    plt.xlabel('Time Steps')
    plt.ylabel('Number of Living Stars')
    plt.legend()
    plt.show()"""

def main():
    # Run simulation
    stars, alive_star_count = simulate_stellar_population(num_stars=20)
    
    # Visualize results
    #visualize_simulation(alive_star_count)
    
    # Additional analysis
    print("\nSimulation Summary:")
    print(f"Total stars simulated: {len(stars)}")
    print(f"Final living stars: {sum(1 for star in stars if star.is_alive)}")
    
    # Detailed star information
    for star in stars:
        if not star.is_alive:
            print(f"\nStar Details:")
            print(f"Initial Mass: {star.initial_mass:.2f}")
            print(f"Final Stage: {star.stage}")
            if hasattr(star, 'remnant'):
                print(f"Remnant: {star.remnant}")

if __name__ == "__main__":
    main()
