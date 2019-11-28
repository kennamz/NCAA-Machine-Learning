import csv
import os
import numpy as np
from numpy import linalg as LA

def read_in_b_data():
    """
    Returns a vector b.
    Column 1 of b contains the ID, a 14-character string of the
        format SSSS_XXXX_YYYY, where SSSS is the four digit season number,
        XXXX is the four-digit TeamID of the lower-ID team, and YYYY is the
        four-digit TeamID of the higher-ID team. 
    Column 2 of b is a 1 if the lower numerical ID team in column 1 won,
        -1 if higher ID won.
    Reads data from NCAATourneySeeds.csv and NCAATourneyCompactResults.csv
    """
    seed_file = open(os.getcwd() + "/data/Stage2DataFiles/NCAATourneySeedsShort.csv")
    seed_reader = csv.reader(seed_file, delimiter = ',')
    next(seed_reader) # first line is header
    for row in seed_reader:
        print(row)
        ID = row[0] + "_" # puts year into ID string
    
    #results_file = open(os.getcwd() +"/data/Stage2DataFiles/NCAATourneyCompactResults.csv")
    #results_reader = csv.reader(results_file, delimiter = ',')


        
    #return [np.matrix()]

'''
def read_in_A_data():
    num_lines = sum(1 for line in file) # count the number of lines in the file
    num_columns = len(next(reader)) # read first line and count columns
    file.seek(0) # go back to beginning of file
    matA = np.zeros((num_lines, num_columns)) # make A

    return np.matrix(matA) 

def read_in_data():
    """
    Returns a list consisting of a matrix A and a vector b.
    Column 1 of both A and b contains the ID, a 14-character string of the
        format SSSS_XXXX_YYYY, where SSSS is the four digit season number,
        XXXX is the four-digit TeamID of the lower-ID team, and YYYY is the
        four-digit TeamID of the higher-ID team. 
    Column 2 of b is a 1 if the lower numerical ID team in column 1 won,
        -1 if higher ID won.
    Columns 2 through n of A consist of a wide range of data about each team,
        with even columns containing data about the lower numerical ID team and
        odd columns contatining data about the higher ID.
    Reads data from 
    """
    


    
'''

read_in_b_data()
