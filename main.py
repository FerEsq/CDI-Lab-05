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
        self.final_key = []
        self.matching_bases = []
        self.eve_bases = []
        self.eve_results = []
        self.eve_detected = False
        
    def generate_alice_bits(self) -> None:
        self.alice_bits = [random.randint(0, 1) for _ in range(self.n_bits)]
        
    def generate_bases(self) -> None:
        self.alice_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
        self.bob_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
        if self.include_eve:
            self.eve_bases = [random.choice(['↕', '↗']) for _ in range(self.n_bits)]
                
    def simulate_bob_measurements(self) -> None:
        for i in range(self.n_bits):
            if self.include_eve:
                # If Eve intercepted, Bob's measurement is based on Eve's result
                if self.bob_bases[i] == self.eve_bases[i]:
                    self.bob_results.append(self.eve_results[i])
                else:
                    self.bob_results.append(random.randint(0, 1))
            else:
                # Normal case without Eve
                if self.alice_bases[i] == self.bob_bases[i]:
                    self.bob_results.append(self.alice_bits[i])
                else:
                    self.bob_results.append(random.randint(0, 1))
                
    def generate_final_key(self) -> None:
        for i in range(self.n_bits):
            if self.alice_bases[i] == self.bob_bases[i]:
                self.matching_bases.append(i)
                self.final_key.append(self.alice_bits[i])
                
    def print_results(self) -> None:
        print("\nBB84 Protocol Simulation Results:")
        
        # Prepare data for the main table
        table_data = []
        for i in range(self.n_bits):
            row = [
                i + 1,  # Index
                self.alice_bits[i],
                self.alice_bases[i],
                self.bob_bases[i],
                self.bob_results[i]
            ]
            if self.include_eve:
                row.extend([self.eve_bases[i], self.eve_results[i]])
            table_data.append(row)
            
        # Define headers
        headers = ["Bit #", "Alice's Bit", "Alice's Base", "Bob's Base", "Bob's Result"]
        if self.include_eve:
            headers.extend(["Eve's Base", "Eve's Result"])
            
        # Print the main table
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        # Print matching bases and final key
        print("\nMatching Bases and Final Key:")
        print("-" * 50)
        
        key_data = []
        for idx in self.matching_bases:
            key_data.append([
                idx + 1,
                self.alice_bases[idx],
                self.bob_bases[idx],
                self.alice_bits[idx]
            ])
            
        key_headers = ["Bit #", "Alice's Base", "Bob's Base", "Final Key Bit"]
        print(tabulate(key_data, headers=key_headers, tablefmt="grid"))
        
        # Print summary
        print("\nSummary:")
        print("-" * 50)
        summary_data = [
            ["Total bits", self.n_bits],
            ["Matching bases", len(self.matching_bases)],
            ["Final key length", len(self.final_key)]
        ]
        if self.include_eve:
            summary_data.append(["Eve detected", "Yes" if self.eve_detected else "No"])
            
        print(tabulate(summary_data, tablefmt="grid"))

    def run_simulation(self) -> None:
        self.generate_alice_bits()
        self.generate_bases()
        self.simulate_bob_measurements()
        self.generate_final_key()
        self.print_results()

# Example usage
if __name__ == "__main__":
    # Simulate BB84 protocol with 20 bits and Eve's interception
    simulation = BB84Simulation(20, include_eve=False)
    simulation.run_simulation()
