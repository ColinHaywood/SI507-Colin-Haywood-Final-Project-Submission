import requests
import json
import requests_cache
from bs4 import BeautifulSoup as bs
import webbrowser

#As per discussion with Professor Madamanchi on 4/29, received permission to use filter instead of tree as solution

###automatic cache set to expire after 30 minutes
requests_cache.install_cache(cache_name="Elden Ring Wiki Cache", backend="sqlite", expire_after=1800)

HTML_base = "https://eldenring.wiki.fextralife.com/"



def createsouplist():
    """scrapes HTML addresses and appends to a list as Beautiful Soup items"""

    RuinsGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Ruins+Greatsword")
    RuinsGreatsword = bs(RuinsGreatswordResponse.text, 'html.parser')
    #Str 50, Int 16

    AxeofGodrickResponse = requests.get("https://eldenring.wiki.fextralife.com/Axe+of+Godrick")
    AxeofGodrick = bs(AxeofGodrickResponse.text, 'html.parser')
    #Str 34, Dex 22

    GreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Greatsword")
    Greatsword = bs(GreatswordResponse.text, 'html.parser')
    #Str 31, Dex 12

    BoltofGransaxResponse = requests.get("https://eldenring.wiki.fextralife.com/Bolt+of+Gransax")
    BoltofGransax = bs(BoltofGransaxResponse.text, 'html.parser')
    #Str 20, Dex 40

    DragonKingCragbladeResponse = requests.get("https://eldenring.wiki.fextralife.com/Dragon+King's+Cragblade")
    DragonKingCragblade = bs(DragonKingCragbladeResponse.text, 'html.parser')
    #Str 18, Dex 37

    HandofMaleniaResponse = requests.get("https://eldenring.wiki.fextralife.com/Hand+of+Malenia")
    HandofMalenia = bs(HandofMaleniaResponse.text, 'html.parser')
    #Str 16, Dex 48

    GoldenOrderGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Golden+Order+Greatsword")
    GoldenOrderGreatsword = bs(GoldenOrderGreatswordResponse.text, 'html.parser')
    #Str 16, Dex 21, Fai 28

    DarkMoonGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Dark+Moon+Greatsword")
    DarkMoonGreatsword = bs(DarkMoonGreatswordResponse.text, 'html.parser')
    #Str 16, Dex 11, Int 38

    MoonveilResponse = requests.get("https://eldenring.wiki.fextralife.com/Moonveil")
    Moonveil = bs (MoonveilResponse.text, 'html.parser')
    #Str 12, Dex 18, Int 23

    SwordofNightFlameResponse = requests.get("https://eldenring.wiki.fextralife.com/Sword+of+Night+and+Flame")
    SwordofNightFlame = bs(SwordofNightFlameResponse.text, 'html.parser')
    #Str 12, Dex 12, Int 24, Fai 24

    BattleAxeResponse = requests.get("https://eldenring.wiki.fextralife.com/Battle+Axe")
    BattleAxe = bs(BattleAxeResponse.text, 'html.parser')
    #Str 12, Dex 8

    FlailResponse = requests.get("https://eldenring.wiki.fextralife.com/Flail")
    Flail = bs(FlailResponse.text, 'html.parser')
    #Str 10, Dex 18

    BastardStarsResponse = requests.get("https://eldenring.wiki.fextralife.com/Bastard's+Stars")
    BastardStars = bs(BastardStarsResponse.text, 'html.parser')
    #Str 8, Dex 22, Int 22

    ShortSwordResponse = requests.get("https://eldenring.wiki.fextralife.com/Short+Sword")
    ShortSword = bs(ShortSwordResponse.text, 'html.parser')
    #Str 8, Dex 10

    DevourerScepterResponse = requests.get("https://eldenring.wiki.fextralife.com/Devourer's+Scepter")
    DevourerScepter = bs(DevourerScepterResponse.text, 'html.parser')
    #Str 24, Dex 20, Fai 25

    SiluriasTreeResponse = requests.get("https://eldenring.wiki.fextralife.com/Siluria's+Tree")
    SiluriasTree = bs(SiluriasTreeResponse.text, 'html.parser')
    #Str 27, Dex 13, Fai 20

    LazuliGlintstoneSwordResponse = requests.get("https://eldenring.wiki.fextralife.com/Lazuli+Glintstone+Sword")
    LazuliGlintStoneSword = bs(LazuliGlintstoneSwordResponse.text, 'html.parser')
    #Str 8, Dex 9, Int 13

    MarikasHammerResponse = requests.get("https://eldenring.wiki.fextralife.com/Marika's+Hammer")
    MarikasHammer = bs(MarikasHammerResponse.text, 'html.parser')
    #Str 20, Dex 12, Fai 19

    EclipseShotelResponse = requests.get("https://eldenring.wiki.fextralife.com/Eclipse+Shotel")
    EclipseShotel = bs(EclipseShotelResponse.text, 'html.parser')
    #Str 10, Dex 25, Fai 30

    HelphensSteepleResponse = requests.get("https://eldenring.wiki.fextralife.com/Helphen's+Steeple")
    HelphensSteeple = bs(HelphensSteepleResponse.text, 'html.parser')
    #Str 19, Dex 10, Int 22

    BlasphemousBladeResponse = requests.get("https://eldenring.wiki.fextralife.com/Blasphemous+Blade")
    BlasphemousBlade = bs(BlasphemousBladeResponse.text, 'html.parser')
    #Str 22, Dex 15, Fai 21

    LorettasWarSickleResponse = requests.get("https://eldenring.wiki.fextralife.com/Loretta's+War+Sickle")
    LorettasWarSickle = bs(LorettasWarSickleResponse.text, 'html.parser')
    #Str 20, Dex 15, Int 20

    GreataxeResponse = requests.get("https://eldenring.wiki.fextralife.com/Greataxe")
    Greataxe = bs(GreataxeResponse.text, 'html.parser')
    #Str 30, Dex 8

    StarscourgeGreatswordResponse = requests.get("https://eldenring.wiki.fextralife.com/Starscourge+Greatsword")
    StarscourgeGreatsword = bs(StarscourgeGreatswordResponse.text, 'html.parser')
    #Str 38, Dex 12, Int 15


    AllSoupItems = []

    AllSoupItems.append(RuinsGreatsword)
    AllSoupItems.append(AxeofGodrick)
    AllSoupItems.append(Greatsword)
    AllSoupItems.append(BoltofGransax)
    AllSoupItems.append(Flail)
    AllSoupItems.append(Moonveil)
    AllSoupItems.append(DragonKingCragblade)
    AllSoupItems.append(HandofMalenia)
    AllSoupItems.append(GoldenOrderGreatsword)
    AllSoupItems.append(DarkMoonGreatsword)
    AllSoupItems.append(SwordofNightFlame)
    AllSoupItems.append(BattleAxe)
    AllSoupItems.append(BastardStars)
    AllSoupItems.append(ShortSword)
    AllSoupItems.append(DevourerScepter)
    AllSoupItems.append(SiluriasTree)
    AllSoupItems.append(LazuliGlintStoneSword)
    AllSoupItems.append(MarikasHammer)
    AllSoupItems.append(EclipseShotel)
    AllSoupItems.append(HelphensSteeple)
    AllSoupItems.append(BlasphemousBlade)
    AllSoupItems.append(LorettasWarSickle)
    AllSoupItems.append(Greataxe)
    AllSoupItems.append(StarscourgeGreatsword)

    return AllSoupItems



