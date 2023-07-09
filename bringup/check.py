from __future__ import print_function

import sys, os, time
import rospy
import rosnode
import tf

from sensor_msgs.msg import LaserScan, Range, Image
from nav_msgs.msg import Odometry

nodenames = []
topicnames = []

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def printOK():
    print('%sOK%s' %(OKGREEN,ENDC))

def printFail():
    print('%sFAIL%s' %(FAIL,ENDC))

def check_ROS_q():
    r = True
    try:
        rosnode.get_node_names()
    except Exception as e:
        r = False
    return r

def get_ROS_nodes():
    global nodenames
    try:
        nodenames = rosnode.get_node_names()
    except Exception as e:
        #print e
        pass

def get_ROS_topics():
    global topicnames
    try:
        topicnames = rospy.get_published_topics()
    except Exception as e:
        #print e
        pass

def check_ROS():
    global nodenames, topicnames
    #print('----------------------------------------')
    #print('Check ROS...')
    nodenames = []
    topicnames = []
    r = True
    try:
        nodenames = rosnode.get_node_names()
        #print('  -- Nodes: %s' %nodenames)
        topicnames = rospy.get_published_topics()
        #print('  -- Topics: %s' %topicnames)
        printOK()
    except Exception as e:
        print(e)
        r = False
        printFail()
    return r


def print_result(r):
    if r:
        printOK()
    else:
        printFail()


def check_it(what):
    fname = 'check_%s()' %what
    print('Running %s ...' %fname)
    return eval(fname)


def check_robot():
    global nodenames
    get_ROS_nodes()

    print('----------------------------------------')
    print('Check orazio robot ...')

    r = '/orazio' in nodenames
    print_result(r)
    return r

def check_social():
    global nodenames
    get_ROS_nodes()

    print('----------------------------------------')
    print('Check social robot ...')
    print('----------------------------------------')
    print(nodenames)
    print('----------------------------------------')
    r = '/face_controller' in nodenames
    print_result(r)
    print(r)
    return r


def check_turtle():
    global nodenames
    get_ROS_nodes()

    print('----------------------------------------')
    print('Check Turtlebot robot ...')

    r = '/mobile_base' in nodenames
    print_result(r)
    return r




def check_simrobot():
    global nodenames
    get_ROS_nodes()

    print('----------------------------------------')
    print('Check Stage simulator ...')

    r = '/stageros' in nodenames
    print_result(r)
    return r


odomcount = 0
odomframe = ''

robot_pose = [0, 0, 0]

def odom_cb(data):
    global robot_pose, odomcount, odomframe
    robot_pose[0] = data.pose.pose.position.x
    robot_pose[1] = data.pose.pose.position.y
    o = data.pose.pose.orientation
    q = (o.x, o.y, o.z, o.w)
    euler = tf.transformations.euler_from_quaternion(q)
    robot_pose[2] = euler[2] # yaw
    odomcount += 1
    odomframe = data.header.frame_id


def check_odom():
    global topicnames, odomcount, odomframe
    odomrate = 0

    print('----------------------------------------')
    print('Check odometry ...')

    get_ROS_topics()
    r = ['/odom', 'nav_msgs/Odometry'] in topicnames

    if r:
        odomcount = 0
        odom_sub = rospy.Subscriber('odom', Odometry, odom_cb)
        dt = 2.0
        time.sleep(dt)
        odom_sub.unregister()
        odomrate = odomcount/dt
        print('  -- Odometry rate = %.2f Hz' %(odomrate))
        print('  -- Odometry frame = %s' %(odomframe))

    print_result(r)
    return odomrate


sonarcount = 0
sonarframe = ''
sonarvalues = [0,0,0,0,0,0,0,0]
idsonar = 0

def sonar_cb(data):
    global sonarcount, sonarframe, idsonar
    sonarcount += 1
    sonarframe = data.header.frame_id
    r = (data.range*0.75)/0.265 #scale the value of the range in meters
    sonarvalues[idsonar] = r

def check_sonar():
    global topicnames, sonarcount, sonarframe, sonarvalues, idsonar
    r = True
    print('----------------------------------------')
    print('Check sonar ...')
    for i in range(0,4):
        sname = 'sonar_%d' %i
        idsonar = i
        if ['/'+sname, 'sensor_msgs/Range'] in topicnames:
            sonarcount = 0
            sonar_sub = rospy.Subscriber(sname, Range, sonar_cb)
            dt = 3.0
            time.sleep(dt)
            sonar_sub.unregister()
            print('  -- Sonar %d scan rate = %.2f Hz' %(i,sonarcount/dt))
            print('  -- Sonar %d frame = %s' %(i,sonarframe))
            print('  -- Sonar %d range = %.2f' %(i,sonarvalues[i]))
        else:
            r = False

    print_result(r)
    return r


def getSonarValues():
    global sonarvalues
    return sonarvalues

def getSonarValue(i):
    global sonarvalues, idsonar
    idsonar = i
    sname = 'sonar_%d' %i
    sonar_sub = rospy.Subscriber(sname, Range, sonar_cb)
    dt = 1.5
    time.sleep(dt)
    sonar_sub.unregister()
    return sonarvalues[i]


# Laser

lasercount = 0
laserframe = ''

def laser_cb(data):
    global lasercount, laserframe
    lasercount += 1
    laserframe = data.header.frame_id


def check_laser():
    global topicnames, lasercount, laserframe

    print('----------------------------------------')
    print('Check laser scan ...')

    laserrate = 0
    get_ROS_topics()
    r = ['/scan', 'sensor_msgs/LaserScan'] in topicnames
    
    if r:
        lasercount = 0
        laser_sub = rospy.Subscriber('scan', LaserScan, laser_cb)
        dt = 2.0
        time.sleep(dt)
        laser_sub.unregister()
        laserrate = lasercount/dt
        print('  -- Laser scan rate = %.2f Hz' %(laserrate))
        print('  -- Laser frame = %s' %(laserframe))

    print_result(r)
    return laserrate


