# iKnow

A demonstration of Intersystems iKnow with M based databases (YottaDB/Intersystems IRIS/Cache/GTM) 

Utilising mg_python text is read from the database and then iKnow, processed data is written back.


![Alt text](iknow.webp?raw=true "iKnow")

In the demonsteation, three pieces of text are processed by iKnow. THe sentences sit in the global IKNOW:

    ^IKNOW("text","After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling")=""
    ^IKNOW("text","I liked the striped pijamas, but the slippers didn't really fit with it")=""
    ^IKNOW("text","Upon exam two weeks ago the patient's weight was 146.5 pounds")=""
    
 When the Python script **iknow.py** is run the processed data is writren back to the IKNOW global based on the types of text in each sentence i.e.:
 
    ^IKNOW("text","I liked the striped pijamas, but the slippers didn't really fit with it", "Concept", "slippers")=""
  
The text **"I liked the striped pijamas, but the slippers didn't really fit with it"** has been taken and the word **slipper** identified as a **concept** type word.
     
and

    ^IKNOW("text","After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling", "Relation", "or")=""

The text **"After discussing his nausea, the patient didn't report suffering from chest pain, shortness of breath or tickling"** has been taken and the word **or** identified as a **relation** type word.
