import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movie.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

lebowski = movie.Movie("The Big Lewbowski",
                       "A misunderstanding leads to trouble for 'the Dude'",
                       "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")

movies = [toy_story, avatar, lebowski]

# Here we pass our movie instances array to the imported fresh_tomatoes
# which then generates an html page and opens it in the browser
fresh_tomatoes.open_movies_page(movies)
