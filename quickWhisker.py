import matplotlib.pyplot as plt

# Define your data
categories = ['Current', 'Proposed']
open_temps = [110, 95]  # Median open temperatures
close_temps = [75, 65]  # Median close temperatures
open_variance = 5
close_variance = 15

# Calculate the temperature ranges for boxes
open_ranges = [(temp - open_variance, temp + open_variance) for temp in open_temps]
close_ranges = [(temp - close_variance, temp + close_variance) for temp in close_temps]

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))

# Colors for the boxes
colors = ['lightblue', 'lightgreen']

# Plot the boxes for each category
for i, category in enumerate(categories):
    position = i + 1  # Position on the y-axis
    # Plot open temperature box
    ax.bxp([{'whislo': open_ranges[i][0], 'q1': open_ranges[i][0], 'med': open_temps[i], 
             'q3': open_ranges[i][1], 'whishi': open_ranges[i][1], 'fliers': []}], 
            positions=[position], vert=False, patch_artist=True, 
            showfliers=False, widths=0.3, boxprops=dict(facecolor=colors[0]))
    
    # Plot close temperature box
    ax.bxp([{'whislo': close_ranges[i][0], 'q1': close_ranges[i][0], 'med': close_temps[i], 
             'q3': close_ranges[i][1], 'whishi': close_ranges[i][1], 'fliers': []}], 
            positions=[position], vert=False, patch_artist=True, 
            showfliers=False, widths=0.3, boxprops=dict(facecolor=colors[1]))

# Add 'x' marker for Thermal Fuse
thermal_fuse_x = 115
thermal_fuse_y = (1 + 2) / 2  # Between 'Current' (1) and 'Proposed' (2)
ax.scatter(thermal_fuse_x, thermal_fuse_y, color='red', zorder=5, marker='x', s=200)
ax.text(thermal_fuse_x, thermal_fuse_y + 0.1, 'Thermal Fuse', ha='center', va='bottom')

# Customize the plot
ax.set_yticks([1, 2])
ax.set_yticklabels(categories)
ax.set_xlabel('Temperature (C)')
ax.set_title('Current and Proposed Temperature Ranges')
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)

# Set x-axis limits if necessary
lower_limit = min(close_temps) - close_variance - 10
upper_limit = max(open_temps) + open_variance + 10
ax.set_xlim(lower_limit, upper_limit)

# Adding custom legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor=colors[0], label='Open Cutoff Temp'),
                   Patch(facecolor=colors[1], label='Close Cutoff Temp')]
ax.legend(handles=legend_elements, loc='upper right')

plt.show()
