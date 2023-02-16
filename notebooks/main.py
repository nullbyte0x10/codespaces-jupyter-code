import random
import math

amount = 0
bigs = 0
initial_inv_level = 0
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 0
num_values_demand = 0
smalls = 0

area_holding = 0.0
area_shortage = 0.0
holding_cost = 0.0
incremental_cost = 0.0
maxlag = 0.0
mean_interdemand = 0.0
minlag = 0.0
prob_distrib_demand = [0.0] * 26
setup_cost = 0.0
shortage_cost = 0.0
sim_time = 0.0
time_last_event = 0.0
time_next_event = [0.0] * 5
total_ordering_cost = 0.0

def initialize():
    pass

def timing():
    pass

def order_arrival():
    pass

def demand():
    pass

def evaluate():
    pass

def report():
    pass

def update_time_avg_stats():
    pass

def expon(mean):
    return -mean * math.log(random.random())

def random_integer(prob_distrib):
    prob_sum = sum(prob_distrib)
    rand = random.uniform(0, prob_sum)
    cumulative_prob = 0.0
    for i, prob in enumerate(prob_distrib):
        cumulative_prob += prob
        if rand <= cumulative_prob:
            return i
    return len(prob_distrib) - 1
def uniform(a, b):
    return a + (b - a) * random.random()
#main function
def main():
    i,num_policies=0,0
    #open input and output files
    infile=open("inv.in","r")
    outfile=open("inv.out","w")
    #specify the number of events for the timing function
    num_events=4
    #read input parameters
    


