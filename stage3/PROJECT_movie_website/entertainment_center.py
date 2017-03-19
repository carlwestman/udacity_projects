import media
import fresh_tomatoes


forest_gump = media.Movie(title="Forest Gump",
                          storyline="Forrest Gump is a simple man with a low I.Q. but good intentions. He is running through childhood with his best and only friend Jenny. His 'mama' teaches him the ways of life and leaves him to choose his destiny. Forrest joins the army for service in Vietnam, finding new friends called Dan and Bubba, he wins medals, creates a famous shrimp fishing fleet, inspires people to jog, starts a ping-pong craze, creates the smiley, writes bumper stickers and songs, donates to people and meets the president several times. However, this is all irrelevant to Forrest who can only think of his childhood sweetheart Jenny Curran, who has messed up her life. Although in the end all he wants to prove is that anyone can love anyone.",
                          trailer_youtube_url="https://www.youtube.com/watch?v=uPIEn0M8su0",
                          poster_image_url="https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                          actors=["Tom Hanks", "Robin Wright", "Gary Sinise"],
                          imdb_rating=8.8,
                          genre=["Comedy", "Drama", "Romance"],
                          year="1994",
                          director="Robert Zemeckis")


platoon = media.Movie(title="Platoon",
                      storyline="Chris Taylor is a young, naive American who gives up college and volunteers for combat in Vietnam. Upon arrival, he quickly discovers that his presence is quite nonessential, and is considered insignificant to the other soldiers, as he has not fought for as long as the rest of them and felt the effects of combat. Chris has two non-commissioned officers, the ill-tempered and indestructible Staff Sergeant Robert Barnes and the more pleasant and cooperative Sergeant Elias Grodin. A line is drawn between the two NCOs and a number of men in the platoon when an illegal killing occurs during a village raid. As the war continues, Chris himself draws towards psychological meltdown. And as he struggles for survival, he soon realizes he is fighting two battles, the conflict with the enemy and the conflict between the men within his platoon.",
                      trailer_youtube_url="https://www.youtube.com/watch?v=AykiF9YYF2U",
                      poster_image_url="https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg",
                      actors=["Charlie Sheen", "Tom Berenger", "Willem Dafoe"],
                      imdb_rating=8.1,
                      genre=["Drama", "War"],
                      year="1986",
                      director="Oliver Stone")

wallstreet = media.Movie(title="Wall street",
                         storyline="Bud Fox is a Wall Street stockbroker in early 1980's New York with a strong desire to get to the top. Working for his firm during the day, he spends his spare time working an on angle with the high-powered, extremely successful (but ruthless and greedy) broker Gordon Gekko. Fox finally meets with Gekko, who takes the youth under his wing and explains his philosophy that 'Greed is Good'. Taking the advice and working closely with Gekko, Fox soon finds himself swept into a world of 'yuppies', shady business deals, the 'good life', fast money, and fast women; something which is at odds with his family including his estranged father and the blue-collared way Fox was brought up.",
                         trailer_youtube_url="https://www.youtube.com/watch?v=FCctqbRrsBQ",
                         poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Wall_Street_film.jpg/220px-Wall_Street_film.jpg",
                         actors=["Charlie Sheen", "Michael Douglas", "Tamara Tunie"],
                         imdb_rating=7.1,
                         genre=["Crime", "Drama"],
                         year="1987",
                         director="Oliver Stone")


midnight_in_paris = media.Movie(title="Midnight in Paris",
                                storyline="Gil and Inez travel to Paris as a tag-along vacation on her parents' business trip. Gil is a successful Hollywood writer but is struggling on his first novel. He falls in love with the city and thinks they should move there after they get married, but Inez does not share his romantic notions of the city or the idea that the 1920s was the golden age. When Inez goes off dancing with her friends, Gil takes a walk at midnight and discovers what could be the ultimate source of inspiration for writing. Gil's daily walks at midnight in Paris could take him closer to the heart of the city but further from the woman he's about to marry.",
                                trailer_youtube_url="https://www.youtube.com/watch?v=BYRWfS2s2v4",
                                poster_image_url="https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                actors=["Owen Wilson", "Rachel McAdams", "Kathy Bates"],
                                imdb_rating=7.7,
                                genre=["Comedy", "Fantasy", "Romance"],
                                year="2011",
                                director="Woody Allen")

life_aquatic = media.Movie(title="Life Aquatic",
                           storyline="When his partner is killed by the mysterious and possibly nonexistent Jaguar Shark, Steve Zissou and his Team Zissou crew set off for an expedition to hunt down the creature. Along with his estranged wife, a beautiful journalist and a co-pilot who could possibly be Zissou's son, the crew set off for one wild expedition.",
                           trailer_youtube_url="https://www.youtube.com/watch?v=yh401Rmkq0o",
                           poster_image_url="https://upload.wikimedia.org/wikipedia/en/thumb/7/7c/Lifeaquaticposter.jpg/220px-Lifeaquaticposter.jpg",
                           actors=["Bill Murray", "Owen Wilson", "Anjelica Huston"],
                           imdb_rating=7.4,
                           genre=["Adventure", "Comedy", "Drama"],
                           year="2004",
                           director="Wes Anderson")

