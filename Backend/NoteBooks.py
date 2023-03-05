import json

def GetNoteBooks(NoteBooksCollection):
    Books = NoteBooksCollection.find()
    a = []
    for Book in Books:
        print(Book)
        a.append(Book["subject"])
    string = json.dumps(a, indent=3,sort_keys=False)
    print(string)
    return string


def GetChapters(NoteBooksCollection,SubjectName,ChapterIndex):
    Book = NoteBooksCollection.find({"subject":SubjectName})[0]
    Chapters = Book["Chapters"]
    NoOfChapters = len(Chapters)
    ChapTitle = Chapters[ChapterIndex]["Chapter_Title"]
    ChapNote = Chapters[ChapterIndex]["Chapter_Note"]
    a = [{"NumberOfChapters":NoOfChapters},{"Chapter_Title":ChapTitle},{"Chapter_Note":ChapNote}]
    string = json.dumps(a, indent=3,sort_keys=False)
    print(string)

def CreateNewNoteBook(NoteBooksCollection,string):
    id = NoteBooksCollection.find({}).sort("_id",-1).limit(1)[0]["_id"]
    id = id+1
    template = {
    "_id":-1,
    "subject": "",
    "Chapters": [
        {
            "Chapter_Title":"",
            "Chapter_Note" : ""
        }

    ]
    }
    template["_id"]=id
    template["subject"]=string
    NoteBooksCollection.insert_one(template)


def DeleteNoteBook(NoteBooksCollection, id):    
    NoteBooksCollection.delete_one({"_id":id})

def UpdateNoteBooks(NoteBooksCollection,id,SubjectName):
    NoteBooksCollection.update_one({"_id":id},{"$set":{"subject":SubjectName}})

def AddChapter(NoteBooksCollection,string,id):
    a = []
    a.append(string)
    update = { "$push": { "Chapters": { "$each": a} } }
    NoteBooksCollection.update_one({"_id":id},update)

def DeleteChapter(NoteBooksCollection,ChapterNumber,id):
    dic = NoteBooksCollection.find_one({"_id":id})["Chapters"]
    dic.pop(ChapterNumber)
    update = { "$set": { "Chapters": dic } }
    NoteBooksCollection.update_one({"_id":id},update)


def UpdateChapter(NoteBooksCollection,string,id):
    dic = NoteBooksCollection.find_one({"_id":id})["Chapters"]
    number = string["ChapterNo"]
    dic[number]["Chapter_Title"]= string["Chapter_Title"]
    dic[number]['Chapter_Note']= string['Chapter_Note']
    update = { "$set": { "Chapters": dic } }
    NoteBooksCollection.update_one({"_id":id},update)