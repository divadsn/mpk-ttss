import json
from vehicles import depot_lists, vehicle_info

data = vehicle_info()
data["_copyright"] = {
    "source": "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/37-tabor",
    "last_update": "2019-01-25"
}

print(json.dumps(data, indent=4))
