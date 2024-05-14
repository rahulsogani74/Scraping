"""
Summary:
This Python script utilizes Selenium and BeautifulSoup to scrape cricket data from the Cricbuzz website. 
It extracts points table data and scoreboard data for the first and second innings of a match, then 
stores the data in separate dictionaries. The script then creates DataFrames from the dictionaries 
and saves them to an Excel file named 'Cricket_Data.xlsx'.
"""


# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time


# Initializing dictionaries to store data
data_points_table = {"Team_Name" : [], "Total_Match" : [], "Won" : [], "Lost" : [], "Points" : [], "NRR" : []}

data_first_inn_scoreboard_header = {"Cricket_data" : []}
data_first_inn_scoreboard_batter = {"Player Name" : [], "Status" : [], "R" : [], "B" : [], "4s" : [], "6s" : [], "SR" : []}
data_first_inn_scoreboard_bowler = {"Player Name" : [], "O" : [], "M" : [], "R" : [], "W" : [], "ECO" : []}

data_sec_inn_scoreboard_header = {"Cricket_data" : []}
data_sec_inn_scoreboard_batter = {"Player Name" : [], "Status" : [], "R" : [], "B" : [], "4s" : [], "6s" : [], "SR" : []}
data_sec_inn_scoreboard_bowler = {"Player Name" : [], "O" : [], "M" : [], "R" : [], "W" : [], "ECO" : []}

# Initializing Chrome WebDriver instance
driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
#time.sleep(3)

actions = ActionChains(driver, duration=2)


"""
----------------------------------------- Points Table ----------------------------------------------
"""    

# Clicking on the 'Points Table' link
points_table_element = driver.find_element("xpath", "//a[text()= 'Points Table']")
actions.click(points_table_element).perform()

# Extracting data from the points table
points_table = driver.find_element("xpath", "//table[@class= 'table cb-srs-pnts']")
actions.click(points_table).perform()

points_table_html = points_table.get_attribute("innerHTML")

soup = BeautifulSoup(points_table_html, "html.parser")

Team_Names = soup.find_all(class_ = "cb-srs-pnts-name")

# for Team_Name in Team_Names:
#     print(Team_Name.text)

Total_Matchs = soup.find_all(class_ = "cb-srs-pnts-td")
# for Total_Match in Total_Matchs:
#     print(Total_Match.text)


for i in range(len(Team_Names)):
    team_name = Team_Names[i].text.strip()
    total_match = int(Total_Matchs[i * 7].text)
    won = int(Total_Matchs[i * 7 + 1].text)
    lost = int(Total_Matchs[i * 7 + 2].text)
    points = int(Total_Matchs[i * 7 + 5].text)
    nrr = float(Total_Matchs[i * 7 + 6].text)
    
    #print(team_name, total_match, won, lost, points, nrr)
    
    data_points_table["Team_Name"].append(team_name)
    data_points_table["Total_Match"].append(total_match)
    data_points_table["Won"].append(won)
    data_points_table["Lost"].append(lost)
    data_points_table["Points"].append(points)
    data_points_table["NRR"].append(nrr)
    
 
"""
----------------------------------------- Scoreboard Data ----------------------------------------------
"""    

# Clicking on the 'Schedule & Results' link and then selecting the first match for scoreboard data
Results_element = driver.find_element("xpath", "//a[text()= 'Schedule & Results']")
actions.click(Results_element).perform()

#time.sleep(3)
Match_element = driver.find_element("xpath", "//a[@class = 'text-hvr-underline']")
actions.click(Match_element).perform()
#time.sleep(3)
scoreboard_element = driver.find_element("xpath", "//a[text()= 'Scorecard']")
actions.click(scoreboard_element).perform()

#time.sleep(3)

# Extracting data from the first innings scoreboard
team_score_element = driver.find_element("xpath", "//div[@class = 'cb-col cb-col-67 cb-scrd-lft-col html-refresh ng-isolate-scope']")
actions.click(team_score_element).perform()

team_score_element_html = team_score_element.get_attribute("innerHTML")

soup1 = BeautifulSoup(team_score_element_html, "html.parser")

result_Name = soup1.find(class_ = 'cb-col cb-scrcrd-status cb-col-100 cb-text-complete ng-scope').text
data_first_inn_scoreboard_header["Cricket_data"].append(result_Name)

#print(result_Name)

