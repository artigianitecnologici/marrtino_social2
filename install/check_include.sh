sudo cp $HOME/src/social/install/include/face_tracker_control/centroid.h $HOME/ros/catkin_ws/devel/include/face_tracker_control/centroid.h
sudo cp $HOME/src/social/install/include/face_tracker_pkg/centroid.h $HOME/ros/catkin_ws/devel/include/face_tracker_pkg/centroid.h
cd $HOME/ros/catkin_ws
catkin_make -j1