# teamstat_first.py
'''
This file adds more stats to the team stats csv

'''

print("importing pandas as pd")
import pandas as pd
print("importing numpy as np")
import numpy as np
import time

### Read in the files to be used as the dataframes. The recruit sheet only needs to be read in once.
### The second dataframe needs to be read in each time we change the sheet.
print("reading in csv file as df1")
df1 = pd.read_csv('/Users/aaronstreepy/Desktop/scrape_the_lane/teams-2018-09-30.csv')


## *********************** ADDING ADVANCED TEAM STATS *************************
## ****************************************************************************
## ****************************************************************************

# ************************ Team True Shot Percentages *************************

## NOTE: This is the team True Shot %
df1['coefficient'] = 0.475
df1['shot_factor'] = df1.FGA + (df1.coefficient * df1.FTA)
cond1 = df1.shot_factor.eq(0)
cond2 = df1.shot_factor.gt(0)
stat1 = 0
stat2 = df1.PTS / (2 * df1.shot_factor)
df1 = df1.assign(tmTS=np.select([cond1, cond2,],[stat1, stat2,]))

## NOTE: This the opponent's True Shot %
df1['coefficient'] = 0.475
df1['shot_factor'] = df1.opp_FGA + (df1.coefficient * df1.opp_FTA)
cond1 = df1.shot_factor.eq(0)
cond2 = df1.shot_factor.gt(0)
stat1 = 0
stat2 = df1.opp_PTS / (2 * df1.shot_factor)
df1 = df1.assign(opp_tmTS=np.select([cond1, cond2,],[stat1, stat2,]))

## NOTE: This is the difference between the team's TS% and their opponents
df1['TS_dif'] = 0
df1['TS_dif'] = df1['tmTS'] - df1['opp_tmTS']


# ********************** Team Effective Field Goal Percentages ****************

## NOTE: This is the team's Effective Field Goal %
df1['coefficient'] = 0.5
df1['three_point_factor'] = df1['coefficient'] * df1['3PM']
cond1 = df1.three_point_factor.eq(0)
cond2 = df1.three_point_factor.gt(0)
cond3 = df1.three_point_factor.lt(0)
stat1 = 0
stat2 = (df1.FGM + df1.three_point_factor) / df1.FGA
stat3 = (df1.FGM + df1.three_point_factor) / df1.FGA
df1 = df1.assign(tmEFG=np.select([cond1, cond2, cond3],[stat1, stat2, stat3]))

## NOTE: This is the opponent's Effective Field Goal %
df1['coefficient'] = 0.5
df1['three_point_factor'] = df1['coefficient'] * df1['opp_3PM']
cond1 = df1.three_point_factor.eq(0)
cond2 = df1.three_point_factor.gt(0)
cond3 = df1.three_point_factor.lt(0)
stat1 = 0
stat2 = (df1.opp_FGM + df1.three_point_factor) / df1.opp_FGA
stat3 = (df1.opp_FGM + df1.three_point_factor) / df1.opp_FGA
df1 = df1.assign(opp_tmEFG=np.select([cond1, cond2, cond3],[stat1, stat2, stat3]))

## NOTE: This is the difference between the team's EFG% and their opponents
df1['EFG_dif'] = 0
df1['EFG_dif'] = df1['tmEFG'] - df1['opp_tmEFG']


# ********************** Team OFFENSIVE REBOUNDING Percentages ****************

## NOTE: This is the team's offensive rebounding percentage
df1['tmOR%'] = 0
df1['tmOR%'] = df1['OR'] / (df1['OR'] + df1['opp_DR'])


## NOTE: This is the team's opponents' offensive rebounding percentage
df1['opp_tmOR%'] = 0
df1['opp_tmOR%'] = df1['opp_OR'] / (df1['opp_OR'] + df1['DR'])


# ********************** Team ASSIST Percentages ******************************
# What percentage of field goals are made on an assist
# Assists / Field Goals Made


## NOTE: This is the team's assist percentage
df1['tmAst%'] = 0
df1['tmAst%'] = df1['AST'] / df1['FGM']

## NOTE: This is the opponent's assist percentage
df1['opp_tmAst%'] = 0
df1['opp_tmAst%'] = df1['opp_AST'] / df1['opp_FGM']