def inningsData(innings):
    if innings:
        team_name = innings.find(class_="cb-col cb-col-100 cb-scrd-hdr-rw").text.strip()
        data_first_inn_scoreboard_header["Cricket_data"].append(team_name)
        #print("Team:", team_name)
        
        # scoreboard_header = innings.find(class_ = "cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray").text.strip()
        # data_scoreboard["Player Name"].append(scoreboard_header)
        
        players_data = innings.find_all(class_='cb-col cb-col-100 cb-scrd-itms')
        
        for player_data in players_data:
            #print(player_data.text.strip())
            
            player_name_tag = player_data.find(class_ = 'cb-col cb-col-25')
    
            # Check if player name is found
            if player_name_tag:
                player_name = player_name_tag.text.strip()
                status = player_data.find(class_='cb-col cb-col-33').text.strip()
                runs = player_data.find(class_='cb-col cb-col-8 text-right text-bold').text.strip()
                balls = player_data.find(class_='cb-col cb-col-8 text-right').text.strip()
                fours = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().text.strip()
                sixes = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().text.strip()
                srr = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().find_next_sibling().text.strip()

                    
                # print("Player Name:", player_name)
                # print("Out:", out)
                # print("Runs:", runs)
                # print("Balls Faced:", balls)
                # print("Fours:", fours)
                # print("Sixes:", sixes)
                # print("Strike Rate:", srr)
    
                data_first_inn_scoreboard_batter["Player Name"].append(player_name)
                data_first_inn_scoreboard_batter["Status"].append(status)
                data_first_inn_scoreboard_batter["R"].append(runs)
                data_first_inn_scoreboard_batter["B"].append(balls)
                data_first_inn_scoreboard_batter["4s"].append(fours)
                data_first_inn_scoreboard_batter["6s"].append(sixes)
                data_first_inn_scoreboard_batter["SR"].append(srr)
            else:
                break
            
            
        #players_data = innings.find_all(class_='cb-col cb-col-100 cb-scrd-itms ')
        
        
        for player_data in players_data:
            #print(player_data.text.strip())
            
            player_name_tag = player_data.find(class_ = 'cb-col cb-col-38')
    
            # Check if player name is found
            if player_name_tag:
                player_name = player_name_tag.text.strip()
                over = player_data.find(class_='cb-col cb-col-8 text-right').text.strip()
                medin_over = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().text.strip()
                runs = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().text.strip()
                wickets = player_data.find(class_='cb-col cb-col-8 text-right text-bold').text.strip()
                eco = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
                    
                # print("Player Name:", player_name)
                # print("over:", over)
                # print("Runs:", runs)
                # print("medin_over:", medin_over)
                # print("wickets:", wickets)
                # print("eco:", eco)
    
                data_first_inn_scoreboard_bowler["Player Name"].append(player_name)
                data_first_inn_scoreboard_bowler["O"].append(over)
                data_first_inn_scoreboard_bowler["M"].append(medin_over)
                data_first_inn_scoreboard_bowler["R"].append(runs)
                data_first_inn_scoreboard_bowler["W"].append(wickets)
                data_first_inn_scoreboard_bowler["ECO"].append(eco)
            else:
                continue
                
    else:
        print("Innings data not found")


