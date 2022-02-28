###################################################################
### TweMSAS stands for "Twitter manual sentiment analysis sort" ###
###################################################################

TweMSAS is free for use. (Out of current context: Stay safe Ukranians <3)

This program needs the following data set in the "data" folder:
	- a csv file
	- with the name "tweets.csv"
	- the following data needs to have the following column labels:
		. tweet texts column -> label "text"
		. tweet author id -> label "author_id"
		. tweet id -> label "tweet_id"
		. tweet creation date -> label "created_at"

	
The program will return the following in the "results" folder:
	- a csv file 
	- with the name "results.csv"
	- the following data is contained:
		'author_id': tweet author id
            	'tweet_id': tweet id
            	text': tweet text
            	'sentiment_polarity': sentiment polarity score from -2 (negative) to +2 (positive)
            	'irony_or_sarcasm': indicator if the text appeared to be sarcastic or ironic 
					(indicating that alhorithms should have trouble indexing it properly)
            	'meme_or_domain': indicator if the text appeared to be of meme or domain specific content 
					(indicating a specific dictionary might have been able to automatically detect it)
            	'created_at': tweet creation date


Features:
	- Hotkeys for sentiment scoring (1-5)
	- Hotkeys to toggle irony/sarcasm and meme/domain checkbox (q & e)
	- Tracker, where you stopped last time
	- Indicator of where you are atm (its 0 indexed as the data files are)