def createfilterlist(AllSoupItems):
    """uses a list of Soup items to scrape the HTML and
    create a list of lists, where each list contains a weapon's information"""

    filterlist = []

    for item in AllSoupItems:
        list_item = item.find_all('div', class_='infobox')
        test_list = list_item[0].text
        split_list = test_list.split()
        # print(test_list.split())

        for x in range(len(split_list)):
            if split_list[x] == "Attack":
                item_name = ' '.join(split_list[0:x])

        for x in range(len(split_list)):
            if split_list[x] == "Requires":
                str_req = int(split_list[x+2])

                if split_list[x+3] == "Dex":
                    dex_req = int(split_list[x+4])
                    if split_list[x+5] == "Int":
                        int_req = int(split_list[x+6])
                        if split_list[x+7] == "Fai":
                            fai_req = int(split_list[x+8])
                        else:
                            fai_req = 0
                    elif split_list[x+5] == "Fai":
                        int_req = 0
                        fai_req = int(split_list[x+6])
                    else:
                        int_req = 0
                        fai_req = 0

                elif split_list[x+3] == "Int":
                    dex_req = 0
                    int_req = int(split_list[x+4])
                    if split_list[x+5] == "Fai":
                        fai_req = int(split_list[x+6])
                    else:
                        fai_req = 0

                elif split_list[x+3] == "Fai":
                    dex_req = 0
                    int_req = 0
                    fai_req = int(split_list[x+4])

                else:
                    dex_req = 0
                    int_req = 0
                    fai_req = 0

        itemlist = []
        itemlist.append(item_name)
        itemlist.append(str_req)
        itemlist.append(dex_req)
        itemlist.append(int_req)
        itemlist.append(fai_req)
        filterlist.append(itemlist)

    return filterlist



