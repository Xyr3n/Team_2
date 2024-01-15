# Spotify Audio Features vs Popularity Analysis and Conclusion

#### Contributers:
Richard Bialick, Julio Dela Cruz, Tim Haake, Kylie Li, Nancy Zheng  
#### Link to Github Repo
https://github.com/Xyr3n/Team_2  

#### Project Description:
In our project we analyzed different audio features that may contribute to popularity of the top tracks from [the top 10 artists globally in 2023](https://newsroom.spotify.com/2023-11-29/top-songs-artists-podcasts-albums-trends-2023/) on Spotify. We made conclusions on current and future trends based on comparing various audio features to music popularity.

#### Research Questions to Answer:
How is popularity of popular music affected by audio features such as acousticness, tempo, energy, loudness, speechiness, danceability, and valence?

Using the correlation between popularity and audiofeatures, what can we predict about future music trends?

#### Datasets Used:
[Spotify Web API](https://developer.spotify.com/documentation/web-api)  
[The Top 10 Artists Globally in 2023](https://newsroom.spotify.com/2023-11-29/top-songs-artists-podcasts-albums-trends-2023/)  

**Top 10 Artists Streamed on Spotify in the United States - Artist ID numbers**

1. Taylor Swift - https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02?si=28979011a2f446fb
2. Drake - https://open.spotify.com/artist/3TVXtAsR1Inutravj472S9r4?si=c036ec885a6c4ab7
3. Travis Scott - https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY?si=13b2ea9ddc304c14
4. Zach Bryan - https://open.spotify.com/artist/40ZNYROS4zLfyyBSs2PGe2?si=db0c9492a4a44e5c
5. Kanye West - https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x?si=14d9933251a04f4e
6. The Weeknd - https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ?si=7fd262759d3d453f
7. Morgan Wallen - https://open.spotify.com/artist/4oUHIQIBe0LHzYfvXNW4QM?si=7c693b6829d04717
8. 21 Savage - https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft?si=f620ac02e71c485e
9. Bad Bunny - https://open.spotify.com/artist/4q3ewBCX7sLwd24euuV69X?si=aad3dd7099f742bf
10. Future - https://open.spotify.com/artist/1RyvyyTE3xzB2ZywiAwp0i?si=876369688ab64a7d**Track ID 

**API Endpoint to Extract Audio Features**  
track_href': https://api.spotify.com/v1/tracks/{Track ID}  
analysis_url': 'https://api.spotify.com/v1/audio-analysis/{Audio Analysis ID}  

*Note: Please see python notebook for the Track IDs and Audio Analysis ID's for each top track *

#### Rough Breakdown of Tasks:

**Tasks:**
- Data extraction from Spotify API by requesting data using python 
- Cleaning data and format into dataframes 
- Merging dataframes
- Statistical analysis using linear regession & correlation with the dependent variable (y) as Popularity
- Statistical analysis using boxplots and summary statistics of each audio feature
- Update main branch via commit and merge each member's analysis in github
- Write-up & slide Deck of the analysis

**Ricky Bialick:** 
- Data extraction from Spotify API
- Plot correlation & regression line between Loudness vs Popularity with conclusion of analysis 
- Statistical analysis using boxplots and summary statistics for loudness

**Julio Dela Cruz:**
- Plot correlation & regression line between danceablity vs popularity with conclusion of analysis
- Statistical analysis using boxplots and summary statistics for danceability
- Plot correlation & regression line between Energy vs Popularity with conclusion of analysis  
- Statistical analysis using boxplots and summary statistics for energy

**Tim Haake:**
- Data extraction from Spotify API
- Data cleaning & format into dataframes
- Plot correlation & regression line between Acousticness vs Popularity with conclusion of analysis
- Statistical analysis using boxplots and summary statistics for acousticness

**Kylie Li:**
- Plot correlation & regression line between Valence vs Popularity with conclusion of analysis
- Statistical analysis using boxplots and summary statistics for valence
- Plot correlation & regression line between Speechiness vs Popularity with conclusion of analysis  
- Statistical analysis using boxplots and summary statistics for speechiness
- Merging tables  

**Nancy Zheng:**
- Proposal draft & edits
- Plot correlation & regression line between Tempo vs Popularity with conclusion of analysis
- Statistical analysis using boxplots and summary statistics for tempo
- Write-up draft & edits
- Slide deck draft & edits

[Presentation Link](https://docs.google.com/presentation/d/16aQn_27_jSCnHkuAOaOS74O0h8zrKMDVw1VuPrmlfOE/edit?usp=sharing)
