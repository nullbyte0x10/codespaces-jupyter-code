import math
import random
from typing import TextIO

Q_LIMIT = 100
BUSY = 1
IDLE = 0
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
def initialize():
    pass


def timing():
    pass


def arrive():
    pass


def depart():
    pass


def report():
    pass


def update_time_avg_stats():
    pass


def expon(mean):
    """"
    Generate a random number from an exponential distribution with a given mean

    Args:
        mean(float): The mean of exponential distribution.

    Returns:
        float: A random number from exponential distribution
    """

    return random.expovariate(1.0 / mean)


# the main function
def main():
    # open the input and output files
    infile: TextIO = open("mm1.out", "r")
    outfile: TextIO = open("mm1.out", "w")
    # specify number of events for timing function
    num_events = 2

    # read input parameters
    with open(infile) as infile:
        # read first line and split in 3 parts
        line = infile.readline().strip()
        parts = line.split()
        # convert each to appropriate data type
        mean_interarrival: float = float(parts[0])
        mean_service: float = float(parts[1])
        num_delays_required: int = int(parts[2])
    # write report heading an input parameters
