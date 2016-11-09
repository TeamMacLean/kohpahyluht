import time
# import camera
import files
# import os
from dronekit import connect

# for testing ONLY
# import dronekit_sitl
# sitl = dronekit_sitl.start_default()
# connection_string = sitl.connection_string()
# print connection_string

# folder_path = None
print 'connecting...'
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
print 'connected, waiting...'


def on_mission_start():
    print 'on mission start'
    global folder_path
    folder_path = files.get_new_folder()
    print 'new path ' + folder_path
    return None


def on_mission_stop():
    print 'on mission end'
    global folder_path
    folder_path = None
    return None


# def on_waypoint(tag):
# if folder_path is not None:
# camera.snap_raw(os.path.join(folder_path, tag))


@vehicle.on_message('MISSION_ITEM_REACHED')
def listener(self, name, message):
    print 'REACHED MISSION TARGET:', message

    if vehicle.commands.next == 1:
        on_mission_start()

    print "Current Waypoint: %s" % vehicle.commands.next

    # print "of: %s" % vehicle.commands.count

    # print 'Local Location: %s' % vehicle.location.local_frame
    # print 'Attitude: %s' % vehicle.attitude
    # print 'Velocity: %s' % vehicle.velocity
    # print 'GPS: %s' % vehicle.gps_0

    # on_waypoint(name)
    return None


# @vehicle.on_message('MISSION_RECEIVED')
# def listener(self, name, message):
#     print 'mission received', name, message
#     return None


# @vehicle.on_message('STATE_VEHICLE_MODE')
# def listener(self, name, message):
#     print 'new mode', name, message
#     # TODO if auto start logging new data!!
#     # else stop logging
#
#     # if auto: on_mission_start()
#     # else on_mission_stop()
#
#     return None


# @vehicle.on_message('ATTITUDE')
# def listener(self, name, message):
#     print 'altitude: %s' % message


while True:
    time.sleep(1)
