import media
import fresh_tomatoes

#create instances of different movies
toy_story = media.Movie(
    "Toy Story",
    "story of boy and toys",
    "http://www.impawards.com/2010/posters/toy_story_three_ver10.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "Vierd blue people",
    "https://cdn.movieweb.com/img.news.tops/NEF2TArJYNFmJL_1_a/Avatar-2-Sequels-"
    "Underwater-Scenes-Motion-Capture.jpg",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

anchorman = media.Movie(
    "Anchorman",
    "Comedy of a news anchor working in San Diego",
    "https://images-na.ssl-images-amazon.com/images/I/91TXzLjVV-L._SX342_.jpg",
    "https://www.youtube.com/watch?v=-T3wnP91OnI")

zoolander = media.Movie(
    "Zoolander",
    "A male fashion artist trying to stay ahead of the curve",
    "https://ia.media-imdb.com/images/M/MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEw"
    "OTMxMDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
    "https://www.youtube.com/watch?v=MaEeSJZYkpY")

threehundred = media.Movie(
    "Anchorman",
    "the story of Spartans",
    "https://static.rogerebert.com/uploads/movie/movie_poster/300-2006/large_4"
    "AmPMxTs1zSdCK0eCacj0kBgOMV.jpg",
    "https://www.youtube.com/watch?v=UrIbxk7idYA")

singstreet = media.Movie(
    "Sing Street",
    "A group of teenagers create a band",
    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2c/Sing_Street_poster."
    "jpeg/220px-Sing_Street_poster.jpeg",
    "hhttps://www.youtube.com/watch?v=C_YqJ_aimkM")

#add movies to a list
movies = [
    toy_story,
    avatar,
    anchorman,
    zoolander,
    threehundred,
    singstreet]

# pass list of movies to be displayed on webpage: 
fresh_tomatoes.open_movies_page(movies)
