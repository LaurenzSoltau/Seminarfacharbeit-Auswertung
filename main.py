import pip._vendor.requests as requests
import json

 
# api url
old_sheet_endpoint = "https://api.sheety.co/1673b5fb0689f48c67f8ed517b8515db/copySeminar/tabellenblatt1"
new_sheet_endpoint = "https://api.sheety.co/1673b5fb0689f48c67f8ed517b8515db/copySeminar/tabellenblatt2"


# conversion matrix 
conversion_matrix = {
    1: {
        "14-19": 1,
        "20-45": 2,
        "46+": 3
    },
    2: {
        "Weiblich": 1,
        "M\u00e4nnlich": 2,
        "Divers": 3,
    },
    4: {
        "Keinen": 1,
        "Hauptschule": 2,
        "Realschule": 3,
        "Gymnasium": 4,
        "Hochschule": 5
    },
    8: {
        "Ja": 1,
        "Nein": 2
    },
    9: {
        "Die Linke": 1,
        "SPD": 2,
        "Die Gr\u00fcnen": 3,
        "FDP": 4,
        "CDU": 5,
        "AFD": 6    
    },
}


# TODO Daten aus dem Spreadsheet einlesen und in Dictionary speichern
response = requests.get(old_sheet_endpoint)
data = response.json()["tabellenblatt1"]


# TODO Daten quantitiesieren und neu sortieren

new_data = []
i = 0
for entry in data:
    new_data.append({})
    j = 0
    for question in entry:
        header = f"frage{j}"
        answer = entry[question]
        if j in conversion_matrix.keys():
            print(answer)
            if answer == "":
                j += 1
                continue
            new_data[i][header] = str(conversion_matrix[j][answer])
        else:
            new_data[i][header] = str(answer)
        j += 1
    i += 1
    
# TODO Daten wieder in das Spreadsheet speichern

post_response = requests.post

for entry in new_data:
    spreadsheet_data = {
        "tabellenblatt2": entry
    }
    print(spreadsheet_data)
    with open("jsonData.json", "w") as f:
        f.write(json.dumps(spreadsheet_data))

    post_response = requests.post(new_sheet_endpoint, json=spreadsheet_data)
    print(post_response)

