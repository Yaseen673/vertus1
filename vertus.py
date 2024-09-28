import time
import requests
import os
from colorama import Fore, Style, init

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def art():
    print("\033[1;91m" + r"""     

 /$$   /$$                                                  
| $$  /$$/                                                  
| $$ /$$/   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$  /$$$$$$ 
| $$$$$/   |____  $$ /$$__  $$| $$  | $$| $$  | $$ |____  $$
| $$  $$    /$$$$$$$| $$  \ $$| $$  | $$| $$  | $$  /$$$$$$$
| $$\  $$  /$$__  $$| $$  | $$| $$  | $$| $$  | $$ /$$__  $$
| $$ \  $$|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/  \__/ \_______/ \____  $$ \______/  \____  $$ \_______/
                     /$$  \ $$           /$$  | $$          
                    |  $$$$$$/          |  $$$$$$/          
                     \______/            \______/           
""" + "\033[0m" + "\033[1;92m" + r"""                                    
 ____  _     _                       _
/ ___|| |__ (_)_ __   ___  _ __ ___ (_)_   _  __ _
\___ \| '_ \| | '_ \ / _ \| '_ ` _ \| | | | |/ _` |
 ___) | | | | | | | | (_) | | | | | | | |_| | (_| |
|____/|_| |_|_|_| |_|\___/|_| |_| |_|_|\__, |\__,_|
                                       |___/
""" + "\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;93mScript created by: Kaguya Shinomiya\033[0m\n\033[1;92mJoin Telegram: \nhttps://t.me/Pumpbtcxyz\033[0m\n\033[1;91mVisit my GitHub: \nhttps://github.com/Kaguya1st\033[0m\n\033[1;96m---------------------------------------\033[0m\n\033[1;38;2;139;69;19;48;2;173;216;230m-------------[Vertus Bot]-------------\033[0m\n\033[1;96m---------------------------------------\033[0m")

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        print(f"{Fore.CYAN + Style.BRIGHT}Wait {hours:02}:{mins:02}:{secs:02}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Wait 00:00:00          ", end='\r')

