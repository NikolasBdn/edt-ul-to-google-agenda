import requests
import json

def getCours():

    url = "https://multi.univ-lorraine.fr/graphql"
    headers = {
        "x-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVpZCI6ImJhdWRvbjV1Iiwicm9sZXMiOlsiRVQiXSwiZW1haWwiOiJuaWNvbGFzLmJhdWRvbjlAZXR1LnVuaXYtbG9ycmFpbmUuZnIiLCJkbiI6IkJBVURPTiBOaWNvbGFzIiwibiI6IkJhdWRvbiIsImYiOiJOaWNvbGFzIn0sImlhdCI6MTYwNDgzNjk5OSwiZXhwIjoxNjA0ODQwNTk5fQ.dK234IVI4JINltzSfutlQGIN0sQLCbwWKDWFiw9o-B4",
        "x-refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InVpZCI6ImJhdWRvbjV1In0sImlhdCI6MTYwNDgzNjk5OSwiZXhwIjoxNjA1NDQxNzk5fQ.wxEslgVnkIR-VYdwVd7SVJhOgEz3YwJIF9iA0IIuOQQ",
        "content-type": "application/json",
        "Origin": "https://multi.univ-lorraine.fr",
        "Cookie": "ULAUTHTRACE=TRACE-2701-t5lFTHkcNYKH1XGFxRSsDalnfpFYVUxhSAaMm9xNvIoxdKPNLS-sieben; _pk_ref.263.067e=%5B%22%22%2C%22%22%2C1604836996%2C%22https%3A%2F%2Fent.univ-lorraine.fr%2F%22%5D; _pk_ses.263.067e=1; _pk_id.263.067e=e27e3ba1b075cd60.1600716829.28.1604837329.1604593039."        
    }
    #Recuperation du parametre json pour la requete
    payload = open("payload.json", "r")


    r = requests.post(url, data=payload, headers=headers)
    #print(r.json())

    json_response = json.loads(r.text)
    print(json_response)
    edt = json_response["data"]["timetable"]["plannings"][0]["events"]

    for cours in edt:
        c = cours["course"]
        print(str(cours["startDateTime"]) + " - " + str(cours["endDateTime"]) + " : \n")
        print("\t- " + str(c["label"]) + "\n")

        if  str(cours["rooms"]) != "[]":
            #print("\t" + str(cours["rooms"]) + "\n")
            print("\t- Salle " + str(cours["rooms"][0]["label"])  + "\n")
        else:
            print("\t- Salle non définie\n")

    return edt

getCours()
