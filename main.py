from ringer.total import total_html
from bs4 import BeautifulSoup

def extract_players(html):
    players = []
    soup = BeautifulSoup(html, "html.parser")
    rank_div = soup.find_all("div",class_="w-8 lg:w-12 lg:min-w-8 text-center shrink type-row-text")
    name_div = soup.find_all("span",class_="hidden md:inline")
    pos_div = soup.find_all("div",class_="w-14 md:w-[72px] text-center md:text-left flex justify-start items-center gap-1 transition-all duration-700 type-row-text")

    for i in range(len(rank_div)):
        rank = rank_div[i].text
        name = name_div[i].text
        pos = pos_div[i].text
        players.append({
            "rank": rank,
            "name": name,
            "pos": pos
        })

    return players

total_players = extract_players(total_html)
print(total_players)