# Extracting data from the second innings scoreboard
def secinningsData(innings):
    if innings:
        team_name = innings.find(class_="cb-col cb-col-100 cb-scrd-hdr-rw").text.strip()
        data_sec_inn_scoreboard_header["Cricket_data"].append(team_name)
        #print("Team:", team_name)
        
        # scoreboard_header = innings.find(class_ = "cb-col cb-col-100 cb-scrd-sub-hdr cb-bg-gray").text.strip()
        # data_scoreboard["Player Name"].append(scoreboard_header)
        
        players_data = innings.find_all(class_='cb-col cb-col-100 cb-scrd-itms')
        
        for player_data in players_data:
            #print(player_data.text.strip())
            
            player_name_tag = player_data.find(class_ = 'cb-col cb-col-25')
    
            # Check if player name is found
            if player_name_tag:
                player_name = player_name_tag.text.strip()
                status = player_data.find(class_='cb-col cb-col-33').text.strip()
                runs = player_data.find(class_='cb-col cb-col-8 text-right text-bold').text.strip()
                balls = player_data.find(class_='cb-col cb-col-8 text-right').text.strip()
                fours = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().text.strip()
                sixes = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().text.strip()
                srr = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().find_next_sibling().text.strip()

                    
                # print("Player Name:", player_name)
                # print("Out:", out)
                # print("Runs:", runs)
                # print("Balls Faced:", balls)
                # print("Fours:", fours)
                # print("Sixes:", sixes)
                # print("Strike Rate:", srr)
    
                data_sec_inn_scoreboard_batter["Player Name"].append(player_name)
                data_sec_inn_scoreboard_batter["Status"].append(status)
                data_sec_inn_scoreboard_batter["R"].append(runs)
                data_sec_inn_scoreboard_batter["B"].append(balls)
                data_sec_inn_scoreboard_batter["4s"].append(fours)
                data_sec_inn_scoreboard_batter["6s"].append(sixes)
                data_sec_inn_scoreboard_batter["SR"].append(srr)
            else:
                break
            
            
        #players_data = innings.find_all(class_='cb-col cb-col-100 cb-scrd-itms ')
        
        
        for player_data in players_data:
            #print(player_data.text.strip())
            
            player_name_tag = player_data.find(class_ = 'cb-col cb-col-38')
    
            # Check if player name is found
            if player_name_tag:
                player_name = player_name_tag.text.strip()
                over = player_data.find(class_='cb-col cb-col-8 text-right').text.strip()
                medin_over = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().text.strip()
                runs = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().text.strip()
                wickets = player_data.find(class_='cb-col cb-col-8 text-right text-bold').text.strip()
                eco = player_data.find(class_='cb-col cb-col-8 text-right').find_next_sibling().find_next_sibling().find_next_sibling().text.strip()
                    
                # print("Player Name:", player_name)
                # print("over:", over)
                # print("Runs:", runs)
                # print("medin_over:", medin_over)
                # print("wickets:", wickets)
                # print("eco:", eco)
    
                data_sec_inn_scoreboard_bowler["Player Name"].append(player_name)
                data_sec_inn_scoreboard_bowler["O"].append(over)
                data_sec_inn_scoreboard_bowler["M"].append(medin_over)
                data_sec_inn_scoreboard_bowler["R"].append(runs)
                data_sec_inn_scoreboard_bowler["W"].append(wickets)
                data_sec_inn_scoreboard_bowler["ECO"].append(eco)
            else:
                continue
                
    else:
        print("Innings data not found")

innings1 = soup1.find(id="innings_1")
innings2 = soup1.find(id="innings_2")

#print("Innings 1:")
inningsData(innings1)

#print("\nInnings 2:")
secinningsData(innings2)


# Creating DataFrames from the collected data and saving it to an Excel file    
df_points_table = pd.DataFrame.from_dict(data_points_table)
data_first_inn_scoreboard_header = pd.DataFrame.from_dict(data_first_inn_scoreboard_header)
data_first_inn_scoreboard_batter = pd.DataFrame.from_dict(data_first_inn_scoreboard_batter)
data_first_inn_scoreboard_bowler = pd.DataFrame.from_dict(data_first_inn_scoreboard_bowler)
data_sec_inn_scoreboard_header = pd.DataFrame.from_dict(data_sec_inn_scoreboard_header)
data_sec_inn_scoreboard_batter = pd.DataFrame.from_dict(data_sec_inn_scoreboard_batter)
data_sec_inn_scoreboard_bowler = pd.DataFrame.from_dict(data_sec_inn_scoreboard_bowler)

# Writing data to an Excel file
with pd.ExcelWriter('Cricket_Data.xlsx') as writer:
    df_points_table.to_excel(writer, index=False, sheet_name='Points_Table')
    data_first_inn_scoreboard_header.to_excel(writer, index=False, sheet_name='Scoreboard')
    data_first_inn_scoreboard_batter.to_excel(writer, index=False, sheet_name='Scoreboard', startrow=len(data_first_inn_scoreboard_header) + 3)
    data_first_inn_scoreboard_bowler.to_excel(writer, index=False, sheet_name='Scoreboard', startrow=len(data_first_inn_scoreboard_header) + len(data_first_inn_scoreboard_batter) + 5)
    data_sec_inn_scoreboard_header.to_excel(writer, index=False, sheet_name='Scoreboard', startrow=len(data_first_inn_scoreboard_header) + len(data_first_inn_scoreboard_batter) + len(data_first_inn_scoreboard_bowler)  + 7)
    data_sec_inn_scoreboard_batter.to_excel(writer, index=False, sheet_name='Scoreboard', startrow=len(data_first_inn_scoreboard_header) + len(data_first_inn_scoreboard_batter) + len(data_first_inn_scoreboard_bowler) + len(data_sec_inn_scoreboard_header)  + 9)
    data_sec_inn_scoreboard_bowler.to_excel(writer, index=False, sheet_name='Scoreboard', startrow=len(data_first_inn_scoreboard_header) + len(data_first_inn_scoreboard_batter) + len(data_first_inn_scoreboard_bowler) + len(data_sec_inn_scoreboard_header) + len(data_sec_inn_scoreboard_batter)  + 11)
    

time.sleep(5)

# Closing the WebDriver instance after execution
driver.close()