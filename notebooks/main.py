
import math
import random
Q_LIMIT=100
BUSY=1
IDLE=0
# Global variables
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_events = 0
num_in_q = 0
server_status = 0
area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_last_event = 0.0
time_next_event = [0.0] * 3
total_of_delays = 0.0
infile = None
outfile = None
# Function prototypes
