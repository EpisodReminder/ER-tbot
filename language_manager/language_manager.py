from os import listdir
from os.path import isfile, join
import json

path = "./language_manager/languages"


def get_languages():
    languages_files = [f for f in listdir(path) if isfile(join(path, f))]
    languages_names = list(map(lambda l: l.split(".")[0], languages_files))
    languages_json = {}
    for language in languages_names:
        with open(f'{path}/{language}.json') as f:
            languages_json[language] = json.load(f)
    return languages_json


class LanguageManager:
    def __init__(self):
        self.language_table = get_languages()
        self.default_language = "ru"

    def __getitem__(self, item):
        if item in self.language_table.keys():
            return self.language_table[item]
        else:
            return self.language_table[self.default_language]

    def get_key_all_languages(self, key):
        res = []
        for lang in self.language_table:
            res.append(self.language_table[lang][key])
        return res
