# Music Genre Prediction - Data Science
(As part of academic project, the requirement was to keep all files in one folder...)
# 
*  Trained model that determines music genre by evaluating song’s lyrics, BPM, key, scale and more...
*  Scraped over 19000 songs from amazon digital music using python and selenium.
*  Gathered song's features from MusicStax and Genius using selenium and API.
*  Extracted features from the text of each song's lyrics to quantify the value of words related to certain genre.
*  Ran test on these models Decision Tree, Naive Bayes, SVM, Logistic Regression to reach the best model.

## Code and Resources Used 
**Python Version:** 3.9  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, wordcloud, pandas_profiling, fake_useragent, lyricsgenius, json, pickle.
**Installing Requirements:**  ```pip install -r requirements.txt```  

## Web Scraping
Managed to scrape over 19000 songs differed by genres from amazon digital music:
*	Song title
*	Song Artist
*	Genre

## Data Cleaning
After scraping the data, I needed to clean it up so I can used it on function I created to achieve variables and features regard the song:

* Parsed out whether song is Explicit or not by filtering the song's title.
* Some songe has '(feat..)' and '(Remix)' which is not necessary.
* Lower case all columns and remove unnecessary whitespaces.
* Drop duplicates by song's title.
* Applied my function to get music data about the songs.
* Dropped NaN values from songs the function was unable to retrive data.
* Getting the lyrics for the remaining songs using Genius API.
* Cleaning up the lyrics, lots of false data needed to be removed.
* Most Important. Lemmetaizng the words and deleting stop words:
    * Transforming words to their root: {'Playing', 'Plays', 'Played'} --> 'Play'.
    * Common words like: 'go', 'like', 'know'.. are removed in order.

## EDA
The highlight of this phase are the different words by genre: 

* Rock Word Cloud
![alt text](https://github.com/idanrk/Genre_Prediction_Data_Science/blob/main/rock_cloud.png "Rock Word Cloud")
* Pop Word Cloud
![alt text](https://github.com/idanrk/Genre_Prediction_Data_Science/blob/main/pop_cloud.png "Pop Word Cloud")
* Country Word Cloud
![alt text](https://github.com/idanrk/Genre_Prediction_Data_Science/blob/main/country_cloud.png "Country Word Cloud")
* HipHop Word Cloud
![alt text](https://github.com/idanrk/Genre_Prediction_Data_Science/blob/main/hiphop_cloud.png "HipHop Word Cloud")

## Model Building 

First, I transformed the categorical variables into dummy variables. 
Splitted the data into train and tests sets with a test size of 20%.   


I tried three different models:
*	**Random Forest**
*	**Naive Bayes**
*	**SVM** 
*	**Logistic Regression**

## Model performance
*	**Random Forest** = 70% (After GridSearch)
*	**Naive Bayes** = 62%
*	**SVM** = 61%
*	**Logistic Regression** = 61%

![alt text](https://github.com/idanrk/Genre_Prediction_Data_Science/blob/main/confusion_matrix.png "Confusion Matrix")
