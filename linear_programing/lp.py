import scipy.optimize as opt

# Objective function: maximize 50x + 80y
# Constraints 1. 5x + 2y <= 20
# 2. -10x - 12y <= -90  (which is   10x + 12y >= 90)
result = opt.linprog(
[50,80],
A_ub= [[5,2],[-10,-12]],
b_ub = [20,-90]
)

if result.success:
    print("Optimal value:", -result.fun)  ;
    print("y:", result.x[1])
else:
    print("No solution found.")