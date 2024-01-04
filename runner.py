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

dog = ShepherdDog(config['DOG']['X'].split()[0], config['DOG']['Y'].split()[0], config['DOG']['RAD'].split()[0], goal, parameters)

sheep_arr = []

sheep_count = int(config['SHEEP']['N'])
for i in range(1, sheep_count + 1):
    curr_sheep_x, curr_sheep_y = config['SHEEP'][f'p{i}'].split(',')
    sheep_obj = Sheep(int(curr_sheep_x), int(curr_sheep_y), goal, parameters)
    sheep_obj.goal_not_reached = True
    sheep_arr.append(sheep_obj)

# shp = Sheep(-100, -100, goal, parameters)
# sheep_arr = [shp]

success = False
step = 0
while step != 400000 and not success:

    sheep_copy = [sheep for sheep in sheep_arr if not sheep.goal_reached]
    goal_sheep = [sheep for sheep in sheep_arr if sheep.goal_reached]

    if not step % 100 or not len(sheep_copy): #for testing plot every 100th step, for visualisation every 10th
        print(f"Step: {step}, sheep left: {len(sheep_copy)}")

        # Plot the current positions
        fig = plt.figure()
        ax = fig.subplots()

        width = int(config['WINDOW']['WIDTH'])
        height = int(config['WINDOW']['HEIGHT'])

        # Setup plot limits
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)

        # Setup ticks to show grid
        ax.set_xticks(range(0, width, 50))
        ax.set_yticks(range(0, height, 50))

        # Show grid with reduced alpha
        ax.grid(alpha=0.25)

        ax.scatter(dog.position[0], dog.position[1], color='red', marker='o', s=25)
        # dog_vision = plt.Circle((dog.position[0], dog.position[1]), dog.radius, color='teal', fill=False)
        # ax.add_artist(dog_vision)

        # Draw sheep on plot
        ax.scatter([sheep_arr[i].position[0] for i in range(len(sheep_arr))], [
                sheep_arr[i].position[1] for i in range(len(sheep_arr))], color='blue', marker='o', s=20)
        
        # Draw the goal circle
        circle = plt.Circle((int(config['GOAL']['X']), int(config['GOAL']['Y'])), int(
            config['GOAL']['RAD'])+2, color='r', fill=False)
        ax.add_artist(circle)
        
        # Draw the fence
        x_offset = parameters['x_offset']
        y_offset = parameters['y_offset']
        fence = plt.Rectangle((0 + x_offset, 0 + y_offset), width-(2*x_offset)-1, height - (2*y_offset)-1, color='brown', fill=False)
        ax.add_artist(fence)
        

        fig.savefig(f'./figures/{step}.png')

        plt.close()

    if not len(sheep_copy):
        print("All sheep reached goal")
        break

    if dog.calculate_velocity(sheep_copy, step):
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

