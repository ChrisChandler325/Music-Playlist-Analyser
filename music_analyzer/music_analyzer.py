def played(music):
   countPlayed = 0
   countNot = 0
   #if played +1 if not played +1
   for song in music:
      if song[25] != "":
         countPlayed += 1
      else:
         countNot += 1
   #print songs
   print(f"Songs that have been played: {countPlayed}")
   print(f"Songs that have not been played: {countNot}")      

def genre(music):
   genre = []
   #get genre
   for song in music:
      genre.append(song[9])
   genres = dict()
   #get dict with genre and count as pair
   for i in genre:
    genres[i] = genres.get(i, 0) + 1
   #print number of songs in genre and make a temp list that will find min and max time
   for k, d in genres.items():
      tempr = []
      for song in music:
         if k == song[9]:
            tempr.append(song)
      print(f"There were {d} song(s) from the genre '{k}' in the playlist. ")
      max(tempr)
      min(tempr)
      print('-----------------------------------------------------------')

def year(music):
   years = []
   #get years
   for line in music:
      years.append(line[16])
   counts = dict()
   #make dict with years and count as pair
   for i in years:
      counts[i] = counts.get(i, 0) + 1
   for k, d in counts.items():
      print(f"There were {d} song(s) from the year '{k}' in the playlist")

def max(music):
   length = []
   x=0
   #get rid of songs with no time, and convert string to int
   for song in music:
      if song[11] != "":
         temp = int(song[11])
         #find maximum value
         if x <= temp:
            x = temp
   #loop through list again but this time compare max time to song time
   for song in music:
      if song[11] != "":
         #most annoying part, cant convert from string, must go to variable first
         temp = int(song[11])
         if x == temp:
            length.append(song)
   for song in length:
      print(f"The longest songs are: {song[0]} by {song[1]}")

def min(music):
   #same exact code as max but opposite
   length =[]
   x=9999999999
   for song in music:
      if song[11] != "":
         temp = int(song[11])
         if x >= temp:
            x = temp
   for song in music:
      if song[11] != "":
         temp = int(song[11])
         if x == temp:
            length.append(song)
   for song in length:
      print(f"Shortest songs in playlist are {song[0]} by {song[1]}")


headers = []
music = []

#open file/get header
while True:
   try:
      name = input("Please type file name followed by a '.txt' for (example: 'iTunes_Music.txt'): ")
      f = open(name,encoding='utf-16')
   except:
      print("invalid filename.")
      continue

   headers = f.readline().split('\t')
   #get music and number of songs in playlist and close file
   for line in f:
       music.append(line.split('\t'))
   print("Total Number of songs:",len(music))
   f.close()
   # Get songs per yer
   year(music)
   #Get longest song
   max(music)
   #Get shortest song
   min(music)
   #get num songs in genre, longest song, and shortest song song[9]
   genre(music)
   #Number of songs that have/haven't been played.
   played(music)
   if(input("Would you like to analyze another file? y/n?") != 'y'):
      print('thank you and have a nice day.')
      break
   else:
      continue