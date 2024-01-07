# Collective Behaviour - Group C

## Group members
1. [Matic Hrastelj](https://github.com/mh4043)
2. [Žan Korošak](https://github.com/ZanKorosak)
3. [Gašper Habjan](https://github.com/haby12)
4. [Vid Cesar](https://github.com/vc4183)

## Sheepdog Driven Algorithm for Sheep Herd Transport
In this project, we make a review and a re-creation of a collective behaviour algorithm for herding sheep by a sheepdog, presented in the reference paper, by [Liu et al](https://ieeexplore.ieee.org/document/9549396). [[1]](#1). We simulate an environment with pre-determined starting positions of all sheep and the sheepdog, while also creating a sheepfold as a final goal for the sheep. We review the performance of the algorithm, presented in the mentioned paper. We also try to suggest and implement some improvements/extensions and compare the obtained results at the end.

For improvements/extensions, we suggest and implement incorporation of two sheepdogs, which of course, reduces the number of required steps to reach the goal. We also manage to implement so-called wandering or combing. In this case, a sheepdog has to find sheep herd first, while at the basic algorithm, we assume that they're on pretty much the same starting position (sheep herd is inside the vision of a sheepdog). When sheep herd is found, the dog afterwards manages to lead them to the goal. However, in each variation of the algorithm, sheepdog successfully leads sheep to the desired goal.

In our work, more specifically in the implementation itself, we also use some rigorous equations. Some detailed explanations can be found [here](https://github.com/mh4043/CollectiveBehavour-GroupC/blob/main/docs/variables%20and%20equations%20descriptions.md). More detailed steps of the basic algorithm can be found [here](https://github.com/mh4043/CollectiveBehavour-GroupC/blob/main/docs/algorithm%20description.md).

## Goals and milestones
| Description                                                                                                                                                                  | Date         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| - Make a rough overview of the field.<br/> - Review the basics of the original paper. <br/> - Re-create the basic algorithm to some extent, presented in the original paper. | 20. 11. 2023 |
| - Fully re-create the algorithm, provided in the original paper. <br/> - Improve our previous work from the 1st milestone, with feedback given by the classmates.            | 18. 12. 2023 |
| - Improve the work, based on our observations and performance of the algorithm. <br/> - Implement additional ideas, in terms of improvements and extensions.                 | 08. 01. 2024 |

We managed to follow the milestones, declared at the very early stage of the project. We also tried to follow the feedback of the other participants of the course as much as possible. This helped us improve our work.

At the final stage, we had a lot of ideas for improvements and extensions, but in the end we decided to apply only few of them. The reason is because we faced some problems at the implementation. Instead, we focused only on the chosen ones and made sure for these to be qualitative.

## How to run - instructions
There are some Python packages required to be installed, in order to be able to run the program. Check requirements [here](https://github.com/mh4043/CollectiveBehavour-GroupC/blob/main/code/requirements.txt).

The program can afterwards be simply run, by applying the command below. Make sure you are inside the right directory (.../code). Before run, also make sure to create the 'figures' directory on the root level.
```
python runner.py
```
```
python runner_2_dogs.py
```

Parameters of the program can be set in the [config.ini](https://github.com/mh4043/CollectiveBehavour-GroupC/blob/main/code/config.ini) file. The variables itself in the file are very descriptive. However, you can still help with the [file](https://github.com/mh4043/CollectiveBehavour-GroupC/blob/main/docs/variables%20and%20equations%20descriptions.md), containing some deeper explanations, which has already been mentioned before.

## References
<a id="1">[1]</a>
Y. Liu, X. Li, M. Lan, Y. He, H. Cai and H. Gao, "Sheepdog Driven Algorithm for Sheep Herd Transport," 2021 40th Chinese Control Conference (CCC), Shanghai, China, 2021, pp. 5390-5395, doi: 10.23919/CCC52363.2021.9549396.
