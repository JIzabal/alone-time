"""Script to run some part of my project."""

import sys
sys.path.append('../')
import MyProjectFolder.my_module.schedule as sched

# Check for the right number of arguments
if len(sys.argv) != 2:
    sys.exit("Please give a valid number of arguments")

# Reads the file, gets the schedules, and then finds the free times
schedule = sched.read_file(sys.argv[1])
schedule_1, schedule_2 = sched.get_schedules(schedule)
print("You're free and your roommate is busy during:")
sched.find_free_time(schedule_1, schedule_2)

