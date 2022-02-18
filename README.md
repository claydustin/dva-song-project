# dva-song-project
Class Project for OMSA CS 6242 utilizing Million Song Dataset to Visualize song topics over time

The datasets for this project are too large for free version control so you'll have to download to your local yourself. Download them all to the same location and call the folder something reasonable (jk call it fruits if you want). To avoid accidentally committing them from your local I provided a path variable at the top of the `example_data_pull.py` file. Set your relative path ex. `../../fruits/` and that will represent your data folder.

Million Song Dataset
1. track_metadata.db: http://millionsongdataset.com/sites/default/files/AdditionalFiles/track_metadata.db
2. mxm_dataset.db: http://millionsongdataset.com/sites/default/files/AdditionalFiles/mxm_dataset.db

You'll also need to download this file. This is where we'll get the lyrics:
https://bigml.com/user/czuriaga/gallery/dataset/5a9e785c92fb563a5d000ff6

There are like 500K+ song lyrics there. Some of those may not be in the 1million song dataset though and thus we won't be able to associate a year with the lyrics. 
