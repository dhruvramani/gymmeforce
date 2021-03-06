# GymmeForce  
*Work in progress...*  
GymmeForce provides a framework for rapid experimentation with popular Deep Reinforcement Learning algorithms, it focus on making very easy to implement new ideias, which can be rapidly evaluated using [OpenAI Gym](https://github.com/openai/gym).  

## Installation
```bash
git clone https://github.com/lgvaz/gymmeforce.git  
cd gymmeforce  
pip install -e .  
```

## About  
[TensorFlow](https://www.tensorflow.org/) implementation of [DQN](https://www.nature.com/nature/journal/v518/n7540/full/nature14236.html?foxtrotcallback=true) for solving [OpenAI-Gym](https://gym.openai.com/) discrete environments.  
Episode 0 ---------------- Episode 3500 ----------- Episode 6000 ----------- Episode 7500 ----------- Episode 21500  
![episode 0](assets/ep0_nolegend.gif)
![episode 3500](assets/ep3500_nolegend.gif)
![episode 6000](assets/ep6000_nolegend.gif)
![episode 7500](assets/ep7500_nolegend.gif)
![episode 21500](assets/ep21500_nolegend.gif)  
<img src="assets/cart_pole.gif" width="280" height="200" />
<img src="assets/acrobot.gif" width="280" height="200" />
<img src="assets/lunar_lander.gif" width="280" height="200" />  
**DQN on Breakout**  
Mean reward after training: 421 (100 episodes)  
Dark blue: Standard DQN  
Light blue: Double DQN  
![Breakout reward](assets/breakout_plots.png)  
