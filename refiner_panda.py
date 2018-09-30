print("importing pandas as pd")
import pandas as pd
print("importing numpy as np")
import numpy as np
import time

### Read in the files to be used as the dataframes. The recruit sheet only needs to be read in once.
### The second dataframe needs to be read in each time we change the sheet.
print("reading in csv file as df1")
df1 = pd.read_csv('/Users/aaronstreepy/Desktop/scrape_the_lane_homework/2018-09-27-0930.csv',)



### ADD KmGmSc per minute Stat
### The per minute stat is only applied if the player ranks in the top 320 total Game Scores (thus
#### eliminating players with small sample size)

df1 = df1.sort_values(['KmGmSc','GmSc'], ascending=[False,False])
df1['KGSrank'] = range(1, len(df1) + 1)

df1["GS3"] = df1.shape[0] * ['Filling it']
df1["GS3"] = 0
df1.loc[df1.KGSrank < 1280, 'GS3'] = df1['KmGmSc']/df1['Min']
df1 = df1.round({'GS3': 3})
# df1.sort_values(['GS3', 'KmGmSc'], ascending=[False,False])

df1["GS30"] = df1['KmGmSc']/df1['Min']

df1['MPG'] = df1['Min']/df1['Gms']
df1 = df1.round({'MPG': 1})


#### ROUNDING SOME NUMBERS BEFORE OUTPUT
df1 = df1.round({'PPG': 1, 'RPG': 1, 'APG': 1, 'SPG': 1, 'BPG': 1, 'TOPG': 1,})






print("Adding L31 to the sheet now ... ")
####League 31 Stat Added
# L31
df1['L31'] = df1.shape[0]*['Filing Now']
df1['L31'] = (df1['PPG']*1) + (df1['TRPG']*1.25) + (df1['APG']*1.615) + (df1['SPG']*6.109) + (df1['BPG']*4.129) - (df1['TOPG']*3.325)

print("Adding Offensive Player of the Year to the sheet now ... ")
####OFFENSIVE PLAYER OF THE YEAR
#OFFPY
df1['OFFPY'] = df1.shape[0]*['Filing Now']
df1['OFFPY'] = (df1['PPG']*1.5) + (df1['TRPG']*.3) + (df1['APG']*2.5) - (df1['TOPG']*2)

print("Adding Defensive Player of the Year to the sheet now ... ")
####DEFENSIVE PLAYER OF THE YEAR
#DEFPY
df1['DEFPY'] = df1.shape[0]*['Filing Now']
df1['DEFPY'] = (df1['TRPG']*1) + (df1['SPG']*6) + (df1['BPG']*3)

df1['OFFPM'] = df1.shape[0]*['Filing Now']
df1['DEFPM'] = df1.shape[0]*['Filing Now']
df1['OFFPM'] = df1['OFFPY']/df1['MPG']
df1['DEFPM'] = df1['DEFPY']/df1['MPG']

#### ROUNDING SOME NUMBERS BEFORE OUTPUT
df1 = df1.round({'PPG': 1, 'RPG': 1, 'APG': 1, 'SPG': 1, 'BPG': 1, 'TOPG': 1, 'L31': 1, 'OFFPM': 3,
'DEFPM': 3, 'GS30': 3})






#####THIS CREATES A NEW POSITION COLUMN THAT SHOULD ALLOW LOOKUP TO WORK WITH IT TO PULL IN HISTORICAL DATA
### IT CONVERTS THE GAME POSITIONS TO ONE OF FIVE REAL LIFE POSITIONS
## IT SETS NAN POSITIONS TO CENTER
print("Converting Positions Now ....")
df1['N_Pos'] = df1.shape[0] * ["C"]
df1['Pos_Count'] = df1["Pos"].str.len()
df1.loc[df1['Pos_Count'] > 2, 'N_Pos'] = df1['Pos'].str[1:3]


df1.loc[df1['Pos'] == "PF, bC, bPF", 'N_Pos'] = "PF"


