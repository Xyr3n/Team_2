## Project 1 Proposal
#### Proposal Title:
Spotify Music Popularity 

#### Team Members:
Richard Bialick, Julio Dela Cruz, Tim Haake, Kylie Li, Nancy Zheng

#### Project Description:
In our project we analyzed different audio features that may contribute to popularity of the top tracks from [the top 10 artists globally in 2023](https://newsroom.spotify.com/2023-11-29/top-songs-artists-podcasts-albums-trends-2023/) on Spotify. We made conclusions on current and future trends based on comparing various audio features to music popularity.

#### Research Questions to Answer:
How is popularity of popular music affected by audio features such as acousticness, tempo, energy, loudness, speechiness, danceability, and valence?

Using the correlation between popularity and audiofeatures, what can we predict about future music trends?

#### Datasets to Be Used:
[Spotify Web API](https://developer.spotify.com/documentation/web-api)  
[The Top 10 Artists Globally in 2023](https://newsroom.spotify.com/2023-11-29/top-songs-artists-podcasts-albums-trends-2023/)  

**Track ID API Endpoint to Extract Audio Features**
track_id = '1BxfuPKGuaTgP7aM0Bbdwr'  
https://api.spotify.com/v1/audio-analysis/{track_id}  

**Top 10 Artist URI ID: ** 
1. Taylor Swift: spotify:artist:06HL4z0CvFAxyc27GXpf02
2. Drake: drake_uri= spotify:artist:3TVXtAsR1Inumwj472S9r4
3. Travis Scott: spotify:artist:0Y5tJX1MQlPlqiwlOH1tJY
4. Zach Bryan: spotify:artist:40ZNYROS4zLfyyBSs2PGe2
5. Kanye West: spotify:artist:5K4W6rqBFWDnAN6FQUkS6x
6. The Weeknd: spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ
7. Morgan Wallen: spotify:artist:4oUHIQIBe0LHzYfvXNW4QM
8. 21 Savage: spotify:artist:1URnnhqYAYcrqrcwql10ft
9. Bad Bunny: spotify:artist:4q3ewBCX7sLwd24euuV69X
10. Future: spotify:artist:1RyvyyTE3xzB2ZywiAwp0i

Note: Please see python notebook for the full dataset including top tracks from each artist

#### Rough Breakdown of Tasks:
**Order of Tasks:**
- Extract Data from Spotify by Requesting data via Python API 
- Cleaning data and format into Dataframes & merging Dataframes
- Matplotlib/Pandas Plots
- Statistical Analysis using Linear Regession & Correlation with the Dependent Variable (y) as Popularity
- Write-up & Slide Deck of the Analysis
- Update main branch via commit and branch merging in Github

**Ricky Bialick:** 
- Data Extraction
- Plot Correlation & Regression line between Loudness vs Popularity with conclusion of analysis  

**Julio Dela Cruz:**
- Plot Correlation & Regression line between Danceablity vs Popularity with conclusion of analysis
- Plot Correlation & Regression line between Energy vs Popularity with conclusion of analysis  

**Tim Haake:**
- Data Extraction
- Data Cleaning
- Plot Correlation & Regression line between Acousticness vs Popularity with conclusion of analysis

**Kylie Li:**
- Plot Correlation & Regression line between Valence vs Popularity with conclusion of analysis
- Plot Correlation & Regression line between Speechiness vs Popularity with conclusion of analysis  
- Merging Tables  

**Nancy Zheng:**
- Proposal Draft & Edits
- Plot Correlation & Regression line between Tempo vs Popularity with conclusion of analysis
- Write-up Draft & Edits
- Slide Deck Draft & Edits

#### Link to Github Repo
https://github.com/Xyr3n/Team_2

#### Github Names of People On Project (username, email or other)
- Ricky Bialick: fingerClub 
- Julio Dela Cruz: juliodelacruzz 
- Tim Haake: thaake408 
- Kylie Li: Xyr3n 
- Nancy Zheng: zhengn95

