import csv
import os
import numpy as np
from numpy import linalg as LA
from itertools import combinations 

def read_in_b_data():
    """
    Returns a numpy matrix b.
    Column 1 of b contains the ID, a 14-character string of the
        format SSSS_XXXX_YYYY, where SSSS is the four digit season number,
        XXXX is the four-digit TeamID of the lower-ID team, and YYYY is the
        four-digit TeamID of the higher-ID team. 
    Column 2 of b is a 1 if the lower numerical ID team in column 1 won,
        -1 if higher ID won.
    Reads data from NCAATourneySeeds.csv and NCAATourneyCompactResults.csv
    """
    ########
    # Get the TeamID for each year for each team to make the first column of b
    ########
    # open seed file
    seed_file = open(os.getcwd() + "/data/Stage2DataFiles/NCAATourneySeeds.csv")
    seed_reader = csv.reader(seed_file, delimiter = ',')
    # get first year
    next(seed_reader) # first line is header
    first_year = next(seed_reader)[0]
    seed_file.seek(0)
    next(seed_reader) # first line is header
    
    prev_year = first_year
    IDs = []
    teams = []
    for row in seed_reader:
        if (row[0] == prev_year):
            teams.append(row[2])
        else: 
            combos = list(combinations(teams, 2))
            for team_pair in combos:
                if int(team_pair[0]) < int(team_pair[1]):
                    ID = prev_year + "_" + team_pair[0] + "_" + team_pair[1]
                else:
                    ID = prev_year + "_" + team_pair[1] + "_" + team_pair[0]
                IDs.append(ID)
            teams = []
            combos = []
            teams.append(row[2])
        prev_year = row[0]
    combos = list(combinations(teams, 2))
    for team_pair in combos:
        if int(team_pair[0]) < int(team_pair[1]):
            ID = prev_year + "_" + team_pair[0] + "_" + team_pair[1]
        else:
            ID = prev_year + "_" + team_pair[1] + "_" + team_pair[0]
        IDs.append(ID)
    
    ########
    # Get whether each team won (1), lost (-1), or did not play (0)
    ########
    #results_file = open(os.getcwd() +"/data/Stage2DataFiles/NCAATourneyCompactResults.csv")
    #results_reader = csv.reader(results_file, delimiter = ',')


        
    #return [np.matrix(IDs)]

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
