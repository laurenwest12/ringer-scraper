from bs4 import BeautifulSoup

from functions import flatten, print_json

from ringer.qb import qb_html
from ringer.rb import rb_html
from ringer.wr import wr_html
from ringer.te import te_html

def extract_players(html, tier):
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
            "pos": pos,
            "tier": tier
        })

    return players

def extract_players_by_tier(html):
    all_players = []
    soup = BeautifulSoup(html, "html.parser")
    tiers = soup.select(".relative.px-4")

    for i in range(len(tiers)):
        tier = tiers[i]
        print(tier)
        players = extract_players(str(tier), i+1)
        all_players.append(players)

    return flatten(all_players)

qbs = extract_players_by_tier(qb_html)
rbs = extract_players_by_tier(rb_html)
wrs = extract_players_by_tier(wr_html)
tes = extract_players_by_tier(te_html)
