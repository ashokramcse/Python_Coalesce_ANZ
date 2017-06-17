'''
Created on 17-Jun-2017

@author: BALASUBRAMANIAM
'''
from pip._vendor.distlib.compat import raw_input
from anz_network.SubnetCalculator import calculate
subnetClass=raw_input('Enter Subnet Class')
noOfHosts=raw_input('Number of Hosts')
startingIP=raw_input('Starting IP Address')

calculate(subnetClass, noOfHosts, startingIP) 