cameracount = 0
cameraframe = ''

def image_cb(data):
    global cameracount, cameraframe
    cameracount += 1
    cameraframe = data.header.frame_id
    #print('image')


def findImageTopic():
    global topicnames

    get_ROS_topics()
    if ['/kinect/rgb/image_raw', 'sensor_msgs/Image'] in topicnames:
        return '/kinect/rgb/image_raw'
    elif ['/rgb/image_raw', 'sensor_msgs/Image'] in topicnames:
        return '/rgb/image_raw'
    elif ['/usbcam/image_raw', 'sensor_msgs/Image'] in topicnames:
        return '/usbcam/image_raw'
    else:
        return None



def check_rgb_camera():
    global topicnames, cameracount, cameraframe

    print('----------------------------------------')
    print('Check RGB camera ...')

    get_ROS_topics()
    camerarate = 0

    topicim = findImageTopic()
    r = topicim is not None

    if r:
        cameracount = 0
        camera_sub = rospy.Subscriber(topicim, Image, image_cb)
        dt = 2.0
        time.sleep(dt)
        camera_sub.unregister()
        camerarate = cameracount/dt
        print('  -- RGB camera rate = %.2f Hz' %(camerarate))
        print('  -- RGB camera frame = %s' %(cameraframe))

    print_result(r)
    return camerarate

def findDepthTopic():
    global topicnames

    get_ROS_topics()

    if ['/depth/image_raw', 'sensor_msgs/Image'] in topicnames:
        return '/depth/image_raw'

    elif ['/kinect/depth/image_raw', 'sensor_msgs/Image'] in topicnames:
        return '/kinect/depth/image_raw'

    else:
        return None

def check_depth_camera():
    global topicnames, cameracount, cameraframe

    print('----------------------------------------')
    print('Check depth camera ...')

    get_ROS_topics()
    camerarate = 0

    topicim = findDepthTopic()
    r = topicim is not None

    if r:
        cameracount = 0
        camera_sub = rospy.Subscriber(topicim, Image, image_cb)
        dt = 2.0
        time.sleep(dt)
        camera_sub.unregister()
        camerarate = cameracount/dt
        print('  -- Depth camera rate = %.2f Hz' %(camerarate))
        print('  -- Depth camera frame = %s' %(cameraframe))
    
    print_result(r)
    return camerarate


tf_listener = None

# Note
# ROS param use_sim_time is not set when wsbringup is launched.
# Some features do not work when launching the simulator that sets use_sim_time to true
# but rospy gettime does not check this param if it is changed after rospy init...
# If you need simulation time, use 'rosparam set /use_sim_time true' before launching
# wsbringup.py

def check_tf(source, target):
    global tf_listener
    r = check_ROS_q()
    if (not r):
        return r
    if (tf_listener == None):
        print("tf_listener ...")  ### FIXME sometimes it blocks here ....
        tf_listener = tf.TransformListener()
    print("  -- TF %s -> %s  " %(source, target), end="")
    try:
        tf_listener.waitForTransform(source, target, rospy.Time(), rospy.Duration(1.0))
        (posn, rotn) = tf_listener.lookupTransform(source, target, rospy.Time())
        # how much time ago we get a transform (secs)
        ct = tf_listener.getLatestCommonTime(source, target).secs
        rt = rospy.Time.now().secs
        print("(tf common time %d) " %ct, end="")
        print("(rospy time %d) " %rt, end="")
        t = rt - ct
        print("time=%d " %t, end="")
        #if (t<3):
        printOK()
        #else:
        #    printFail()
        #    r = False
    except tf.Exception as e:
        print(" %s " %e, end="")
        printFail()
        r = False

    return r


def check_tfs():
    print('----------------------------------------')
    print('Check transforms ...')
    check_tf('map', 'odom')
    check_tf('odom', 'base_frame')
    check_tf('base_frame', 'laser_frame')
    check_tf('base_frame', 'rgb_camera_frame')
    check_tf('base_frame', 'depth_camera_frame')


def check_kinect():
    print('----------------------------------------')
    print('Check kinect ...')
    global nodenames
    get_ROS_nodes()
    r=[]
    r=[node for node in nodenames if 'kinect' in node]
    if len(r)!=0:
        printOK()
        r= True
    else:
        printFail()
        r= False
    return r


def check_node(m, r):
    print('  --%s' %m, end="")
    if '/'+m in nodenames:
        printOK()
        t = True
    else:
        printFail()
        t = False
    r.append([m,t])


def check_nodes():
    r = []
    print('Check modules ...')
    check_node('gmapping',r)
    check_node('srrg_mapper2d',r)
    check_node('amcl',r)
    check_node('srrg_localizer',r)
    check_node('move_base_node',r)
    check_node('spqrel_planner',r)
    check_node('gradientBasedNavigation',r)
    check_node('astra',r)
    check_node('xtion2',r)
    check_node('usbcam',r)
    check_node('astralaser',r)
    check_node('xtion2laser',r)
    check_node('hokuyo',r)
    check_node('rplidar',r)
    check_node('joystick',r)
    check_node('apriltag_detector',r)

    return r

def main():
    r = check_ROS()
    if (r):
        rospy.init_node('marrtino_check')
        #check_simrobot()
        check_robot()
        check_social()
        check_odom()
        check_sonar()
        check_laser()
        check_rgb_camera()
        check_depth_camera()
        check_tfs()
        #check_kinect()
        check_nodes()


if __name__=='__main__':
    main()

