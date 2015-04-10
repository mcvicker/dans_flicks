# import class definitions and webpage generator functions
import media
import dans_flicks

# instantiate a series of Movie objects

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

aliens = media.Movie("Aliens", "Space Marines and Xenomorphs locked in a battle to the death",
                     "http://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
                     "https://www.youtube.com/watch?v=RppKRCLW9OM")

star_trek_ii = media.Movie("Star Trek II: The Wrath of Khan", "Khaaan!",
                           "http://upload.wikimedia.org/wikipedia/en/9/9a/Star_Trek_II_The_Wrath_of_Khan.png",
                           "https://www.youtube.com/watch?v=Z8rOUVc2sCc")

shawshank_redemption = media.Movie("The Shawshank Redemption", "A man learns the meaning of hope in a dark place",
                                   "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

out_of_sight = media.Movie("Out of Sight","A cop and a robber have a love affair",
                          "http://upload.wikimedia.org/wikipedia/en/7/70/Outofsight.jpg",
                          "https://www.youtube.com/watch?v=A_GOrRyhABg")

skyfall = media.Movie("Skyfall", "James Bond returns to his roots",
                      "http://www.flicksandbits.com/wp-content/uploads/2012/09/skyfall-movie-poster.jpg",
                      "https://www.youtube.com/watch?v=6kw1UVovByw")

# create a list from the Movie objects
movies = [aliens,out_of_sight,shawshank_redemption,skyfall,star_trek_ii,toy_story]

# run webpage generator against the list 'movies'
dans_flicks.open_movies_page(movies)
