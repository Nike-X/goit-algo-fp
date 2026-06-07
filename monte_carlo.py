# This script implements Monte Carlo simulation for rolls of 
# an arbitrary number of dice of a given size

import random
from itertools import product

# Calculate probability of each roll sum using Monte Carlo method
def calculate_monte_carlo_probabilities(dice_number, dice_size, roll_number):
    # Create a dictionary for all possible roll results
    rolls = dict.fromkeys(range(dice_number, dice_number * dice_size + 1), 0)

    # Execute rolls in loop
    for _ in range(roll_number):
        # Reset the roll sum
        roll_sum = 0
        # Roll each die and sum the results
        for _ in range(1, dice_number + 1):
            roll_sum += random.randint(1, dice_size)
        # Record obtained roll results sum 
        rolls[roll_sum] = rolls[roll_sum] + 1

    # Calculate probability for each roll result as a percentage
    results = {key: round(value / roll_number * 100, 2) for key, value in rolls.items()}

    return results

# Calculate probabilities for all possible roll results using
# Cartesian product (itertools.product)
def calculate_analytical_probabilities(dice_number, dice_size):
    sums_count = dict.fromkeys(range(dice_number, dice_number * dice_size + 1), 0)

    all_rolls = product(range(1, dice_size + 1), repeat=dice_number)

    total_combinations = 0

    for roll in all_rolls:
        roll_sum = sum(roll)
        sums_count[roll_sum] += 1
        total_combinations += 1

    probabilities = {
        key: round(value / total_combinations * 100, 2)
        for key, value in sums_count.items()
    }

    return probabilities

# Function prints results as a formatted table
def print_results_table(monte_carlo_results, analytical_results, dice_number, dice_size, roll_number):
    # Print results and difference for both approaches
    print(f"\nMonte Carlo simulation for {dice_number}d{dice_size}")
    print(f"Number of rolls: {roll_number:,}\n")

    print("+-----+---------------+--------------+--------------+")
    print("| Sum | Monte Carlo % | Analytical % | Difference % |")
    print("+-----+---------------+--------------+--------------+")
    for roll_sum in sorted(monte_carlo_results):
        monte_carlo_value = monte_carlo_results[roll_sum]
        analytical_value = analytical_results[roll_sum]
        # Calculate difference between analytical result and Monte Carlo simulation
        difference = abs(monte_carlo_value - analytical_value)

        print(
            f"| {roll_sum:>4}" 
            f"| {monte_carlo_value:>14.2f}" 
            f"| {analytical_value:>13.2f}" 
            f"| {difference:>12.2f} |"
            )
    print("+-----+---------------+--------------+--------------+")

# Calculate probabilities for the given dice setup
# using analytical approach and Monte Carlo simulation
def main():
    # Add fixed seed to get reproducible result
    random.seed(55)

    # Define the number of dice, die size, and number of rolls
    dice_number = 2
    dice_size = 6
    roll_number = 1_000_000

    # Calculate probability of each roll result
    monte_carlo_results = calculate_monte_carlo_probabilities(dice_number, dice_size, roll_number)
    analytical_results = calculate_analytical_probabilities(dice_number, dice_size)

    # Print results as a formatted table
    print_results_table(monte_carlo_results, analytical_results, dice_number, dice_size, roll_number)

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()
