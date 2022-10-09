import requests
import json

heroes_list = ['Hulk', 'Captain america', 'Thanos']
#создадим словарь, в котором будет находиться информация о интеллекте каждого героя (изначально 0)
url = 'https://www.superheroapi.com/api.php/2619421814940190/search/'

def hero_intelect(allURL):
    for hero in heroes_list:
        hero_dict = json.loads(requests.get(allURL + hero).content)

    super_man = []
    for power_stats in hero_dict['results']:
        super_man.append({
            'name': power_stats['name'],
            'intelligence': power_stats['powerstats']['intelligence'],
        })

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")

hero_intelect(url)
