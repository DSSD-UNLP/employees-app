#import yaml

class SettingsParser(object):

    def __init__(self):
        self.settings = {}
        for line in open("employeesProject/settings_secret.yml"):
            try:
              name, value = line.split(':', 1)
            except:
              continue
            self.settings[name.strip()] = value.strip()

    def get(self, attribute):
        return self.settings.get(attribute, None)