import os
import shutil

book_directory = "D:\OneDrive\BOOKS\Fiction\Gerald Seymour"
destination_directory = "D:\z-covers\RESULTS\cover"

#~ def get_covers(directory):

cover_paths = []

for root, directories, files in os.walk(book_directory):
    
    for filename in files:
        if filename.endswith('.jpg'):
            filepath = os.path.join(root, filename)
            cover_paths.append(filepath)
						
	#~ return cover_paths
	
#~ def copy_covers(cover_paths):
for index, cover in enumerate(cover_paths):
    shutil.copy(cover, destination_directory + str(index) + '.jpg')
			