def recommend_best_item(resultlist):
    """finds the most powerful item by sum of stat requirements
    in the result list and recommends it to the user for their character.
    also opens in web browser."""

    i=0
    for item in resultlist:
        item_stat_sum = sum(item[1:])
        if item_stat_sum > i:
            i = item_stat_sum

    for item in resultlist:
        item_stat_sum = sum(item[1:])
        if item_stat_sum == i:
            print(f"\nThe best weapon for your character is: {item[0]}\n")
            item_url = HTML_base + item[0].replace(' ', '+')
            print(f"Launching {item_url} in web browser...\n")
            webbrowser.open(item_url, new=1)



def main():
    """input prompts resulting in 4 variables.
    prompt responses must be numeric and between a certain range of numbers.
    integer-converted input values will be compared to tree values"""

    print("\nWelcome to the Elden Ring Weapon Recommender!\nPlease enter your character's stats below and we will recommend a weapon ideally suited to your character.\n")

    while True:
        try:
            str_input = input("Enter your character's Strength: ")
            if str_input.strip().isnumeric() == True and int(str_input) >= 8 and int(str_input) <=99:
                break
            elif str_input.strip().isnumeric() == False:
                print("\nPlease enter a numeric value.\n")
            elif int(str_input) < 8:
                print("\nThe minimum Strength for a character is 8.\n")
            elif int(str_input) > 99:
                print("\nThe maximum Strength for a character is 99.\n")
            else:
                print("\nPlease enter a numeric value.\n")
        except:
            print("\nThere's been an error.  Please try again.\n")

    while True:
        try:
            dex_input = input("Enter your character's Dexterity: ")
            if dex_input.strip().isnumeric() == True and int(dex_input) >= 9 and int(dex_input) <= 99:
                break
            elif dex_input.strip().isnumeric() == False:
                print("\nPlease enter a numeric value.\n")
            elif int(dex_input) < 10:
                print("\nThe minimum Dexterity for a character is 10.\n")
            elif int(dex_input) > 99:
                print("\nThe maximum Dexterity for a character is 99.\n")
            else:
                print("\nPlease enter a numeric value.\n")
        except:
            print("\nThere's been an error.  Please try again.\n")

    while True:
        try:
            int_input = input("Enter your character's Intelligence: ")
            if int_input.strip().isnumeric() == True and int(int_input) >= 7 and int(int_input) <= 99:
                break
            elif int_input.strip().isnumeric() == False:
                print("\nPlease enter a numeric value.\n")
            elif int(int_input) < 7:
                print("\nThe minimum Intelligence for a character is 7.\n")
            elif int(int_input) > 99:
                print("\nThe maximum Intelligence for a character is 99.\n")
            else:
                print("\nPlease enter a numeric value.\n")
        except:
            print("\nThere's been an error.  Please try again.\n")

    while True:
        try:
            fai_input = input("Enter your character's Faith: ")
            if fai_input.strip().isnumeric() == True and int(fai_input) >= 7 and int(fai_input) <= 99:
                break
            elif fai_input.strip().isnumeric() == False:
                print("\nPlease enter a numeric value.\n")
            elif int(fai_input) < 7:
                print("\nThe minimum Faith for a character is 7.\n")
            elif int(fai_input) > 99:
                print("\nThe maximum Faith for a character is 99.\n")
            else:
                print("\nPlease enter a numeric value.\n")
        except:
            print("\nThere's been an error.  Please try again.\n")

    print("\nComparing character stats to weapon database...")

    AllSoupItems = createsouplist()

    print("\nAnalyzing data to determine the best weapon for your character...")

    #parse the HTML and create a list of lists where each list is a weapon
    filterlist = createfilterlist(AllSoupItems)
    # print(filterlist)

    with open('finalprojectJSON.json', 'w') as fileobj:
        json.dump(filterlist, fileobj)

    #filter the filter list into a list of results that the character can use
    resultlist = [x for x in filterlist if x[1] <= int(str_input) and x[2] <= int(dex_input) and x[3] <= int(int_input) and x[4] <= int(fai_input)]


    #recommends the best item for the user based on the stat requirements of usable items remaining in the result list
    recommend_best_item(resultlist)


if __name__ == '__main__':
    main()