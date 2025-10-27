import matplotlib.pyplot as plt
import numpy as np

# Create a figure and a polar subplot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Define some polar coordinates (r, theta)
theta = np.array([np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4])
r = np.array([2, 3, 1, 2.5, 1.5])

# Plot the points
ax.scatter(theta, r, marker='o', color='blue', s=50)

# Annotate each point with its coordinates
for i in range(len(theta)):
    # Format the coordinates for display
    coord_text = f'({r[i]:.1f}, {np.degrees(theta[i]):.0f}°)'
    
    # Add the annotation, adjusting position for readability
    ax.annotate(coord_text, 
                xy=(theta[i], r[i]), 
                xytext=(theta[i], r[i] + 0.5), # Offset text slightly above the point
                arrowprops=dict(facecolor='black', shrink=0.05, width=0.5),
                ha='center', va='bottom')

# Set plot title and display
ax.set_title("Polar Plot with Point Coordinates")
plt.show()