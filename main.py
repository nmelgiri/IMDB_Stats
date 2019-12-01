import pandas as pd


def get_east_west_dataframes():
	player_name_height = pd.read_csv("data/all_seasons.csv")[["Player", "player_height"]].set_index("Player")
	player_name_team_salary = pd.read_csv("data/sportsref_download.csv")[["Player", "Tm", "2019-20"]].set_index(
		"Player")
	conjoined_dataframe = player_name_height.merge(
		player_name_team_salary,
		on="Player"
	)
	conjoined_dataframe = conjoined_dataframe.loc[~conjoined_dataframe.index.duplicated(keep="first")]
	eastern_dataframe = pd.DataFrame(conjoined_dataframe).iloc[0: 0]
	western_dataframe = pd.DataFrame(conjoined_dataframe).iloc[0: 0]
	western_teams = pd.read_csv("data/Short-forms-of-teams.csv")["Short form West"].values
	eastern_teams = pd.read_csv("data/Short-forms-of-teams.csv")["Short form East"].values
	
	acceptable_teams_western = ["MEM", "POR", "SAS", "GSW", "HOU"]
	acceptable_teams_eastern = ["CHI", "ORL", "IND", "PHI", "BOS"]
	
	for index, row in conjoined_dataframe.iterrows():
		team = row["Tm"]
		if team in western_teams and team in acceptable_teams_western:
			western_dataframe = western_dataframe.append(row)
		elif team in eastern_teams and team in acceptable_teams_eastern:
			eastern_dataframe = eastern_dataframe.append(row)
	
	return eastern_dataframe, western_dataframe


def main():
	eastern_dataframe, western_dataframe = get_east_west_dataframes()
	
	eastern_dataframe.to_csv("data/eastern.csv")
	western_dataframe.to_csv("data/western.csv")


if __name__ == '__main__':
	main()

