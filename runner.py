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

goal = [int(config['GOAL']['X']), int(config['GOAL']['Y']), int(config['GOAL']['RAD'])]

# Setup starting positions
dog = ShepherdDog(config['DOG']['X'], config['DOG']['Y'],config['DOG']['RAD'], goal, parameters)

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

    sheep_copy = [sheep for sheep in sheep_arr if not sheep.goal_reached]
    goal_sheep = [sheep for sheep in sheep_arr if sheep.goal_reached]

    if not step % 10 or not len(sheep_copy):
        print(f"Step: {step}, sheep left: {len(sheep_copy)}")
        # Plot the current positions
        fig = plt.figure()
        ax = fig.subplots()

        width = int(config['WINDOW']['WIDTH'])
        height = int(config['WINDOW']['HEIGHT'])

        # Setup plot limits
        ax.set_xlim(0, 350)
        ax.set_ylim(0, 350)

        # Setup ticks to show grid
        ax.set_xticks(range(0, 375, 50))
        ax.set_yticks(range(0, 375, 50))

        # Show grid with reduced alpha
        ax.grid(alpha=0.25)

        ax.scatter(dog.position[0], dog.position[1], color='red', marker='o', s=25)

        # Draw sheep on plot
        ax.scatter([sheep_arr[i].position[0] for i in range(len(sheep_arr))], [
                sheep_arr[i].position[1] for i in range(len(sheep_arr))], color='blue', marker='o', s=20)
        
        # Draw the goal circle
        circle = plt.Circle((int(config['GOAL']['X']), int(config['GOAL']['Y'])), int(
            config['GOAL']['RAD'])+2, color='r', fill=False)
        
        ax.add_artist(circle)

        fig.savefig(f'./figures/{step}.png')

        plt.close()

    if not len(sheep_copy):
        print("All sheep reached goal")
        break

    if dog.calculate_velocity(sheep_copy):
        # print("Success at step: ", step)
        break
    dog.move()

    # Move sheep
    for sheep in sheep_arr:
        if sheep.goal_reached:
            sheep.velocity = 0.99*sheep.velocity
            sheep.move()
        else:
            sheep.calculate_velocity(dog, sheep_copy, step)
            sheep.move()
        
        # TODO, check if sheep reached goal, if so, set goal_reached to True and remove from sheep_arr

    

    step += 1

