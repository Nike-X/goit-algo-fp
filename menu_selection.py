# This script implements greedy algorithm and dynamic programming based
# solutions for a 0/1 knapsack problem variant

# Implement greedy algorithm based solution
def menu_greedy_algorithm(meals: dict, budget: int):
    # Initialize results
    selected_items = []
    total_cost = 0
    total_calories = 0

    remaining_budget = budget

    # Calculate each meal "efficiency" as calories / cost ratio
    food_efficiency = [{"name": name, "ratio": round(info["calories"] / info["cost"], 2)}
        for name, info in meals.items()
    ]

    # Sort meals list by "efficiency" in descending order
    food_efficiency.sort(key=lambda x: x["ratio"],reverse=True)

    # For each meal from most efficient
    for item in food_efficiency:
        name = item["name"]

        cost = meals[name]["cost"]
        calories = meals[name]["calories"]

        # If meal fits into remaining budget
        # add it to results 
        # and subtract it cost from remaining budget
        # Otherwise, ignore meal
        if cost <= remaining_budget:
            total_cost += cost
            total_calories += calories
            remaining_budget -= cost
            selected_items.append(name)

    # Return list of selected meals, their total cost and total calories
    return selected_items, total_cost, total_calories

# Implement dynamic programming based solution
def menu_dynamic_programming(meals: dict, budget: int):
    # Convert dictionary to list to work with item indices
    items_list = list(meals.items())
    item_count = len(items_list)

    # dp[i][current_budget] stores the maximum calories
    # using the first i items and the given current_budget
    dp = [[0 for _ in range(budget + 1)] for _ in range(item_count + 1)]

    # Fill DP table
    for i in range(1, item_count + 1):
        item_name, item_data = items_list[i - 1]
        cost = item_data["cost"]
        calories = item_data["calories"]

        for current_budget in range(budget + 1):
            # Option 1: do not take the current item
            dp[i][current_budget] = dp[i - 1][current_budget]

            # Option 2: take the current item, if it fits the current budget
            if cost <= current_budget:
                calories_with_item = calories + dp[i - 1][current_budget - cost]

                if calories_with_item > dp[i][current_budget]:
                    dp[i][current_budget] = calories_with_item

    # Restore selected items from the filled DP table
    selected_items = []
    current_budget = budget

    for i in range(item_count, 0, -1):
        # If value changed compared to the previous row,
        # this item was included in the optimal solution
        if dp[i][current_budget] != dp[i - 1][current_budget]:
            item_name, item_data = items_list[i - 1]
            selected_items.append(item_name)
            current_budget -= item_data["cost"]

    selected_items.reverse()

    total_cost = sum(meals[item]["cost"] for item in selected_items)
    total_calories = dp[item_count][budget]

    return selected_items, total_cost, total_calories

# Select items (meals) using both methods and print results
def main():
    # Define budget
    budget = 100

    # Define meals dictionary
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    # Select meals using greedy algorithm and print results
    greedy_selected_items, greedy_total_cost, greedy_total_calories = menu_greedy_algorithm(items, budget)

    print("Greedy algorithm:\n")
    print(f"Selected items: {greedy_selected_items}\n")
    print(f"Total cost: {greedy_total_cost}\n")
    print(f"Total calories: {greedy_total_calories}\n")

    # Select meals using dynamic programming and print results
    dp_selected_items, dp_total_cost, dp_total_calories = menu_dynamic_programming(items, budget)

    print("Dynamic programming:\n")
    print(f"Selected items: {dp_selected_items}\n")
    print(f"Total cost: {dp_total_cost}\n")
    print(f"Total calories: {dp_total_calories}\n")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()
