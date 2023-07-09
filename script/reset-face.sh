rostopic pub -1 /social/emotion std_msgs/String "startblinking"  
rostopic pub -1 /tilt_controller/command std_msgs/Float64 0
rostopic pub -1 /pan_controller/command std_msgs/Float64 0
