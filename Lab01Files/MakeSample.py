"""
MakeSample.py
Michael R. Gustafson II
January 1, 2021

I understand and have adhered to all the tenets of the Duke Community Standard
in creating this code.
Signed: mrg
"""

# Import modules
import matplotlib.pyplot as plt
import numpy as np

# Create linearly spaced array as basis for graphs
x = np.linspace(0, 1, 100)

# Generate x**3 data
y = x**3

# Initialize figure and axes
fig, ax = plt.subplots(num=1, clear=True)

# Plot various lines in different colors and line styles
ax.plot(x, y, 'orange')
ax.plot(1 - x, y, 'g:')
ax.plot(y, x, 'r--')
ax.plot(y, 1 - x, 'c-.')
ax.plot(x, 1 - y, 'm:')
ax.plot(1 - x, 1 - y, 'y-')
ax.plot(1 - y, x, 'k-.')
ax.plot(1 - y, 1 - x, 'b--')

# Add text to center
ax.text(0.5, 0.5, 'Sample', horizontalalignment='center',
        verticalalignment='center', size=30)

# Set properties
ax.set(xlabel='x (UNITS)', ylabel='y (UNITS)',
       title='Different Relationships (NetID)',
       aspect='equal')

# Further refine and save plot
ax.grid(True)
fig.tight_layout()
fig.savefig('SamplePyplot.png')
