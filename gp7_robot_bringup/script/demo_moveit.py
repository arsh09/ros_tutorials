#! /usr/bin/env python

# Imports 
import sys
import copy
import rospy
import moveit_commander


def main ():

    moveit_commander.roscpp_initialize(sys.argv)
    group_name = 'arm'
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',DisplayTrajectory,queue_size=20)



if __name__ == "__main__":

    rospy.init_node("remote_moveit_node")
    main()
    rospy.spin()