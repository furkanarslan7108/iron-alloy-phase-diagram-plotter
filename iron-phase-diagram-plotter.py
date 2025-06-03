import matplotlib.pyplot as plt
from pycalphad import Database, binplot
import pycalphad.variables as v

# Load database
db_steel = Database('steel_database_fix.tdb')

# Choose phases relevant to Fe-C system
user_phases = input(f'Input custom phase you want to plot (Leave empty for defaults: Liquid and Austenite Ferrite).')
if user_phases != '':
	my_phases_steel = ['LIQUID', 'FCC_A1', user_phases]
else:
	my_phases_steel = ['LIQUID', 'FCC_A1']

# Choose alloy element
element = input('Input iron alloy element: ')
while element == '' or element not in db_steel.elements:
	if element == '':
		print('Element cannot be empty.')
		element = input('Input iron alloy element: ')
	else:
		print('Element not in database. You can try again with a different element or press Ctrl+C to exit.')
		element = input('Input iron alloy element: ')

percentage = input('Input percentage of iron alloy: ')
percentage = float(percentage)/100

# Create a matplotlib Figure object and get the active Axes
fig = plt.figure(figsize=(9,6))
axes = fig.gca()

# Option 1: Binary section at fixed Mn content (e.g., Fe-C at 1.92% Mn)
binplot(db_steel, ['FE', 'C', element, 'VA'], my_phases_steel,
        {v.X('C'):(0, 0.1, 0.001), v.T: (500, 1800, 10), v.X(element): percentage},
        plot_kwargs={'ax': axes, 'tielines': False})

plt.xlabel('X(C)')
plt.ylabel('Temperature (K)')
plt.title(f'Fe-C Phase Diagram ({percentage*100:.4f}% {element})')
plt.tight_layout()
plt.show()