friends = media.TvShow(title="Friends",
                       storyline="Rachel Green, Ross Geller, Monica Geller, Joey Tribbiani, Chandler Bing and Phoebe Buffay are all friends, living off of one another in the heart of New York City. Over the course of ten years, this average group of buddies goes through massive mayhem, family trouble, past and future romances, fights, laughs, tears and surprises as they learn what it really means to be a friend.",
                       trailer_youtube_url="https://www.youtube.com/watch?v=Eibl9JIpcKk",
                       poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTg4NzEyNzQ5OF5BMl5BanBnXkFtZTYwNTY3NDg4._V1._CR24,0,293,443_UX182_CR0,0,182,268_AL_.jpg",
                       actors=["Jennifer Aniston", "Courteney Cox", "Lisa Kudrow", "Matthew Perry", "David Schwimmer", "Matt LeBlanc"],
                       imdb_rating=9.0,
                       genre=["Comedy", "Romance"],
                       start_year="1994",
                       end_year="2004",
                       seasons=10,)

big_bang_theory = media.TvShow(title="Big Bang Theory",
                               storyline="Leonard Hofstadter and Sheldon Cooper are both brilliant physicists working at Cal Tech in Pasadena, California. They are colleagues, best friends, and roommates, although in all capacities their relationship is always tested primarily by Sheldon's regimented, deeply eccentric, and non-conventional ways. They are also friends with their Cal Tech colleagues mechanical engineer Howard Wolowitz and astrophysicist Rajesh Koothrappali. The foursome spend their time working on their individual work projects, playing video games, watching science-fiction movies, or reading comic books. As they are self-professed nerds, all have little or no luck with women. When Penny, a pretty woman and an aspiring actress from Omaha, moves into the apartment across the hall from Leonard and Sheldon's, Leonard has another aspiration in life, namely to get Penny to be his girlfriend.",
                               trailer_youtube_url="https://www.youtube.com/watch?v=3WPSDiTuHWQ",
                               poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNDMxNjQyN15BMl5BanBnXkFtZTgwNzA4NDQwMDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                               actors=["Johnny Galecki", "Jim Parsons", "Kaley Cuoco", "Simon Helberg", "Kunal Nayyar", "Melissa Rauch", "Mayim Bialik"],
                               imdb_rating=8.3,
                               genre=["Comedy", "Romance"],
                               start_year="2007",
                               seasons=10)

game_of_thrones = media.TvShow(title="Game of Thrones",
                               storyline="In the mythical continent of Westeros, several powerful families fight for control of the Seven Kingdoms. As conflict erupts in the kingdoms of men, an ancient enemy rises once again to threaten them all. Meanwhile, the last heirs of a recently usurped dynasty plot to take back their homeland from across the Narrow Sea.",
                               trailer_youtube_url="https://www.youtube.com/watch?v=8Ld-1Puov00",
                               poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTcxODc2Ml5BMl5BanBnXkFtZTgwMjMyMDk2MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                               actors=["Peter Dinklage","Lena Headey","Emilia Clarke","	Kit Harington","Sophie Turner"],
                               imdb_rating=9.5,
                               genre=["Adventure", "Drama", "Fantasy"],
                               start_year='2011',
                               seasons=7)

modern_family = media.TvShow(title="Modern Family",
                             storyline="Told from the perspective of an unseen documentary filmmaker, the series offers an honest, often-hilarious perspective of family life. Parents Phil and Claire yearn for an honest, open relationship with their three kids. But a daughter who is trying to grow up too fast, another who is too smart for her own good, and a rambunctious young son make it challenging. Claire's dad, Jay, and his Latina wife, Gloria, are raising two sons together, but people sometimes believe Jay to be Gloria's father. Jay's gay son, Mitchell, and his partner, Cameron, have adopted a little Asian girl, completing one big -- straight, gay, multicultural, traditional -- happy family.",
                             trailer_youtube_url="https://www.youtube.com/watch?v=8RR9r2XyIhQ",
                             poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BNzRjOTE1ZTEtMTkwYy00MDQ4LTkxMmYtNzgxMWFlY2YyZjU2XkEyXkFqcGdeQXVyMzAzNTY3MDM@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             actors=["Ed O'Neill", "Sofia Vergara", "Julia Bowen", "Ty Burell", "Jesse Tyler Ferguson", "Eric Stonestreet"],
                             imdb_rating=8.5,
                             genre=["Comedy", "Romance"],
                             start_year='2009',
                             seasons=8)

silicon_valley = media.TvShow(title="Silicon Valley",
                              storyline="In the high-tech gold rush of modern Silicon Valley, the people most qualified to succeed are the least capable of handling success. A comedy partially inspired by Mike Judge's own experiences as a Silicon Valley engineer in the late 1980s.",
                              trailer_youtube_url="https://www.youtube.com/watch?v=r8sCCf82Nf8",
                              poster_image_url="https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwNTUzNzIxM15BMl5BanBnXkFtZTgwMzQ1NTk2ODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                              actors=["Thomas Middleditch", "T.J. Miller", "Josh Brener", "Martin Starr", "Kumail Nanjiani", "Amanda Crew"],
                              imdb_rating=8.5,
                              genre=["Comedy"],
                              start_year='2014',
                              seasons=4)

media = [forest_gump, platoon, wallstreet, midnight_in_paris, life_aquatic, big_bang_theory, game_of_thrones, modern_family, friends, silicon_valley]
fresh_tomatoes.open_movies_page(media=media)







