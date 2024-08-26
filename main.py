import requests
import pandas as pd
from bs4 import BeautifulSoup

Chapter =[]
for i in range(1,79):
    url= "https://www.holy-bhagavad-gita.org/chapter/18/verse/"+str(i)
    print(url)

    response = requests.get(url)
    print(f"Status {i} : The response is {response}")
    # Parse the HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with id "translation"
    Sanskrit_Verse = soup.find(id = "originalVerse")
    # Extract the Sanskrit_Verse content
    if Sanskrit_Verse:
        Sanskrit_Verse = Sanskrit_Verse.get_text(strip=True)
    else:
        Sanskrit_Verse = None
        
    Sanskrit_Transliteration = soup.find(id = "transliteration")
    if Sanskrit_Transliteration:
        Sanskrit_Transliteration = Sanskrit_Transliteration.get_text(strip=True)
    else:
        Sanskrit_Transliteration = None
        
    WordTranslation = soup.find(id="wordMeanings")
    if WordTranslation:
        WordTranslation = WordTranslation.get_text(strip=True)
    else:
        WordTranslation = None
        
    Sanskrit_English = soup.find(id="transliteration_wo_dia")
    if Sanskrit_English:
        Sanskrit_English = Sanskrit_English.get_text(strip=True)
    else:
        Sanskrit_English = None
        
    Verse_Translation = soup.find(id="translation")    
    if Verse_Translation:
        Verse_Translation = Verse_Translation.get_text(strip=True)
    else:
        Verse_Translation = None
        
    Verse_Commentary = soup.find(id = "commentary")
    if Verse_Commentary:
        Verse_Commentary = Verse_Commentary.get_text(strip=True)
    else:
        Verse_Commentary = None
    
    Chapter.append({
        'CHAPTER': 18,
        'CHAPTER NAME SANSKRIT': "Mokṣha Sanyās Yog",
        'CHAPTER NAME ENGLISH' : "Yog through the Perfection of Renunciation and Surrender",
        "VERSE NUMBER": i,
        'SANSKRIT VERSE': Sanskrit_Verse,
        'SANSKRIT TRANSLITERATION': Sanskrit_Transliteration,
        'WORD TRANSLATION': WordTranslation,
        'SANSKRIT ENGLISH': Sanskrit_English,
        'VERSE TRANSLATION': Verse_Translation,
        'VERSE COMMENTARY': Verse_Commentary
    })

data= pd.DataFrame(Chapter)
data.to_csv("Bhagvad Chapter 18.csv")