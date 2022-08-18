# new_temp_project

### Netflix Analysis

## Purpose
Our final project is an analysis of Netflix data captured from shows and movies that are actively being streamed in the US as of July 2022.  We gathered our data from [Kaggle](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies?select=titles.csv).

## Goal
What did we want to learn from this analysis?
With this data, we wanted to know (based on IMDB scores):
* What is the most popular movie age-certification?
* What is the best run time?
* What is/are the top genre(s)?
* Who are the best actors/directors?
* What IMDB score will a movie using these "best" qualities likely garner?

### What makes a movie the "best"? 
To find objectively the "best" traits of a movie, we based it upon the movie's IMDB score. The information we sought was the most prevalent movie age certification, genre, runtime, actor, and director. We omitted any films made outside the US. A machine learning model was created to predict the score of a movie based on what was determined to be the "best" of each category.

## Our process: 
We began cleaning the data using Google Collab with the pandas library. After converting the raw data into initial dataframes, we determined which columns had data we deemed impertinent to our analysis and dropped them. We dropped the columns for movie "description" and actor's "character" since we are not looking for best descriptions or characters based on IMDB scores. We also dropped the "seasons" column since seasons applies to TV shows- not to movies. We then filtered out all TV shows and all movies produced outside the United States.

We then used the ETL method to create two SQL databases from our cleaned and filtered data. One of our databases has the movie data and the other has the actor/director data.   
Originally, we were going to merge our two databases based on the movie ID, but we found that it duplicated the movie data since there were multiple actors credited for each movie.   
For example: without the merge we would have one set of data for the movie Titanic. If we merged the dataframes, we would then have several sets of duplicate data for each actor (Leonardo DiCaprio, Kate Winslet, ect).  
Therefore, we kept the data separated and downloaded each dataframe into a new csv file: cleaned_credits.csv and cleaned_movie_db.csv.  

In conjunction with our SQL databases, we also created an entity relationship diagram.  
![ERD](https://user-images.githubusercontent.com/96644316/182062124-d52cfd66-72bd-4460-b7f1-7488ead23090.png)  
This diagram shows the major categories of data and how it will be broken down for further analysis in our quest to find the "best".

We used logistic regression clustered centroids to undersample the data to build a machine learning model that was able to predict an IMDB score of 8.0 or above 75% of the time. Our model has a 99% accuracy.  
![image](https://user-images.githubusercontent.com/96644316/185049917-e9733790-31e2-4612-a1da-a1cff5f89094.png)  
  
From the cleaned databases, movies with scores lower than 7.9 were filtered out. This was determined because the IMDB range is out of 10, therefore we wanted only movies in the top 20% of scores. Movies with an IMDB score of 8.0 or higher were then used to find the highest frequency of age certification, genre, actor, and director. Run time was calculated based on the average run time of all movies above 8.0.

To display our data in an interactive format, we have created a flask app deployed through Heroku.

## Results
The “Best”:
* Age Certification: R
* Genre: Documentary
* Actors (tied): Bo Burnham, Leonardo DiCaprio, Bill Burr
* Directors (tied): Christopher Storer, Bo Burnham
* Run time: 108 minutes  
The highest rated movies were Inception and Forrest Gump- tied with an IMDB score of 8.8.  
There were 61% more “R” rated movies compared to the next highest rating of “G”.  
The top three genres were: Documentary, Drama, and Comedy.  
Tom Hanks was second “best” actor.  

### Limitations of analysis
The biggest limitation of our analysis is that an IMDB score is completely subjective. Any user registered to the website can submit a movie rating to contribute to the overall score.  
Another limitation is that the Netflix data is a snapshot of only movies that were available during July 2022. This is why Bo Burnham was found to be the "best" actor and director- he had specials that were released crediting him as both roles that went viral online. This skews our data based on Netflix movie contracts and surrounding cultural impact.  
An additional limitation is the fact that our movie data extends from release dates as early as 1954 to present day. Present day movies are more likely to have a higher number of votes. It is also difficult to account for extenuating factors such as overall cultural impact and societal changes since older movies have released. For this analysis, we did not weigh the IMDB scores with how many votes they had. A movie with very few votes but a high score would skew the data further.  

### Tech
These are a few of the technologies used to complete this analysis:
* Coding languages:
  * Python
  * HTML
  * CSS
  * JavaScript  
    
* Softwares:
  * Visual Studio Code
  * Microsoft Excel
  * PostgreSQL
  * DBDiagram
  * Google Colab
  * Heroku  
    
* Libraries:  
  * Pandas
  * json
  * sqlalchemy
  * config
  * time
  * Pathlib
  * Matplotlib
  * sklearn
  * tensorflow
  * numpy



