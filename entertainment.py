import media
import fresh_tomatoes


dangal = media.Movie("Dangal", "Sports", "img/Dangal_Poster.jpg", 
                   "https://www.youtube.com/watch?v=x_7YlGv9u1g")

raees = media.Movie("Raees", "Drama", "img/Raees_Poster.jpg" ,
                  "https://www.youtube.com/watch?v=J7_1MU3gDk0")

kaabil = media.Movie("Kaabil", "Drama", "img/Kaabil_Movie_Poster.jpg",
                   "https://www.youtube.com/watch?v=nubDFeiUAsI")

jolly_llb = media.Movie("Jolly_LLB", "Comedy", "img/Jolly_LLB_2_first_look.jpg",
                      "https://www.youtube.com/watch?v=q07SQFmL4rM")

sultan = media.Movie("Sultan", "Sports", "img/Sultan_film_poster.jpg",
                   "https://www.youtube.com/watch?v=wPxqcq6Byq0")

dear_zindagi = media.Movie("Dear Zindagi", "Fiction", "img/Dear_Zindagi_poster.jpg",
                         "https://www.youtube.com/watch?v=5DkO7ksXY8E")
                   
movies=[dangal,raees,kaabil,jolly_llb,sultan,dear_zindagi]

# open_movies_page takes an array of movies instances as an arguement 
# it displays the instances on the web browser 
fresh_tomatoes.open_movies_page(movies)


