# -*- coding: utf-8 -*-
"""WEEK2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ovHnVeOxfQ8LY6xBtJQspf36Suz9Ki7b

**Question 1: Simulating a 1D Random Walk with Step Bias**  
A particle moves along a one-dimensional line (1D). At each time step, it can either move:   
 * +1 step to the right with probability p, or
 * -1 step to the left with probability 1−p   
Suppose p=0.85 (i.e., a bias to the right).

**Instructions:**  
1. Write a Python program to simulate a 1D random walk with 1000 steps where:  o The starting position is 0.     
o Each step has a probability of p=0.85 to move right and 1−p=0.15 to move left.
2. Plot the position vs time graph (time on x-axis, position on y-axis).
3. Run the simulation five times and overlay all five random walks in the same graph.
4. Calculate and interpret:  
o The final position of the particle after 1000 steps.
o The mean and standard deviation of the final position across five simulations.
"""

import numpy as np
import matplotlib.pyplot as plt

def simulate_1d_random_walk(n_steps=1000, p=0.85):
    # Each step: +1 with probability p, -1 with probability 1-p
    steps = np.where(np.random.rand(n_steps) < p, 1, -1)
    positions = np.cumsum(steps)
    positions = np.insert(positions, 0, 0)  # starting at position 0
    return positions

# Run the simulation five times
n_simulations = 5
n_steps = 1000
final_positions = []

plt.figure(figsize=(10, 6))
for i in range(n_simulations):
    positions = simulate_1d_random_walk(n_steps=n_steps, p=0.85)
    final_positions.append(positions[-1])
    plt.plot(positions, label=f'Simulation {i+1}')

plt.xlabel('Time (steps)')
plt.ylabel('Position')
plt.title('1D Random Walk with p=0.85 (Biased to Right) - 5 Simulations')
plt.legend()
plt.show()

# Calculate mean and standard deviation of the final positions
mean_final = np.mean(final_positions)
std_final = np.std(final_positions)

print("Final positions:", final_positions)
print("Mean final position:", mean_final)
print("Standard deviation of final positions:", std_final)

"""**Interpretation**  
**Trend:** The particle consistently moves right due to the p = 0.85 bias.  
**Final Positions:** Close to the expected 700, showing a strong drift effect.  
**Mean (696.0):** Matches theoretical expectation (700).  
**Standard Deviation (21.17):** Slightly above the theoretical value (~16), but within a reasonable range.  
**Outliers:** One run (732) was higher than expected, showing natural randomness.  

**Conclusion:** The results align with theory—biased random walks drift right with moderate variation.
"""



"""**Question 2: Comparing 1D Random Walks with and without Drift**   
Suppose two particles perform 1D random walks starting from position 0:   
* *Particle A*: Moves with a drift, i.e., p=0.7 (70% chance to move right).
* *Particle B*: Moves without drift, i.e., p=0.5(equal probability both sides).   

**Instructions:**
1. Write a Python program to simulate 1000 steps for each particle.
2. Plot both random walks on the same graph with:  
o Time on the x-axis.
o Position on the y-axis.
o Different colors for each particle.
3. Calculate and display:
o The mean and standard deviation of the final position after 1000 steps. 4. Interpret your answer

"""

def simulate_1d_random_walk_particle(n_steps=1000, p=0.5):
    steps = np.where(np.random.rand(n_steps) < p, 1, -1)
    positions = np.cumsum(steps)
    positions = np.insert(positions, 0, 0)
    return positions

# Simulate for Particle A (p=0.7) and Particle B (p=0.5)
positions_A = simulate_1d_random_walk_particle(n_steps=1000, p=0.7)
positions_B = simulate_1d_random_walk_particle(n_steps=1000, p=0.5)

plt.figure(figsize=(10, 6))
plt.plot(positions_A, label='Particle A (Drift, p=0.7)', color='blue')
plt.plot(positions_B, label='Particle B (No drift, p=0.5)', color='red')
plt.xlabel('Time (steps)')
plt.ylabel('Position')
plt.title('Comparison of 1D Random Walks: With Drift vs Without Drift')
plt.legend()
plt.show()

# Calculate mean and std for final positions from multiple simulations (if desired, here just one example)
final_A = positions_A[-1]
final_B = positions_B[-1]
print("Particle A final position:", final_A)
print("Particle B final position:", final_B)



"""**Question 3: Simulating a 2D Random Walk (Unbiased)**  
A mosquito trapped in a square grid moves randomly:   
∙ Up, Down, Left, or Right with equal probability (25%) in each direction. The mosquito starts at coordinate (0,0).   

**Instructions:**  
1. Write a Python program to simulate a 2D random walk for 500 steps.
2. Plot the path of the mosquito (X vs Y) using a scatter plot or line plot.
3. Calculate and display:
o The final position after 500 steps.
o The total distance from the origin after 500 steps.
4. Run the simulation 10 times and calculate:  
o The average distance from the origin after 500 steps.
o The standard deviation of the distance.
5. Interpret your answer

"""

