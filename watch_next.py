# in this python file, it will recommend the next movie to watch based on an entered description. 

import spacy 

# load in the appropriate model. 
nlp = spacy.load('en_core_web_md')

def recommended_movie(movie_description: str) -> str:
    """This function takes in a description and then outputs the name of the 
    movie that should be watched."""
    movie_description_nlp = nlp(movie_description)
    movies_dict = read_movie_file()
    # set up some variables to store the current highest matching percent 
    # and the movie to recommend
    best_match_percent = 0.0
    movie_to_recommend = ""
    # go through each movie in turn to get the similarity
    for movie, description in movies_dict.items():
        movie_similarity = nlp(description).similarity(movie_description_nlp)
        # if the similarity is higher than the current highest match
        # then make it the movie to watch. 
        if movie_similarity > best_match_percent:
            movie_to_recommend = movie
            best_match_percent = movie_similarity
    return movie_to_recommend

def read_movie_file()-> dict:
    """read in the movie file and store the information in a dict"""
    movies_dict = {}
    with open("movies.txt", 'r') as movies_txt:
        for line in movies_txt:
            movie = line.split(":")
            movies_dict[movie[0]] = movie[1]
    return movies_dict


movie_description = """Will he save their world or destroy it? When the Hulk 
becomes too dangerous for the Earth, the Illuminati trick Hulk into a 
shuttle and launch him into space to a planet where the Hulk can live in 
peace. Unfortunately, Hulk land on the planet Sakaar where he is sold
into slavery and trained as a gladiator."""

movie_to_recommend = recommended_movie(movie_description)
print(f"Based on the description you entered, you should watch {movie_to_recommend}.")




