import configparser


class ConfigFile:
  @staticmethod
  def GetPropValue(filePath, head, key):
    config = configparser.ConfigParser()
    config.read(filePath)
    value = config.get(head, key)
    return value