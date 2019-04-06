json_path = "bin/json/data.json"
import json
buffer = dict()
def check_state(attribute):
    with open(json_path, "r") as json_read:
        data = json.load(json_read)
        buffer.update(data)
    if attribute == "surgeon":
        for k,v in buffer.items():
            if v['profession'] == attribute:
                return k
    elif attribute == "stomatologist":
        for k,v in buffer.items():
            if "stomatologist" == v['profession']:
                return k
    elif attribute == "proctologist":
        for k,v in buffer.items():
            if "proctologist" == v['profession']:
                return k
    elif attribute == "therapist":
        for k,v in buffer.items():
            if "therapist" == v['profession']:
                return k
    elif attribute == "ophthalmologist":
        for k,v in buffer.items():
            if "ophthalmologist" == v['profession']:
                return k
    elif attribute == "cardiologist":
        for k,v in buffer.items():
            if "cardiologist" == v['profession']:
                return k
    elif attribute == "mammologist":
        for k,v in buffer.items():
            if "mammologist" == v['profession']:
                return k
    return "nokey"