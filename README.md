# Stuff for the sensor placement project
In the model folder, there exists the model sdf files for the use in gazebo. Those with "_vis" need to be loaded with the livox plugin.

Inside the src folder is the editted for livox lidar simulation plugin(https://github.com/Livox-SDK/livox_laser_simulation). Codes are editted to now support multiple lidar visualization in one world. Also there is a simple python srcipt to generate some new scan patterns for custom lidar.

# Usage
Create the catkin workspace and follow the instructions in https://github.com/Livox-SDK/livox_laser_simulation.