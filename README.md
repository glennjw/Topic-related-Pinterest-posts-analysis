# Topic-related-Pinterest-posts-analysis
  The topic is that find the top three most influencers about "graduation commencement". 
  

Hadoop algorithms: 

		Mapper:
			1. Read text and time stamp from json files. 
			2. Search key words.
			3. Pick “owner:id”, “edge_liked_by” and time stamp.
			4. Output owner id, number of liked and time stamp .
		Reducer: 
			1. Split the received strings.
			2. Store and count owner id, number of liked and time stamp .
			3. Sort and output the result.


Results:
  
  results.png
















Pinterest dataset sample:

{'instaloader': {'node_type': 'Post', 'version': '4.2.3'},
'node': {'__typename': 'GraphImage',
'accessibility_caption': 'Image may contain: text',
'comments_disabled': False,
'dimensions': {'height': 1080, 'width': 1080},
'display_url': 'https://scontent-atl3-...',
'edge_liked_by': {'count': 15},
'edge_media_preview_like': {'count': 15},
'edge_media_to_caption': {'edges': [{'node': {'text': 'Are you
graduating this semester? Be sure to register for the Lamar Dodd School of Art
graduation ceremony! 🎓🎓 \nLearn more through the link in our bio\n#doddlife
#thedodd #artatuga #uga'}}]},
'edge_media_to_comment': {'count': 0},
'id': '1997248124665835303',
'is_video': False,
'owner': {'id': '3041334883'},
'shortcode': 'Bu3ppZnBa8n',
'taken_at_timestamp': 1552310551,
'thumbnail_resources': [{'config_height': 150,
'config_width': 150,
'src': 'https://scontent-atl3-...'},
{'config_height': 240,
'config_width': 240,

'src': 'https://scontent-atl3-...'},

{'config_height': 320,
'config_width': 320,

'src': 'https://scontent-atl3-...'},

{'config_height': 480,
'config_width': 480,
'src': 'https://scontent-atl3-...'},
{'config_height': 640,
'config_width': 640,

'src': 'https://scontent-atl3-...'}],

'thumbnail_src': 'https://scontent-atl3-...'}}
