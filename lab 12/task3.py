from scipy.optimize import linprog

# Coefficients for objective function (negative for maximization)
# Let x = units of A, y = units of B
# Profit: 6x + 5y → maximize → minimize -6x -5y
c = [-6, -5]

# Constraints:
# 1. Milk: 1x + 1y <= 5
# 2. Choco: 3x + 2y <= 12
A = [
    [1, 1],    # Milk constraint
    [3, 2],    # Choco constraint
]
b = [5, 12]

# Bounds for decision variables (cannot produce negative units)
x_bounds = (0, None)
y_bounds = (0, None)

# Solve using linprog (default method='highs' in new scipy)
result = linprog(
    c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs'
)

if result.success:
    x, y = result.x
    print("Optimal solution (may not be integers):")
    print(f"Produce {x:.2f} units of A and {y:.2f} units of B")
    print(f"Maximum Profit: Rs {6*x + 5*y:.2f}")
    # For integer solutions (production must be whole units)
    print("\nInteger feasible solutions near optimal point:")
    import math
    candidates = []
    for x_int in [math.floor(x), math.ceil(x)]:
        for y_int in [math.floor(y), math.ceil(y)]:
            if (
                x_int >= 0 and y_int >= 0
                and x_int + y_int <= 5
                and 3*x_int + 2*y_int <= 12
            ):
                profit = 6 * x_int + 5 * y_int
                candidates.append((profit, x_int, y_int))
    if candidates:
        best = max(candidates)
        print(f"Produce {best[1]} units of A and {best[2]} units of B for profit Rs {best[0]}")
    else:
        print("No integer feasible solution found very close to the optimum.")
else:
    print("Optimization failed:", result.message)
