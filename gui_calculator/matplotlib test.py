import matplotlib.pyplot as plt


#plt.figure(figsize=(4, 3))
#plt.figure(figsize=(40, 30))

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
#plt.savefig("grafica1.png")


'''
# The x and y coordinates for our points
x_coords = [3, 1]
y_coords = [2, 5]

# Create the plot
plt.figure(figsize=(16, 12))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='r')

# Add titles and labels for clarity
plt.title('Graph with Points (3, 2) and (1, 5)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a grid
plt.grid(True)

# Annotate the points
plt.text(x_coords[0] + 0.1, y_coords[0], '(3, 2)')
plt.text(x_coords[1] + 0.1, y_coords[1], '(1, 5)')

# Set axis limits to make the plot easy to read
plt.xlim(0, 6)
plt.ylim(0, 6)

# Show the plot
plt.show()
'''