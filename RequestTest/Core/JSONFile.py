import json

class JSONFile:
  @staticmethod
  def ReadJSON(filePath):
    JSONData = []
    f = open(filePath)
    data = json.load(f)
    for i in data['DataMethod']:
      JSONData.append(i)
    f.close()
    return JSONData
  
if __name__ == '__main__':
  print(JSONFile.ReadJSON('./RequestTest/Files/inputDelete.json'))
  
