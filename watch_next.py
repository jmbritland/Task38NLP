# This Python program recommends movies to watch based on the last movie watched
import spacy
nlp = spacy.load("en_core_web_md")

# Create movie to compare class to store info about movies
class Movie_to_Compare:
    def __init__(self, title, description):
        self.title = title
        self.description = nlp(description)
        self.sim_score = 0.0
    
    def compare(self, string_to_compare):
        string_to_compare = nlp(string_to_compare)
        self.sim_score = self.description.similarity(string_to_compare)

# Create movies list from movies.txt
movies_list = []
movies_file = open("movies.txt", "r")
for line in movies_file:
    line = line.split(":")
    movies_list.append(Movie_to_Compare(line[0], line[1]))
movies_file.close()

# Create function to recommend next movie
def watch_next(movie_description):
    max_index = 0
    for current_index, movie in enumerate(movies_list):
        movie.compare(movie_description)
        if movie.sim_score > movies_list[max_index].sim_score:
            max_index = current_index
    return max_index

# Read in description of last movie watched
current_description = '''Will he save their world or destroy it? When the Hulk becomes
too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him
into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# Print out title of most similar movie
next_index = watch_next(current_description)
print(f"Watch next: {movies_list[next_index].title}")
