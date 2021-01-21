from quickstart import get_calendar_service
from cours import getCours

from datetime import datetime, timedelta

def getColor(colorId):
    colorId = colorId.replace("#", "")
    colorId = int(colorId, 16)
    print(colorId)

    switch={
        16759104:6, #CPOA : Orange
        3355647:9,  #Logique : Bleu fonéc
        6750156:7,   #CMBD : Bleu clair
        1:"error"
    }
    print(switch.get(colorId))

# creates one hour event tomorrow 10 AM IST
service = get_calendar_service()
edt = getCours()

#d = datetime.now().date()
#tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
#start = tomorrow.isoformat()
#end = (tomorrow + timedelta(hours=1)).isoformat()

#for cours in edt:
cours = edt[0]
debutCours = cours["startDateTime"]
finCours = cours["endDateTime"]
nomCours = cours["course"]["label"]
couleurCours = cours["course"]["color"]

if  str(cours["rooms"]) != "[]":
    salleCours = cours["rooms"][0]["label"]
else:
    salleCours = "non definie."
getColor(cours["course"]["color"])

body={
    "summary": nomCours,
    "description": 'Salle: ' + salleCours,
    "start": {"dateTime": debutCours, "timeZone": 'Asia/Kolkata'},
    "end": {"dateTime": finCours, "timeZone": 'Asia/Kolkata'},
    "colorId": 1
}

event_result = service.events().insert(calendarId='0vi7g2ef77llenlto7c89a15qs@group.calendar.google.com', body=body).execute()

print("created event")

print("summary: ", event_result['summary'])
print("starts at: ", event_result['start']['dateTime'])
print("ends at: ", event_result['end']['dateTime'])
