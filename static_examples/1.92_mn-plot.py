import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

# Load database
db_steel = Database('steel_database_fix.tdb')

# Choose phases relevant to Fe-C-Mn system
# These are common phases in steel systems - adjust based on what's available in your TDB
my_phases_steel = ['LIQUID', 'FCC_A1']

# Create a matplotlib Figure object and get the active Axes
fig = plt.figure(figsize=(9,6))
axes = fig.gca()

# Option 1: Binary section at fixed Mn content (e.g., Fe-C at 1.92% Mn)
binplot(db_steel, ['FE', 'C', 'MN', 'VA'], my_phases_steel,
        {v.X('C'):(0, 0.1, 0.001), v.T: (500, 1800, 10), v.X('MN'): 0.01928},
        plot_kwargs={'ax': axes, 'tielines': False})

plt.xlabel('X(C)')
plt.ylabel('Temperature (K)')
plt.title('Fe-C Phase Diagram (1.92% Mn)')
plt.tight_layout()
plt.show()