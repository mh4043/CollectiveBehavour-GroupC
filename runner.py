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
dog = ShepherdDog(config['DOG']['X'].split()[0], config['DOG']['Y'].split()[0], goal, parameters)

sheep_arr = []

sheep_count = int(config['SHEEP']['N'])
for i in range(1, sheep_count + 1):
    curr_sheep_x, curr_sheep_y = config['SHEEP'][f'p{i}'].split(',')
    sheep_obj = Sheep(int(curr_sheep_x), int(curr_sheep_y), goal, parameters)
    sheep_obj.goal_not_reached = True
    sheep_arr.append(sheep_obj)

success = False
step = 0
while step != 4000 and not success:

    if not step % 100:
        print(f"Step: {step}")
        # Plot the current positions
        fig = plt.figure()
        ax = fig.subplots()

        width = int(config['WINDOW']['WIDTH'])
        height = int(config['WINDOW']['HEIGHT'])

        # Setup plot limits
        ax.set_xlim(-100, width-100)
        ax.set_ylim(0, height)

        # Setup ticks to show grid
        ax.set_xticks(range(-50, int(config['WINDOW']['WIDTH']), 50))
        ax.set_yticks(range(-50, int(config['WINDOW']['HEIGHT']), 50))

        # Show grid with reduced alpha
        ax.grid(alpha=0.25)

        ax.scatter(dog.position[0], dog.position[1], color='red', marker='o', s=25)

        # Draw sheep on plot
        ax.scatter([sheep_arr[i].position[0] for i in range(len(sheep_arr))], [
                sheep_arr[i].position[1] for i in range(len(sheep_arr))], color='blue', marker='o', s=20)
        
        # Draw the goal circle
        circle = plt.Circle((int(config['GOAL']['X']), int(config['GOAL']['Y'])), int(
            config['GOAL']['RAD']), color='r', fill=False)
        
        ax.add_artist(circle)

        fig.savefig(f'./figures/{step}.png')

        plt.close()


    if dog.calculate_velocity(sheep_arr):
        # print("Success at step: ", step)
        break
    dog.move()

    # Move sheep
    for sheep in sheep_arr:
        sheep.calculate_velocity(dog, sheep_arr, step)
        sheep.move()





    step += 1

