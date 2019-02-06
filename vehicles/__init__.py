import urllib.request
from bs4 import BeautifulSoup

# unofficial lists of all current vehicles
# last update: 25.01.2019
depot_lists = [
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/1218-zajezdnia-podgorze",
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/1219-zajezdnia-nowa-huta",
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/33-zajezdnia-bienczyce",
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/35-tabor-autobusowy-7",
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/1817-zajezdnia-plaszow-2",
    "http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/927-zajezdnia-na-zaleczu-mobilis-sp-z-o-o"
]

translate = {
    "Tabor tramwajowy": "tram",
    "Tabor autobusowy": "bus"
}

# list of corrections of typos in data
corrections = {
    "Ubrino": "Urbino"
}

# return a list of known vehicle types
def vehicle_info():
    # we need to modify our request in order to not receive a 403 Forbidden
    request = urllib.request.Request("http://www.psmkms.krakow.pl/index.php/ciekawostki/krakowski-tabor/37-tabor", headers={ 'User-Agent' : 'Mozilla/5.0' })
    html_data = urllib.request.urlopen(request).read()

    # parse page using BS4
    page = BeautifulSoup(html_data, "html.parser")

    # list to return
    vehicle_info = {
        "tram": [],
        "bus": []
    }

    for table in page.find_all("table"):
        # define whether the table is for trams or busses
        index = "trams"

        # find all rows in table and go through each of them
        for row in table.find_all("tr"):
            column = row.find("td")

            # check if row contains any text
            if not column.find("p"):
                continue

            # get value of entry
            data = column.find("p").text.strip()

            # parse the data
            if data == "Suma":
                continue
            elif data == "Tabor tramwajowy" or data == "Tabor autobusowy":
                index = translate[data]
            else:
                # correct possible typos in vehicle name
                for key, value in corrections.items():
                    data = data.replace(key, value)

                vehicle_info[index].append(data)

    return vehicle_info
