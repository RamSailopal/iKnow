# iKnow

iKnow is a library for natural language processing (NLP) This repo is a demonstration of Intersystems iKnow with M based databases (YottaDB/Intersystems IRIS/Cache/GTM) 

Utilising mg_python, text is read from the database and then iKnow processed data is written back.


![Alt text](iknow.webp?raw=true "iKnow")

In the demonstration, three pieces of text are processed by iKnow. The sentences sit in the global IKNOW:

    ^IKNOW("text","After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling")=""
    ^IKNOW("text","I liked the striped pijamas, but the slippers didn't really fit with it")=""
    ^IKNOW("text","Upon exam two weeks ago the patient's weight was 146.5 pounds")=""
    
 When the Python script **iknow.py** is run the processed data is writren back to the IKNOW global, based on the types of text in each sentence i.e.:
 
    ^IKNOW("text","I liked the striped pijamas, but the slippers didn't really fit with it", "Concept", "slippers")=""
  
The text **"I liked the striped pijamas, but the slippers didn't really fit with it"** has been taken and the word **slipper** identified as a **concept** type word.
     
and

    ^IKNOW("text","After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling", "Relation", "or")=""

The text **"After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling"** has been taken and the word **or** identified as a **relation** type word.

 # Gitpod Demo
 
1) Create a free/paid Gitpod account - https://www.gitpod.io/
2) Log into the account
3) Open a new browser tab and add **gitpod.io/#https://github.com/RamSailopal/iknow** to the address - This will create a new Gitpod cloud instance with three terminal windows automatically opened. The second window will be the YottaDB environment and the third window to run the iknow Python script (see the above Graphic for further details)


# References

Intersystems iKnow - https://github.com/intersystems/iknow

mg_python - https://github.com/chrisemunt/mg_python
