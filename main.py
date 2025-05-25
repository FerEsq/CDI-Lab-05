import random
import numpy as np
from typing import List, Tuple
from tabulate import tabulate

class BB84Simulation:
    def __init__(self, n_bits: int, include_eve: bool = False):
        self.n_bits = n_bits
        self.include_eve = include_eve
        self.alice_bits = []
        self.alice_bases = []
        self.bob_bases = []
        self.bob_results = []
        
    def generate_alice_bits(self) -> None:
        self.alice_bits = [random.randint(0, 1) for _ in range(self.n_bits)]
        
    def generate_bases(self) -> None:
        self.alice_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
        self.bob_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
        if self.include_eve:
            self.eve_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
        

    def run_simulation(self) -> None:
        self.generate_alice_bits()
        self.generate_bases()

# Example usage
if __name__ == "__main__":
    # Simulate BB84 protocol with 20 bits and Eve's interception
    simulation = BB84Simulation(20, include_eve=False)
    simulation.run_simulation()
