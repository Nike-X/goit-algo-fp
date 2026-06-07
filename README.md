# Basic Algorithms and Data Structures — Final Project

This repository contains the final project files for the course **“Basic Algorithms and Data Structures”**.

This README describes the outputs for the following tasks:

- **Task 6:** Greedy algorithms and dynamic programming (`menu_selection.py`)
- **Task 7:** Monte Carlo simulation of dice rolls (`monte_carlo.py`)

---

## 6. Greedy Algorithms and Dynamic Programming (`menu_selection.py`)

This task is a variation of the **0/1 knapsack problem**.

The goal is to select a set of dishes with the maximum total number of calories without exceeding the given budget.

### Initial Data

**Total budget:** `100`

**List of dishes:**

```python
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
```

### Results of Execution

#### Greedy Algorithm

```text
Selected items: ['cola', 'potato', 'pepsi', 'hot-dog']
Total cost: 80
Total calories: 870
```

#### Dynamic Programming

```text
Selected items: ['pizza', 'pepsi', 'cola', 'potato']
Total cost: 100
Total calories: 970
```

### Conclusion

As we can see, the dynamic programming approach finds the optimal solution, while the greedy algorithm does not always guarantee the best result.

On the other hand, the greedy algorithm is faster and easier to implement.

---

## 7. Simulating Dice Rolls Using the Monte Carlo Method (`monte_carlo.py`)

In this task, `2d6` dice rolls were simulated using the Monte Carlo method. The results are compared with the analytical probabilities.

### Initial Data

**Number of dice:** `2`  
**Number of faces per die:** `6`  
**Number of rolls:** `1,000,000`

### Results of Execution

```text
Monte Carlo simulation for 2d6
Number of rolls: 1,000,000

+-----+---------------+--------------+--------------+
| Sum | Monte Carlo % | Analytical % | Difference % |
+-----+---------------+--------------+--------------+
|   2 |          2.79 |         2.78 |         0.01 |
|   3 |          5.57 |         5.56 |         0.01 |
|   4 |          8.33 |         8.33 |         0.00 |
|   5 |         11.05 |        11.11 |         0.06 |
|   6 |         13.90 |        13.89 |         0.01 |
|   7 |         16.66 |        16.67 |         0.01 |
|   8 |         13.90 |        13.89 |         0.01 |
|   9 |         11.13 |        11.11 |         0.02 |
|  10 |          8.33 |         8.33 |         0.00 |
|  11 |          5.56 |         5.56 |         0.00 |
|  12 |          2.78 |         2.78 |         0.00 |
+-----+---------------+--------------+--------------+
```

### Conclusion

With `1,000,000` rolls, the Monte Carlo simulation produces results that are very close to the analytical probabilities.

The difference is only a few hundredths of a percent, which confirms that increasing the number of simulations improves the accuracy of the Monte Carlo method.
