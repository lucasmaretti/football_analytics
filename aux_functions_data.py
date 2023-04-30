import pandas as pd
import json
from tqdm import tqdm

leagues= ['England', 'European_Championship', 'France', 'Germany', 'Spain', 'Italy', 'World_Cup']


def read_wyscout_event_data(path: str = './data/wyscout/events/', all_leagues: bool = True, leagues_to_read: list = None) -> pd.DataFrame:

    """
    Function returns a pandas dataframe of the Wyscout data for the events dataset.
    
    :param path: (str) string containing the file path to the event data
    :param all_leagues: (bool) If True, will return data for all the possible leagues available: 'England', 'European_Championship', 'France', 'Germany', 'Spain', 'Italy', 'World_Cup'
    :param leagues_to_read: (list) if all leagues are not desired, user must pass a list of desired leagues
    :return: pandas Dataframe with the event data loaded
    """
    event_dataframes = []

    if all_leagues:

        for league in tqdm(leagues):
            with open(path + 'events_'+league+'.json') as f:
                print(f"Working on {league} file")
                json_data = json.load(f) # lê o arquivo json dos eventos
                pandas_data = pd.DataFrame(json_data) # transforma em pandas dataframe
                pandas_data['league'] = str(league)
                event_dataframes.append(pandas_data) # adiciona na lista event_dataframes
    
    else:
        if leagues_to_read is None:
            raise ValueError("If not all leagues are desired, a list leagues_to_read must be provided.")
        
        else:

            for league in leagues_to_read:
                with open(path + 'events_'+league+'.json') as f:
                    print(f"Working on {league} file")
                    json_data = json.load(f) # lê o arquivo json dos eventos
                    pandas_data = pd.DataFrame(json_data) # transforma em pandas dataframe
                    event_dataframes.append(pandas_data) # adiciona na lista event_dataframes


    print("Concatenating dataframes")
    all_events_df = pd.concat(event_dataframes, axis=0).reset_index(drop=True) # concatenando todos os eventos da lista de eventos

    return all_events_df

####################################################################################################################################

def read_wyscout_match_data(path: str = './data/wyscout/matches/', all_leagues: bool = True, leagues_to_read: list = None) -> pd.DataFrame:

    """
    Function returns a pandas dataframe of the Wyscout data for the matches dataset.
    
    :param path: (str) string containing the file path to the event data
    :param all_leagues: (bool) If True, will return data for all the possible leagues available: 'England', 'European_Championship', 'France', 'Germany', 'Spain', 'Italy', 'World_Cup'
    :param leagues_to_read: (list) if all leagues are not desired, user must pass a list of desired leagues
    :return: pandas Dataframe with the matches data loaded
    """
    matches_dataframes = []

    if all_leagues:

        for league in tqdm(leagues):
            with open(path + 'matches_'+league+'.json') as f:
                print(f"Working on {league} file")
                json_data = json.load(f) # lê o arquivo json dos eventos
                pandas_data = pd.DataFrame(json_data) # transforma em pandas dataframe
                pandas_data['league'] = str(league)
                matches_dataframes.append(pandas_data) # adiciona na lista event_dataframes
    
    else:
        if leagues_to_read is None:
            raise ValueError("If not all leagues are desired, a list leagues_to_read must be provided.")
        
        else:    
            for league in leagues_to_read:
                with open(path + 'matches_'+league+'.json') as f:
                    print(f"Working on {league} file")
                    json_data = json.load(f) # lê o arquivo json dos eventos
                    pandas_data = pd.DataFrame(json_data) # transforma em pandas dataframe
                    matches_dataframes.append(pandas_data) # adiciona na lista event_dataframes

    for i in tqdm(matches_dataframes):
        print("Concatenating dataframes")
        all_matches_df = pd.concat(matches_dataframes, axis=0).reset_index(drop=True) # concatenando todos os eventos da lista de eventos

    return all_matches_df

###############################################################################################################################

def read_wyscout_player_data(path: str = './data/wyscout/') -> pd.DataFrame:


    """
    Function returns a pandas dataframe of the Wyscout data for the players dataset.
    
    :param path: (str) string containing the file path to the event data
    :return: pandas Dataframe with the players data loaded

    """

    with open(path+'players.json') as f:
        player_json=json.load(f)
        player_df = pd.DataFrame(player_json)

    return player_df