df1.loc[df1['Pos'] == "SF, bC", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, bPF", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, bSF", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, bSG", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, bPG", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, PG", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, SG", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, PF", 'N_Pos'] = "SF"
df1.loc[df1['Pos'] == "SF, C", 'N_Pos'] = "SF"

df1.loc[df1['Pos'] == "SG, bC", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, bPF", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, bSF", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, bSG", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, bPG", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, PG", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, SF", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, PF", 'N_Pos'] = "SG"
df1.loc[df1['Pos'] == "SG, C", 'N_Pos'] = "SG"

df1.loc[df1['Pos'] == "PG, bC", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, bPF", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, bSF", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, bSG", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, bPG", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, SG", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, SF", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, PF", 'N_Pos'] = "PG"
df1.loc[df1['Pos'] == "PG, C", 'N_Pos'] = "PG"

df1.loc[df1['Pos'] == "C, bC", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, bPF", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, bSF", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, bSG", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, bPG", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, SG", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, SF", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, PF", 'N_Pos'] = "C"
df1.loc[df1['Pos'] == "C, PG", 'N_Pos'] = "C"

df1.loc[df1['Pos'] == "PF, bC", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, bPF", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, bSF", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, bSG", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, bPG", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, SG", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, SF", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, C", 'N_Pos'] = "PF"
df1.loc[df1['Pos'] == "PF, PG", 'N_Pos'] = "PF"

df1.loc[df1['Pos_Count']<= 2, 'N_Pos'] = df1['Pos']
df1.loc[df1['N_Pos'] == "bC", 'N_Pos'] = "C"


df1.loc[(df1['N_Pos'] != "PG") & (df1['N_Pos'] != "SG") & (df1['N_Pos'] != "SF") & (df1['N_Pos'] != "PF") & (df1['N_Pos'] != "C"), 'N_Pos'] = 'C'







############## In order to get the percentile ratings to work we need to update the lookup sheets
##             to include all positions including bPG, bSG, bSF, bPF, bC, NA.



print("Adding Points Percentile data to the sheet now ... ")
### PERCENTILE POINTS OR Pperc
# Creating a new column and holding its place with "Filling Now"
df1['PpercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the PPG and casts them as a string.
df1['PpercL'] = df1['N_Pos'].astype(str) + " " + df1['PPG'].astype(str)
# This reads in the new sheet to convert Points to Percentiles
# NOTE: I may want to put something like print("calculating points percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Pperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results



print("Adding Rebounds Percentile data to the sheet now ... ")
### PERCENTILE Rebounds OR Rperc
# Creating a new column and holding its place with "Filling Now"
df1['RpercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the RPG and casts them as a string.
df1['RpercL'] = df1['N_Pos'].astype(str) + " " + df1['TRPG'].astype(str)
# This reads in the new sheet to convert Rebounds to Percentiles
# NOTE: I may want to put something like print("calculating Rebound percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Rperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results

print("Adding Assists Percentile data to the sheet now ... ")
### PERCENTILE Assists OR Aperc
# Creating a new column and holding its place with "Filling Now"
df1['ApercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the APG and casts them as a string.
df1['ApercL'] = df1['N_Pos'].astype(str) + " " + df1['APG'].astype(str)
# This reads in the new sheet to convert Assists to Percentiles
# NOTE: I may want to put something like print("calculating Assist percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Aperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results

print("Adding Steals Percentile data to the sheet now ... ")
### PERCENTILE Steals OR Sperc
# Creating a new column and holding its place with "Filling Now"
df1['SpercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the SPG and casts them as a string.
df1['SpercL'] = df1['N_Pos'].astype(str) + " " + df1['SPG'].astype(str)
# This reads in the new sheet to convert Steals to Percentiles
# NOTE: I may want to put something like print("calculating Steal percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Sperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results

print("Adding Blocks Percentile data to the sheet now ... ")
### PERCENTILE Blocks OR Bperc
# Creating a new column and holding its place with "Filling Now"
df1['BpercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the SPG and casts them as a string.
df1['BpercL'] = df1['N_Pos'].astype(str) + " " + df1['BPG'].astype(str)
# This reads in the new sheet to convert Blocks to Percentiles
# NOTE: I may want to put something like print("calculating Blocks percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Bperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results

print("Adding Turnovers Percentile data to the sheet now ... ")
### PERCENTILE TURNOVERS OR Tperc
# Creating a new column and holding its place with "Filling Now"
df1['TpercL'] = df1.shape[0]*['Filling Now']
# This concatenate's the HS POS attribute with the TPG and casts them as a string.
df1['TpercL'] = df1['N_Pos'].astype(str) + " " + df1['TOPG'].astype(str)
# This reads in the new sheet to convert Blocks to Percentiles
# NOTE: I may want to put something like print("calculating Turnovers percentiles now .... ")
df2 = pd.read_excel('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/Lookups.xlsx',sheet_name='Tperc')
# Merging the two dataframes - We could redefine df1 immmediately here, but for bug checking
# and other consistencies, I prefer to output it as results and then redefine df1.
results = pd.merge(df1, df2)

# Redefine df1 as current results.
df1 = results


print("Adding Total Percentile data to the sheet now ... ")
### TOTAL PERC COLUMN ADDED HERE
# Total Perc is just the 0 to 1 scale of all 6 added up and divided by 6
df1['Total_PERC'] = df1.shape[0]*['Filling Now']
df1['Total_PERC'] = (df1['Pperc'] + df1['Rperc'] + df1['Aperc'] + df1['Sperc'] + df1['Bperc'] + df1['Tperc'])/6

print("Adding Weighted Percentile data to the sheet now ... ")
df1['Weighted_PERC'] = df1.shape[0]*['Filling Now']
df1['Weighted_PERC'] = (df1['Pperc']*.25) + (df1['Rperc']*.125) + (df1['Aperc']*.125) + (df1['Sperc']*.2) + (df1['Bperc']*.2) + (df1['Tperc']*.1)



####PERCENTILE BASED OFFENSIVE PLAYER OF THE YEAR
#OFFPY
df1['pOFFPY'] = df1.shape[0]*['Filling Now']
df1['pOFFPY'] = (df1['Pperc']*4.5) + (df1['Rperc']*.5) + (df1['Aperc']*2.5) + (df1['Tperc']*2.5)

df1['pOFFPM'] = df1.shape[0]*['Filling Now']

df1['pOFFPM'] = df1['pOFFPY'] / df1['MPG']


####PERCENTILE BASED DEFENSIVE PLAYER OF THE YEAR
#DEFPY
df1['pDEFPY'] = df1.shape[0]*['Filing Now']
df1['pDEFPY'] = (df1['Rperc']*3) + (df1['Sperc']*3) + (df1['Bperc']*4)

df1['pDEFPM'] = df1.shape[0]*['Filling Now']
df1['pDEFPM'] = df1['pDEFPY'] / df1['MPG']





print("reading in excel lookup file")
print("reading in HeightToInches lookup values")
# Height to Inches (Don't need to update this one since it is being called first.)
df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/dtl_college_ht_lookup.csv')

# Use the merge method to merge (or vlookup) the height to inches.  This will automatically add the inches
# column to the end
# We have added INCH to the columns and the appropriate # based on the Ht column.
print("adding inches to dataframe RESULTS")
results=pd.merge(df1, df2)

print("Updating df1 .... ")
# EXAM TO 2-POINT SCALE
#Update Dataframe #1
df1 = results








print("Adding Height Modifiers Now ")
df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/pgHt.csv')
results = pd.merge(df1, df2)
df1 = results

df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/sgHt.csv')
results = pd.merge(df1, df2)
df1 = results

df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/sfHt.csv')
results = pd.merge(df1, df2)
df1 = results

df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/pfHt.csv')
results = pd.merge(df1, df2)
df1 = results

df2 = pd.read_csv('/Users/aaronstreepy/Desktop/aaa_recruit_analyzer/cHt.csv')
results = pd.merge(df1, df2)
df1 = results



print("Creating Positional Scores Now ")
df1['pgRS'] = df1.shape[0]*['Filling Now']
df1['sgRS'] = df1.shape[0]*['Filling Now']
df1['sfRS'] = df1.shape[0]*['Filling Now']
df1['pfRS'] = df1.shape[0]*['Filling Now']
df1['cRS'] = df1.shape[0]*['Filling Now']


stats_coefficient = 3.25

print("Crunching Positional Scores")
df1['pgRS'] = (((df1['APG']*.25)+(df1['Pperc']*1) + (df1['Rperc']*.1) + (df1['Aperc']*1.9) + (df1['Sperc']*1.5) + (df1['Bperc']*.1) + (df1['Tperc']*1.4))* stats_coefficient) * df1['pgHt']
df1['sgRS'] = (((df1['PPG']*.1)+(df1['Pperc']*2.15) + (df1['Rperc']*.25) + (df1['Aperc']*.75) + (df1['Sperc']*1.85) + (df1['Bperc']*.25) + (df1['Tperc']*.75))* stats_coefficient) * df1['sgHt']
df1['sfRS'] = (((df1['SPG']*1)+(df1['Pperc']*1.5) + (df1['Rperc']*.7) + (df1['Aperc']*.65) + (df1['Sperc']*1.4) + (df1['Bperc']*0.75) + (df1['Tperc']*1))* stats_coefficient) * df1['sfHt']
df1['pfRS'] = (((df1['TRPG']*.15)+(df1['Pperc']*1.25) + (df1['Rperc']*1.25) + (df1['Aperc']*.5) + (df1['Sperc']*.5) + (df1['Bperc']*1.25) + (df1['Tperc']*.75))* stats_coefficient) * df1['pfHt']
df1['cRS'] = (((df1['BPG']*.3)+(df1['Pperc']*.85) + (df1['Rperc']*2.25) + (df1['Aperc']*.2) + (df1['Sperc']*.2) + (df1['Bperc']*2.25) + (df1['Tperc']*.25))* stats_coefficient) * df1['cHt']

# RANKING NEW STATS
df1 = df1.sort_values(['pgRS'], ascending=[False])
df1['pg_rnk'] = range(1, len(df1) + 1)

df1 = df1.sort_values(['sgRS'], ascending=[False])
df1['sg_rnk'] = range(1, len(df1) + 1)

df1 = df1.sort_values(['sfRS'], ascending=[False])
df1['sf_rnk'] = range(1, len(df1) + 1)

df1 = df1.sort_values(['pfRS'], ascending=[False])
df1['pf_rnk'] = range(1, len(df1) + 1)

df1 = df1.sort_values(['cRS'], ascending=[False])
df1['c_rnk'] = range(1, len(df1) + 1)

# ROUNDING NEW STATS
df1 = df1.round({'Weighted_PERC': 3, 'Total_PERC': 3, 'pOFFPY': 2, 'pDEFPY': 2, 'pOFFPM': 3, 'pDEFPM': 3, 'pgRS': 1, 'sgRS': 1, 'sfRS': 1, 'pfRS': 1,
'cRS': 1})







print("Selecting Worksheets to save to file and generating dataframes ...")
### Creating a second dataframe of just St. Martinville Mice players

df1 = df1[['Player', 'Team', 'Conf', 'Yr', 'Ht', 'Wt', 'Pos', 'Gms',
    'MPG', 'PPG','ORPG', 'DRPG', 'TRPG', 'APG', 'SPG', 'BPG', 'TOPG', 'PFpg', '+/-pg',
    'FG%', '2P%', '3P%', 'FT%', 'TS%', 'EFG%',
    'PP30', 'OR30', 'DR30','TR30', 'Ast30', 'Stl30', 'Blk30', 'To30', 'PF30', '+/- 30',
    'GmSc', 'KmGmSc', 'KGSrank', 'GS3', 'GS30','L31', 'OFFPY', 'OFFPM', 'DEFPY','DEFPM',
    'pOFFPY', 'pOFFPM','pDEFPY', 'pDEFPM','Pperc', 'Rperc', 'Aperc', 'Sperc', 'Bperc', 'Tperc', 'Total_PERC', 'Weighted_PERC',
    'FGM','FGA', '2PM', '2PA', '3PM', '3PA', 'FTM', 'FTA',
    'Min', 'Pts', 'OR', 'DR', 'TR', 'Ast', 'Stl', 'Blk', 'TO', 'PF', '+ / -',
    'pg_rnk', 'sg_rnk', 'sf_rnk', 'pf_rnk', 'c_rnk', 'N_Pos', 'Inch', 'pgRS', 'sgRS', 'sfRS', 'pfRS', 'cRS',
    'PId','Team #']]
df2 = df1[['Player', 'Team', 'Conf', 'Yr', 'Ht', 'Wt', 'Pos', 'Gms',
    'MPG', 'PPG','ORPG', 'DRPG', 'TRPG', 'APG', 'SPG', 'BPG', 'TOPG', 'PFpg', '+/-pg',
    'FG%', '2P%', '3P%', 'FT%', 'TS%', 'EFG%',
    'PP30', 'OR30', 'DR30','TR30', 'Ast30', 'Stl30', 'Blk30', 'To30', 'PF30', '+/- 30']]
df3 = df1[['Player', 'Team', 'Conf', 'Yr', 'Ht', 'Wt', 'Pos', 'Gms', 'MPG',
    'PP30', 'OR30', 'DR30','TR30', 'Ast30', 'Stl30', 'Blk30', 'To30', 'PF30', '+/- 30',
    'GmSc', 'KmGmSc', 'KGSrank', 'GS3', 'GS30','pg_rnk', 'sg_rnk', 'sf_rnk', 'pf_rnk', 'c_rnk']]
df4 = df1[['Player', 'Team', 'Conf', 'Yr', 'Ht', 'Wt', 'Pos', 'Gms',
    'FGM','FGA', 'FG%','2PM', '2PA','2P%', '3PM', '3PA','3P%', 'FTM', 'FTA','FT%',
    'Min', 'Pts', 'OR', 'DR', 'TR', 'Ast', 'Stl', 'Blk', 'TO', 'PF', '+ / -']]


'''
	Player	Team	Conf	Yr	Ht	Pos	Gms
    MPG PPG	ORPG	DRPG	TRPG	APG	SPG	BPG	TOPG	PFpg	+/-pg
    FG%	2P%	3P%	FT%	TS%	EFG%
    PP30	OR30	DR30	TR30	Ast30	Stl30	Blk30	To30	PF30	+/- 30
    GmSc	KmGmSc	KGSrank	GS3	GS30 L31 OFFPY	DEFPY	OFFPM	DEFPM
    Pperc	Rperc Aperc Sperc Bperc Tperc Total_PERC Weighted_PERC pOFFPY	pDEFPY
    FGM	FGA	2PM	2PA	3PM	3PA	FTM	FTA
    Min Pts	OR	DR	TR	Ast	Stl	Blk	TO	PF	+ / -
    pg_rnk	sg_rnk	sf_rnk	pf_rnk	c_rnk N_Pos Inch pgRS	sgRS	sfRS	pfRS	cRS
    PId	TeamNUM

    Delete the following categories
    	Pos_Count	PpercL		RpercL	ApercL		SpercL		BpercL		TpercL
    	pgHt	sgHt	sfHt	pfHt	cHt
'''





df5 = df1.loc[df1['Team'] == "St. Martinville Mice"]
df6 = df1.loc[df1['Conf'] == 9]
df7 = df1.loc[df1['Team'] == "Hartford Bullfrogs"]
df8 = df1.loc[df1['Team'] == "South Bend Diplomats"]
df9 = df1.loc[df1['Team'] == "Pittsburgh Predators"]
df10 = df1.loc[df1['Team'] == "Fort Worth Radiators"]
df11 = df1.loc[df1['Team'] == "El Paso Conquistadors"]
df12 = df1.loc[df1['Team'] == "Panama City phoenixs"]





print("Time Stamping the File Now ")
###########
#Write the results of the dataframe to csv
# add a timestamp to the file name

td = time.strftime("%Y-%m-%d-%H%M")
#panda_recruits = "panda_recruits_" + td +".xlsx"
#df1.to_excel(panda_recruits, sheet_name='sheet1', index = False)




#short_pandas = "short_pandas2_" + td + ".xlsx"
#df3.to_excel(short_pandas, sheet_name='pgR', index = False)

print("Saving to File")

writer = pd.ExcelWriter('refined_pandas_' + td + '.xlsx')
df1.to_excel(writer,"all")
df2.to_excel(writer,"per_game")
df3.to_excel(writer,"per_30")
df4.to_excel(writer,"totals")


df5.to_excel(writer,"SMC")
df6.to_excel(writer,"Conf_9")
df7.to_excel(writer,"HART")
df8.to_excel(writer,"SB")
df9.to_excel(writer,"PITT")
df10.to_excel(writer,"FW")
df11.to_excel(writer,"ELP")
df12.to_excel(writer,"PC")


'''
    1. Round Positional Scores
    2. Rank Positional Scores
    3. Add Percentile Defpm and Offpm
    4. Round Weighted Perc to 3
    5. Round Total Perc to 3
    6. Prior to output delete Raw Position Scores, Percentile Lookups, Pos_Count, N_Pos,
7. Display FG% in consistent method
    8. Display MPG at beginning of PPG Section
    9. Create Tab Worksheets



Todo:
    1. Move minutes per game to per game stats section.
    2. Move minutes to total stats section.
2b. Add rankings for various stats
3. Add Shot Distribution %s to spreadsheet
4. Add Point Distribution %s to spreadsheet (possible second worksheet?)
5. Update Percentile Lookups For College
5B. Create Tab/Worksheet Reports for various items:
    A. Percentiles
    B. Rankings
    C. Per Game Stats
    D. Per 30 Stats
    E. Totals
    F. Scout Page (My Favorites)
    G. EVENTUALLY: A Projected Ratings Page

    6. Finish position specific rankings (PG, SG, SF, PF, C)
7. Figure out how to add HS Recruiting DataFrame to Current Season DataFrame
8. Save Recruiting Files to a new and seperate folder
9. Delete old files after Updated
10. Save Lookup files to a dedicated universal folder
'''