def simulate_2d_random_walk(n_steps=500):
    # Define moves: (dx, dy) for up, down, left, right
    moves = {
        'up':    (0, 1),
        'down':  (0, -1),
        'left':  (-1, 0),
        'right': (1, 0)
    }
    directions = list(moves.keys())
    pos = np.array([0, 0])
    path = [pos.copy()]

    for _ in range(n_steps):
        move = moves[np.random.choice(directions)]
        pos += np.array(move)
        path.append(pos.copy())

    path = np.array(path)
    return path

# Run one simulation and plot the 2D path
path = simulate_2d_random_walk(n_steps=500)
plt.figure(figsize=(8, 8))
plt.plot(path[:,0], path[:,1], marker='o', markersize=2, linewidth=1)
plt.scatter(path[-1,0], path[-1,1], color='red', label='Final Position')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('2D Random Walk (500 steps) of a Mosquito')
plt.legend()
plt.grid(True)
plt.show()

# Calculate final position and distance from origin
final_position = path[-1]
distance_from_origin = np.linalg.norm(final_position)
print("Final position:", final_position)
print("Distance from origin:", distance_from_origin)

# Run simulation 10 times to compute average distance and standard deviation
distances = []
for _ in range(10):
    path = simulate_2d_random_walk(n_steps=500)
    final_position = path[-1]
    distance = np.linalg.norm(final_position)
    distances.append(distance)

avg_distance = np.mean(distances)
std_distance = np.std(distances)
print("Average distance after 500 steps (over 10 runs):", avg_distance)
print("Standard deviation of distance:", std_distance)



"""**Question 4: Comparing 2D Random Walks with Bias vs No Bias**   
A person walks randomly in a 2D grid but with a slight bias towards the East (right).   

∙ In each step:    
o Move East: 40% probability   
o Move West: 20% probability   
o Move North: 20% probability   
o Move South: 20% probability   

The person starts at (0,0).   

**Instructions:**   
1. Write a Python program to simulate:  
o 500 steps for the biased random walk.
o 500 steps for an unbiased random walk (equal probability).
2. Plot both paths on the same graph with:  
o Different colors for each walk.
o Scatter plot showing the final position.
3. Calculate and display:
o The final position after 500 steps.
o The total distance from the origin for both walks.
4. Run the simulation 10 times and compute:  
o The average distance from the origin for both biased and unbiased walks. o The standard deviation of the distance.
5. Interpretation:
o Why does the biased random walk drift to the east?
o How does drift affect the standard deviation of the final position?
o What real-world phenomena could this simulation represent (e.g., wind drift,  ocean currents)?

"""

def simulate_2d_random_walk_biased(n_steps=500, bias=True):
    # Define moves: (dx, dy)
    moves = {
        'east':  (1, 0),
        'west':  (-1, 0),
        'north': (0, 1),
        'south': (0, -1)
    }
    if bias:
        directions = ['east', 'west', 'north', 'south']
        # Define probabilities: biased toward east
        probs = [0.4, 0.2, 0.2, 0.2]
    else:
        directions = ['east', 'west', 'north', 'south']
        probs = [0.25, 0.25, 0.25, 0.25]

    pos = np.array([0, 0])
    path = [pos.copy()]

    for _ in range(n_steps):
        move = moves[np.random.choice(directions, p=probs)]
        pos += np.array(move)
        path.append(pos.copy())

    path = np.array(path)
    return path

# Single simulation for both biased and unbiased walks
path_biased = simulate_2d_random_walk_biased(n_steps=500, bias=True)
path_unbiased = simulate_2d_random_walk_biased(n_steps=500, bias=False)

plt.figure(figsize=(10, 8))
plt.plot(path_biased[:,0], path_biased[:,1], label='Biased Walk (East drift)', color='blue')
plt.plot(path_unbiased[:,0], path_unbiased[:,1], label='Unbiased Walk', color='green')
plt.scatter(path_biased[-1,0], path_biased[-1,1], color='red', s=100, label='Biased Final Position')
plt.scatter(path_unbiased[-1,0], path_unbiased[-1,1], color='orange', s=100, label='Unbiased Final Position')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.title('Comparison of 2D Random Walks: Biased vs Unbiased (500 steps)')
plt.legend()
plt.grid(True)
plt.show()

# Calculate final positions and distances
final_biased = path_biased[-1]
final_unbiased = path_unbiased[-1]
distance_biased = np.linalg.norm(final_biased)
distance_unbiased = np.linalg.norm(final_unbiased)

print("Biased final position:", final_biased, "Distance from origin:", distance_biased)
print("Unbiased final position:", final_unbiased, "Distance from origin:", distance_unbiased)

# Run 10 simulations for each and compute average distance and standard deviation
distances_biased = []
distances_unbiased = []
for _ in range(10):
    pb = simulate_2d_random_walk_biased(n_steps=500, bias=True)
    pu = simulate_2d_random_walk_biased(n_steps=500, bias=False)
    distances_biased.append(np.linalg.norm(pb[-1]))
    distances_unbiased.append(np.linalg.norm(pu[-1]))

avg_distance_biased = np.mean(distances_biased)
std_distance_biased = np.std(distances_biased)
avg_distance_unbiased = np.mean(distances_unbiased)
std_distance_unbiased = np.std(distances_unbiased)

print("Biased walk - Average distance:", avg_distance_biased, "Std dev:", std_distance_biased)
print("Unbiased walk - Average distance:", avg_distance_unbiased, "Std dev:", std_distance_unbiased)

