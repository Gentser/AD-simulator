# AD-simulator

Please read carefuly readme in gym-duckietown. For making all this work you'd better use Ubuntu 18.04 and ROS melodic.
To run the simulator use ros/basic\_control.py script. If you run it and you can see a bot rotating on one place - than everything is fine. To make it stop you should change the demo\_node. (or just remove it)

Your task is:
1) To make a bot move through lane
2) It sholud not hit the wall (the edge of a road) for 1 minute after it has been launched
3) You should control your bot using ROS topics

To make a bot simply move (just as a control sample) launch `/ros/basic_control.py`
