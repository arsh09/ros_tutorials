### Introduction 

This project is related to a series of tutorials on How to simulate any industrial robotic arm using ROS. 


Please follow the tutorial video at this [link](https://www.youtube.com/watch?v=7pjogRqbmIk)


### How to run 

1 - Clone the repo in your workspace 
```bash
$ cd path-to-your-workspace-folder/src
$ git clone https://github.com/arsh09/ros_tutorials.git
```

2 - Catkin make the package 

```bash
$ cd ..
$ catkin_make
```

3 - Source and run the control simulation file

```bash
$ source devel/setup.bash
$ roslaunch gp7_visualization control_gazebo.launch
```

