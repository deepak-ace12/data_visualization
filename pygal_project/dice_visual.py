import pygal
from die import Die

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the result
hist = pygal.Bar()

hist.tittle = "Result of rolling D6 and D10 50000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_visual.svg')
