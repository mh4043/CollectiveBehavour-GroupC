import matplotlib.pyplot as plt
from sheep import Sheep
from shepherd import ShepherdDog
import configparser


# Import config file from config.ini
config = configparser.ConfigParser()
config.read('config.ini')


def setup_plot():
    # Setup a plot
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

    # Read sheep count from config file
    sheep_count = int(config['SHEEP']['N'])

    # Read sheep coordinates from config file
    sheep = []
    for i in range(1, sheep_count + 1):
        curr_sheep_x, curr_sheep_y = config['SHEEP'][f'p{i}'].split(',')
        sheep.append(Sheep(int(curr_sheep_x), int(curr_sheep_y)))

    # Draw sheep on plot
    ax.scatter([sheep[i].x for i in range(sheep_count)], [
               sheep[i].y for i in range(sheep_count)], color='blue', marker='o', s=20)

    # Draw the dog on plot
    dog = ShepherdDog(config['DOG']['X'], config['DOG']['Y'])
    ax.scatter(dog.x, dog.y, color='red', marker='o', s=25)

    # Draw the goal circle
    circle = plt.Circle((int(config['GOAL']['X']), int(config['GOAL']['Y'])), int(
        config['GOAL']['RAD']), color='r', fill=False)
    ax.add_artist(circle)

    return fig, ax, sheep


fig, ax, sheep = setup_plot()
fig.savefig('./figures/sheep.png')
plt.close()
