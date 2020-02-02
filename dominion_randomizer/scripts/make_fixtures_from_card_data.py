# encoding=utf8
import json
import os
import copy
import re
from collections import OrderedDict

class CardClassifier():
    type_dict = {
        'アクション': 'action',
        'アタック': 'attack',
        'ARTIFACT': 'artifact',
        '祝福': 'boon',
        '城': 'castle',
        '呪い': 'curse',
        '不運': 'doom',
        '持続': 'duration',
        'イベント': 'event',
        '幸運': 'fate',
        '集合': 'gathering',
        '家宝': 'heirloom',
        '呪詛': 'hex',
        '騎士': 'knight',
        '夜行': 'night',
        '略奪者': 'looter',
        'ランドマーク': 'landmark',
        '褒賞': 'prize',
        'PROJECT': 'project',
        'リアクション': 'reaction',
        'リザーブ': 'reserve',
        '廃墟': 'ruins',
        '精霊': 'spirit',
        '状態': 'state',
        '避難所': 'shelter',
        '財宝': 'treasure',
        'トラベラー': 'traveller',
        '勝利点': 'victory',
        'ゾンビ': 'zombie'
    }

    base_card_name_list = [
        '銅貨',
        '銀貨',
        '金貨',
        '白金貨',
        '屋敷',
        '公領',
        '属州',
        '植民地',
        '呪い',
        'ポーション',
        # Ruins
        '廃坑',
        '図書館跡地',
        '市場跡地',
        '廃村',
        '生存者',
    ]

    non_supply_type_list = ['廃墟', '精霊', '避難所', '家宝', 'ゾンビ', '褒賞']

    effect_type_dict = {
        'PROJECT': 'project',
        'ARTIFACT': 'artifact',
        'イベント': 'event',
        'ランドマーク': 'landmark',
        '呪詛': 'hex',
        '祝福': 'boon',
        '状態': 'state'
    }

    non_randomizer_name_list = [
        # Castle
        '崩れた城',
        '小さい城',
        '幽霊城',
        '華やかな城',
        '広大な城',
        '壮大な城',
        '王城',
        # Traveller
        '兵士',
        '脱走兵',
        '門下生',
        '教師',
        'トレジャーハンター',
        'ウォリアー',
        'ヒーロー',
        'チャンピオン',
        # Knight
        'デイム・アンナ',
        'デイム・ジョセフィーヌ',
        'デイム・モリー',
        'デイム・ナタリー',
        'デイム・シルビア',
        'サー・ベイリー',
        'サー・デストリー',
        'サー・マーチン',
        'サー・マイケル',
        'サー・ヴァンデル',
        # Split piles
        'エンポリウム',
        '鹵獲品',
        '騒がしい村',
        '石',
        '大金',
        'アヴァント'
    ]
    
    card_category_list = [
        'artifact',
        'base_card',
        'boon',
        'event',
        'hex',
        'kingdom_card',
        'landmark',
        'non_supply',
        'project',
        'state'
    ]

    def __init__(self, cards_data_list, expansion_data_list):
        self.cards_data_list = cards_data_list
        self.expansion_name_to_id_dict = self.parse_expantion_json(expansion_data_list)

        self.artifact_list = []
        self.base_card_list = []
        self.boon_list = []
        self.event_list = []
        self.hex_list = []
        self.kingdom_card_list = []
        self.landmark_list = []
        self.non_supply_list = []
        self.project_list = []
        self.state_list = []

        self.randomizer_card_list = []

    @staticmethod
    def parse_expantion_json(expansion_data_list):
        expansion_data_dict = OrderedDict()
        for expansion_data in expansion_data_list:
            expansion_data_dict[expansion_data['fields']['name_jp_kanji']] = expansion_data['pk']
        return expansion_data_dict

    def classification(self):
        for raw_card_json in self.cards_data_list:
            common_params_dict = self.make_common_params_dict(raw_card_json)
            category = self.get_category(raw_card_json)
            if category == 'event':
                parsed_card_dict = self.make_event_dict(common_params_dict, raw_card_json)
            elif category in self.effect_type_dict.values():
                parsed_card_dict = self.make_effect_dict(common_params_dict)
            else:
                parsed_card_dict = self.make_deck_card_dict(common_params_dict, raw_card_json)
            
            fixtures_data_element = self.make_fixtures_data_element(category, parsed_card_dict)
            eval('self.' + category + '_list.append(fixtures_data_element)')

            if category == 'kingdom_card' and not(parsed_card_dict['name_jp_kanji'] in self.non_randomizer_name_list):
                randomizer_data_element = copy.deepcopy(fixtures_data_element)

                randomizer_data_element['model'] = 'dominion_randomizer.RandomizerCard'
                randomizer_data_element['pk'] = len(self.randomizer_card_list) + 1
                self.randomizer_card_list.append(randomizer_data_element)

    def get_category(self, cards_data):
        if cards_data["name_jp"] in self.base_card_name_list:
            return "base_card"
        for card_type in cards_data["types"][0].split("−"):
            if card_type in self.non_supply_type_list:
                return "non_supply"
        if "PROJECT" in cards_data["types"][0]:
            return "project"
        if "ARTIFACT" in cards_data["types"][0]:
            return "artifact"
        if "イベント" in cards_data["types"][0]:
            return "event"
        if "ランドマーク" in cards_data["types"][0]:
            return "landmark"
        if "呪詛" in cards_data["types"][0]:
            return "hex"
        if "祝福" in cards_data["types"][0]:
            return "boon"
        if "状態" in cards_data["types"][0]:
            return "state"
        return "kingdom_card"

    def make_common_params_dict(self, raw_card_json):
        common_params_dict = OrderedDict([
            ('name_jp_kanji', raw_card_json['name_jp']),
            ('name_jp_pronunciations', raw_card_json['pronunciations']),
            ('name_en', raw_card_json['name_en']),
            ('expansion', self.expansion_name_to_id_dict[raw_card_json['expansion']]),
            ('text_jp', raw_card_json['text_jp']),
            ('text_en', raw_card_json['text_en'])
        ])
        return common_params_dict
        
    @staticmethod
    def make_event_dict(common_params_dict, raw_card_json):
        event_dict = OrderedDict([
            ('cost_coin', raw_card_json['cost']['coin']),
            ('cost_potion', raw_card_json['cost']['potion']),
            ('cost_debt', raw_card_json['cost']['debt'])
        ])
        event_dict.update(common_params_dict)
        return event_dict

    @staticmethod
    def make_effect_dict(common_params_dict):
        return common_params_dict

    def make_deck_card_dict(self, common_params_dict, raw_card_json):
        deck_card_dict = OrderedDict([
            # Cost
            ('cost_coin',self.str2int(raw_card_json['cost']['coin'])),
            ('cost_potion',self.str2int(raw_card_json['cost']['potion'])),
            ('cost_debt',self.str2int(raw_card_json['cost']['debt'])),
            # Gain
            ('gain_card',raw_card_json['gain']['card']),
            ('gain_action',raw_card_json['gain']['action']),
            ('gain_buy',raw_card_json['gain']['buy']),
            ('gain_coin',raw_card_json['gain']['money']),
            ('gain_vp',raw_card_json['gain']['vp']),
            ('gain_villager',raw_card_json['gain']['villager']),
            ('gain_coffer',raw_card_json['gain']['coffer'])
        ])
        deck_card_dict.update(common_params_dict)
        deck_card_dict.update(self.make_types_dict(raw_card_json['types'][0]))
        return deck_card_dict

    @staticmethod
    def str2int(target_str):
        if not target_str:
            return None
        return int(re.sub("\\D", "", target_str))

    def make_types_dict(self, types_string):
        # Types template
        types_dict = OrderedDict([
            ('types', types_string,)
        ])
        for card_type in types_string.split("−"):
            types_dict[self.type_dict[card_type]] = True
        return types_dict
    
    def make_fixtures_data_element(self, category, fields_data):
        category_list_length = eval('len(self.' + category + '_list)')
        model_name = self.snake2upper_camel(category)
        fixtures_data_element = OrderedDict([
            ("model", "dominion_randomizer." + model_name),
            ("pk", category_list_length + 1),
            ("fields", fields_data)
        ])
        return fixtures_data_element

    @staticmethod
    def snake2upper_camel(snake_str):
        return re.sub("_(.)", lambda x:x.group(1).upper(), snake_str.capitalize())

    def export_json(self):
        fixtures_dir_path = 'dominion_randomizer/dominion_randomizer/fixtures/'
        for target_category in self.card_category_list:
            data_file_path = fixtures_dir_path + target_category + '.json'
            with open(data_file_path, 'w', encoding='utf-8') as data_file:
                eval('json.dump(self.' + target_category + '_list, data_file, indent=4, ensure_ascii=False)')
        
        data_file_path = fixtures_dir_path + 'randomizer_card.json'
        with open(data_file_path, 'w', encoding='utf-8') as data_file:
            json.dump(self.randomizer_card_list, data_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    print("start!!")
    # Get card data from JSON file
    cards_data_file_path = 'dominion_randomizer/data/cards.json'
    try:
        with open(cards_data_file_path, 'r', encoding='utf-8') as cards_data_file:
            cards_data_list = json.load(cards_data_file)
    except Exception as e:
        print(e)

    # Get expantion data
    expansion_data_file_path = 'dominion_randomizer/dominion_randomizer/fixtures/expansion.json'
    try:
        with open(expansion_data_file_path, 'r', encoding='utf-8') as expansion_data_file:
            expansion_data_list = json.load(expansion_data_file)
    except Exception as e:
        print(e)

    card_classifier = CardClassifier(cards_data_list, expansion_data_list)
    card_classifier.classification()
    card_classifier.export_json()