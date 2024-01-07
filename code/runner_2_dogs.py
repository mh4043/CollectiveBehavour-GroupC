import matplotlib.pyplot as plt
from sheep import Sheep
from shepherd import ShepherdDog
import configparser
import time


# Import config file from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Read parameters from config file
parameters = {key: float(p.split()[0]) for key, p in config['PARAMETERS'].items()}

# print(parameters)
goal = [int(config['GOAL']['X']), int(config['GOAL']['Y']), int(config['GOAL']['RAD'])]

# Setup starting positions
# Example X = 63,90 #? testing search algo set to 10 //! initial value 63
# Split the string on comma and space and # to get values




dogs = [ShepherdDog(config['DOG']['X'].split()[0], 
                  config['DOG']['Y'].split()[0], 
                  config['DOG']['RAD'].split()[0], 
                  goal, 
                  parameters,
                  side="left"
                  ),
         ShepherdDog(config['DOG']['X2'].split()[0], 
                  config['DOG']['Y2'].split()[0], 
                  config['DOG']['RAD2'].split()[0], 
                  goal, 
                  parameters,
                  side="right"
                  ),
]

# dogs = [ShepherdDog(config['DOG']['X'].split()[0], 
#                   config['DOG']['Y'].split()[0], 
#                   config['DOG']['RAD'].split()[0], 
#                   goal, 
#                   parameters,
#                   )]

dog_colors = ['red', 'purple']

sheep_arr = []

sheep_count = int(config['SHEEP']['N'])
for i in range(1, sheep_count + 1):
    curr_sheep_x, curr_sheep_y = config['SHEEP'][f'p{i}'].split('#')[0].split(',')
    sheep_obj = Sheep(int(curr_sheep_x), int(curr_sheep_y), goal, parameters)
    sheep_obj.goal_not_reached = True
    sheep_arr.append(sheep_obj)

# Delete all images in figures folder
import os
import glob
files = glob.glob('../figures/*')
for f in files:
    os.remove(f)

success = False
step = 0
while step != 400000 and not success:

    sheep_copy = [sheep for sheep in sheep_arr if not sheep.goal_reached]
    goal_sheep = [sheep for sheep in sheep_arr if sheep.goal_reached]

    if not step % 20 or not len(sheep_copy): #for testing plot every 100th step, for visualisation every 10th
        print(f"Step: {step}, sheep left: {len(sheep_copy)}")

        # Plot the current positions
        fig = plt.figure(figsize=(8, 8))
        ax = fig.subplots()

        # Add title
        ax.set_title(f'Step: {step}')

        width = int(config['WINDOW']['WIDTH'])
        height = int(config['WINDOW']['HEIGHT'])

        # Setup plot limits
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)

        # Setup ticks to show grid
        ax.set_xticks(range(0, width, 50))
        ax.set_yticks(range(0, height, 50))

        # Show grid with reduced alpha
        ax.grid(alpha=0.1)

        for i,dog in enumerate(dogs):
            ax.scatter(dog.position[0], dog.position[1], color=dog_colors[i], marker='o', s=25)
            # dog_vision = plt.Circle((dog.position[0], dog.position[1]), dog.radius, color='teal', fill=False)
            # ax.add_artist(dog_vision)

        # Draw sheep on plot
        ax.scatter([sheep_copy[i].position[0] for i in range(len(sheep_copy))], [
                sheep_copy[i].position[1] for i in range(len(sheep_copy))], color='blue', marker='o', s=20)
        # Draw sheep on plot
        ax.scatter([goal_sheep[i].position[0] for i in range(len(goal_sheep))], [
                goal_sheep[i].position[1] for i in range(len(goal_sheep))], color='green', marker='o', s=20)
        
        # Draw the goal circle
        circle = plt.Circle((int(config['GOAL']['X']), int(config['GOAL']['Y'])), int(
            config['GOAL']['RAD'])+2, color='r', fill=False)
        ax.add_artist(circle)
        
        # Draw the fence
        x_offset = parameters['x_offset']
        y_offset = parameters['y_offset']
        fence = plt.Rectangle((0 + x_offset, 0 + y_offset), width-(2*x_offset)-1, height - (2*y_offset)-1, color='brown', fill=False)
        ax.add_artist(fence)
        

        fig.savefig(f'../figures/{step}.png')

        plt.close()

    if not len(sheep_copy):
        print("All sheep reached goal")
        break


    dogs[0].calculate_velocity(sheep_copy, step, None)
    dogs[1].calculate_velocity(sheep_copy, step, dogs[0])
    dogs[0].move()
    dogs[1].move()

    # Move sheep
    for sheep in sheep_arr:
        if sheep.goal_reached:
            # Slow down sheep if it reached goal
            sheep.velocity = 0.975*sheep.velocity
            sheep.move()
        else:
            sheep.calculate_velocity(dogs[0], sheep_copy, step, other_dog=dogs[1])
            # sheep.calculate_velocity(dogs[0], sheep_copy, step, None)
            sheep.move()
        
    step += 1