def load_tokens(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def get_headers(token):
    return {
        "accept": "application/json, text/plain, */*",
        "authorization": f"Bearer {token}",
        "content-type": "application/json"
    }

def login(token):
    url = "https://api.thevertus.app/users/get-data"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        balance = int(data.get("user").get("balance", 0)) / 10**18
        farm_b = int(data.get("user").get("vertStorage", 0)) / 10**18
        pph = int(data.get("user").get("valuePerHour", 0)) / 10**18
        eo = int(data.get("user").get("earnedOffline", 0)) / 10**18
        print(Fore.GREEN + Style.BRIGHT + f"Vert Balance: {balance:.3f} | Earned Offline: {eo:.4f}")
        print(Fore.GREEN + Style.BRIGHT + f"Farm Balance: {farm_b:.5f} | PPH: {pph:.4f}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def daily_bonus(token):
    url = "https://api.thevertus.app/users/claim-daily"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        
        success = data.get("success")
        n_balance = data.get("balance", 0) / 10**18
        message = data.get("msg", "")
        reward = data.get("claimed", 0) / 10**18
        day = data.get("consecutiveDays", 0)
        
        if success:
            print(Fore.GREEN + Style.BRIGHT + f"Day {day} Daily Bonus {reward} Claimed Successfully")
            print(Fore.GREEN + Style.BRIGHT + f"New Balance: {n_balance:.3f}")
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"{message}")
    
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def ads(token):
    url_1 = "https://api.thevertus.app/missions/check-adsgram"
    headers = get_headers(token)
    body = {}

    try:
        response = requests.post(url_1, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        isSuccess = data.get("isSuccess")
        message = data.get("msg")

        if isSuccess:
            print(Fore.CYAN + Style.BRIGHT + "Ads Reward Claiming.....")
            time.sleep(30)
            url_2 = "https://api.thevertus.app/missions/complete-adsgram"
            response_2 = requests.post(url_2, headers=headers, json=body, allow_redirects=True)
            response_2.raise_for_status()
            data_2 = response_2.json()
            
            isSuccess = data_2.get("isSuccess")
            new_balance = data_2.get("newBalance", 0) / 10**18
            total_claim = data_2.get("completion")
            
            if isSuccess:
                print(Fore.GREEN + Style.BRIGHT + "Ads Reward Claimed Successfully")
                print(Fore.GREEN + Style.BRIGHT + f"New Balance: {new_balance:.3f} | Total Claim: {total_claim} times")
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"Ads Reward Failed: {data_2}")
                      
        else:
            print(Fore.YELLOW + Style.BRIGHT + f"{message}")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")        

def get_task(token):
    get_task_url = "https://api.thevertus.app/missions/get"
    headers = get_headers(token)
    body = {"isPremium": False, "languageCode": "en"}
    id_list = []
    task_title = []

    try:
        response = requests.post(get_task_url, headers=headers, json=body, allow_redirects=True)
        response.raise_for_status()
        data = response.json()

        groups = data.get('groups', [])
        for group in groups:
            for mission_list in group.get('missions', []):
                for mission in mission_list:
                    id_list.append(mission.get('_id'))
                    task_title.append(mission.get('title'))

        sponsors = data.get('sponsors', [])
        for sponsor_list in sponsors:
            for sponsor in sponsor_list:
                id_list.append(sponsor.get('_id'))
                task_title.append(sponsor.get('title'))

        sponsors2 = data.get('sponsors2', [])
        if isinstance(sponsors2, list):
            for sponsor2 in sponsors2:
                id_list.append(sponsor2.get('_id'))
                task_title.append(sponsor2.get('title'))

        communitys = data.get('community', [])
        for community_list in communitys:
            for community in community_list:
                id_list.append(community.get('_id'))
                task_title.append(community.get('title'))

        recommendations = data.get('recommendations', {}).get('missions', [])
        for mission in recommendations:
            id_list.append(mission.get('_id'))
            task_title.append(mission.get('title'))

        return id_list, task_title

    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")
        return [], []

def comp_task(token, id_list, task_title):
    url = "https://api.thevertus.app/missions/complete"
    headers = get_headers(token)
    
    initial_balance = None
    try:
        response = requests.post("https://api.thevertus.app/users/get-data", headers=headers, json={}, allow_redirects=True)
        response.raise_for_status()
        data = response.json()
        initial_balance = int(data.get("user").get("balance", 0)) / 10**18
    except requests.exceptions.RequestException as e:
        print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")
    
    if initial_balance is None:
        return

    for index, _id in enumerate(id_list):
        body = {"missionId": _id}
        try:
            response = requests.post(url, headers=headers, json=body, allow_redirects=True)
            response.raise_for_status()
            data = response.json()
            isSuccess = data.get("isSuccess")
            n_balance = data.get("newBalance", 0) / 10**18

            if isSuccess:
                print(Fore.GREEN + Style.BRIGHT + f"Task {task_title[index]} Completed!")
                print(Fore.GREEN + Style.BRIGHT + f"New Balance: {n_balance:.3f}")
                countdown_timer(5)
            else:
                print(Fore.YELLOW + Style.BRIGHT + f"Task {task_title[index]} Failed!")
        
        except requests.exceptions.RequestException as e:
            print(Fore.RED + Style.BRIGHT + f"Request failed: {e}")

def upgrade_farm(token):
    # Add the code for farm upgrade here
    pass

def upgrade_storage(token):
    # Add the code for storage upgrade here
    pass

def upgrade_population(token):
    # Add the code for population upgrade here
    pass

def get_cards(token):
    # Add the code for getting cards here
    pass

def post_card_upgrade(card_id, card_name, token):
    # Add the code for upgrading cards here
    pass

def start(token_file):
    clear_terminal()
    art()
    tokens = load_tokens(token_file)

    for token in tokens:
        print(Fore.MAGENTA + Style.BRIGHT + "Processing account...")
        login(token)
        daily_bonus(token)
        ads(token)
        id_list, task_title = get_task(token)
        if id_list:
            comp_task(token, id_list, task_title)
        upgrade_farm(token)
        upgrade_storage(token)
        upgrade_population(token)
        card_details = get_cards(token)
        if card_details:
            for card_id, card_name in card_details:
                post_card_upgrade(card_id, card_name, token)
        print(Fore.MAGENTA + Style.BRIGHT + "Finished processing account\n")

if __name__ == "__main__":
    start('tokens.txt')
