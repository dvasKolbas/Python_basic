import json
from typing import Any
import requests

def get_dict(req: str) -> Any:
    res= requests.get(req)
    return json.loads(res.text)

def find_episode(season: str, episode: str, dct: dict) -> int:
    result = list(filter(lambda elem:elem["season"] == season and elem["episode"] == episode, dct))
    return result[0]["episode_id"]

def find_max_death() -> None:
    deaths = get_dict("https://breakingbadapi.com/api/deaths")
    episodes = get_dict("https://breakingbadapi.com/api/episodes")

    death_dict = dict()
    for death in deaths:
        id = find_episode(str(death["season"]), str(death["episode"]), episodes)
        episode = death_dict.get(id)
        if episode:
            episode["number_of_deaths"] += death["number_of_deaths"]
            episode["deaths"] += (", " + death["death"])
        else:
            death_dict[id] = {"season": death["season"], "episode": death["episode"],
                              "number_of_deaths": death["number_of_deaths"], "deaths": death["death"]}

    sort_death = sorted(death_dict, key=lambda elem: death_dict.get(elem)["number_of_deaths"], reverse=True)[0]
    max_death = death_dict.get(sort_death)
    max_death["id"] = sort_death
    create_json(max_death)
    print_ax_death(max_death)

def print_ax_death(max_death: dict) -> None:
    print("id эпизода: {0}\nНомер сезона: {1}\nНомер эпизода: {2}\n"
          "Общее количество смертей: {3}\nСписок погибших: {4}".format(max_death["id"], max_death["season"],
                                                                       max_death["episode"], max_death["number_of_deaths"],
                                                                       max_death["deaths"]))

def create_json(max_death: dict) -> None:
    with open("max_death.json", "w") as file:
        json.dump(max_death, file, indent=4)

find_max_death()



