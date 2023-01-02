import spacy  # importing spacy
nlp = spacy.load('en_core_web_md')

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Open the txt file & create a new list called movies_descr
f = open('movies.txt', 'r+')
movies_descr = []
movies_title = []

# For each line in the movies.txt file, add it to a list
for line in f:
    line = line.split(':')
    movies_title.append(line[0])
    movies_descr.append(line[1])

f.close()

planet_hulk = nlp(planet_hulk)

similarity_scores = []

for description in movies_descr:
    similarity = nlp(description).similarity(planet_hulk)
    similarity_scores.append(similarity)
    print(description + " - ", similarity)

similair_movie_index = movies_descr.index(max(movies_descr))

print(movies_title[similair_movie_index])