# ********************** Possessions *******************************************
# Formula from https://www.basketball-reference.com/about/glossary.html
# I have broken this down into extra little pieces because the formula is long and somewhat complicated.
# Poss = total number of Possessions
# Poss_pg = average number of possessions per game
# part_one is the teams total number of possessions
# part_two is the opponents number of possessions
df1['Poss'] = 0
df1['Poss_pg'] = 0
df1['part_one'] = 0
df1['part_one'] = (df1['FGA'] + 0.4 * df1['FTA'] - 1.07 * (df1['OR'] / (df1['OR'] + df1['opp_DR'])) *
(df1['FGA'] - df1['FGM']) + df1['TO'])
df1['part_two'] = (df1['opp_FGA'] + 0.4 * df1['opp_FTA'] - 1.07 * (df1['opp_OR'] / (df1['opp_OR'] + df1['DR'])) *
                   (df1['opp_FGA'] - df1['opp_FGM']) + df1['opp_TO'])
df1['Poss'] = (df1['part_one'] + df1['part_two']) * .5
df1['Poss_pg'] = df1['Poss'] / df1['games']


# ********************** Tempo ************************************************
# Formula from kenpom
# tempo
# tempo per 40 minutes
'''
Tempo: We can estimate possessions very well from box score stats by using this formula:
FGA-OR+TO+0.475xFTA.
For each team, possessions are counted for the team and their opponents, and then averaged.
A team’s average tempo is total possessions divided by minutes.

'''
df1['tempo_team'] = (df1['FGA'] - df1['OR'] + df1['TO'] + 0.475 * df1['FTA']) / (df1['minutes'] / 5)
df1['tempo_opp'] = (df1['opp_FGA'] - df1['opp_OR'] + df1['opp_TO'] + 0.475 * df1['opp_FTA']) / (df1['opp_minutes'] / 5)
df1['tempo'] = 0
df1['tempo'] = (df1['tempo_team'] + df1['tempo_opp']) * .5
df1['t40'] = df1['tempo'] * 40

# ********************** Team Steal Percentage  *******************************
# Team Steals / Team Possessions

df1['tmStl%'] = df1['STL'] / df1['Poss']
df1['opp_tmStl%'] = df1['opp_STL'] / df1['Poss']

'''
The following description is for individual players.  We are creating a more
straight-forward formula for determining the number of steals a team has per
possessions it plays.

Basketball Reference: STL%
Steal Percentage (available since the 1973-74 season in the NBA); the formula is
100 * (STL * (Tm MP / 5)) / (MP * Opp Poss). Steal Percentage is an estimate of
the percentage of opponent possessions that end with a steal by the player while
he was on the floor.

Kenpom:
Steal Percentage (%Stls): This is the percentage of possessions that a player
records a steal shile he is on the court. It is computed by Steals/(%Min * Team
Possessions).
'''

# ********************** Team Block Percentage  *******************************
# Team Blocks / Team Possessions

df1['tmBlk%'] = df1['BLK'] / df1['Poss']
df1['opp_tmBlk%'] = df1['opp_BLK'] / df1['Poss']


# ********************** Team Turnover Percentage  ****************************
# Team Turnovers / Team Possessions

df1['tmTo%'] = df1['TO'] / df1['Poss']
df1['opp_tmTo%'] = df1['opp_TO'] / df1['Poss']


# ********************** Team Free Throw Rate  *** ****************************
# team FTA / FGA

df1['tmFTrate'] = df1['FTA'] / df1['FGA']
df1['opp_tmFTrate'] = df1['opp_FTA'] / df1['opp_FGA']

# ********************** Offensive Rating  *** ****************************
# points per 100 possesions
# (team points / team possessions) * 100

df1['Off_Eff'] = (df1['PTS'] / df1['Poss']) * 100
df1['Def_Eff'] = (df1['opp_PTS'] / df1['Poss']) * 100

###########
#Write the results of the dataframe to csv
# add a timestamp to the file name

td = time.strftime("%Y-%m-%d-%H%M")
#panda_recruits = "panda_recruits_" + td +".xlsx"
#df1.to_excel(panda_recruits, sheet_name='sheet1', index = False)




#short_pandas = "short_pandas2_" + td + ".xlsx"
#df3.to_excel(short_pandas, sheet_name='pgR', index = False)



writer = pd.ExcelWriter('team_pandas3_' + td + '.xlsx')
df1.to_excel(writer,"all")
