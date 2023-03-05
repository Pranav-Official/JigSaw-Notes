import json

def GetQuickNotes(QuickNotesCollection):
    notes = QuickNotesCollection.find()
    a = []
    for note in notes:
        print(note)
        note2 = note
        if(len(note2["Note"])>100):
            note2["Note"] = note2["Note"][:100]
        a.append(note2)
    string = json.dumps(a, indent=3,sort_keys=False)
    print(string)
    return string

def GetQuickNotePage(QuickNotesCollection,id):
    note = QuickNotesCollection.find_one({"_id": id})
    string = json.dumps(note,indent=3,sort_keys=False)
    print(string)
    return string

# def CreateNewQuickNote(QuickNotesCollection,string):
#     QuickNotesCollection.insert_one(string)

def CreateNewQuickNote(QuickNotesCollection,string):
    id = QuickNotesCollection.find({}).sort("_id",-1).limit(1)[0]["_id"]
    id = id+1
    template = {
    "_id":-1,
    "Title": "",
    "Note": ""
    }
    template["_id"]=id
    template["Note"]=string["Note"]
    template["Title"]=string["Title"]
    QuickNotesCollection.insert_one(template)


def UpdateCurrentQuickNote(QuickNotesCollection,string):
    data = json.loads(string)
    print(data["_id"])

    QuickNotesCollection.update_one({"_id":data["_id"]},{"$set":{"Title":data["Title"]}})
    QuickNotesCollection.update_one({"_id":data["_id"]},{"$set":{"Note":data["Note"]}})

def DeleteCurrentQuickNote(QuickNotesCollection,id):
    QuickNotesCollection.delete_one({"_id":id})