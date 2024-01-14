import os
import json

data = []
for ld in os.listdir("./data"):
 f = open("./data/"+ld+"/desc.json", "r")
 d = json.load(f)
 data.append(d)

print(data)
w = open("./data.json", "w")
w.write(json.dumps(data))
w.close()

  
  
  