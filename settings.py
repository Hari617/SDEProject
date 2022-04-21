import json


class Settings:

    def __init__(self, settings_file_path="settings.json"):
        self._settings_file_path = settings_file_path
        self._settings_dict = {}
        self.load()
    def save(self):
        with open(self._settings_file_path, "w") as f:
            json.dump(self._settings_dict, f)
    def add(self, settings):
        self._settings_dict = dict(self._settings_dict, **settings)
    def persist(self, settings=None):
        if settings:
            self.add(settings)
    def load(self):
        with open(self._settings_file_path) as f:
            self._settings_dict = dict(self._settings_dict, **json.load(f))
        self.load()
        self.save()
    def __setitem__(self, key, value):
        self._settings_dict[key] = value
    def __getitem__(self, key):
        return self._settings_dict[key]


