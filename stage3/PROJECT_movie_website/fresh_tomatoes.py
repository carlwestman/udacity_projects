import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }

        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile-container {

        }
        .movie-tile {
            padding-top: 5px;
            padding-bottom:5px;

        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .panel-heading{
            margin-bottom:0px;
        }
        .panel-body{
            padding:0px;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile-container').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img class="center" src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes My Favorite Movies and TV Shows </a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile-container">
    <div class="panel panel-default">
        <div class="panel-body">
            <div class="movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
                <img src="{poster_image_url}" width="220" height="342">
                <h2> {movie_title} </h2>
            </div>
        </div>
        <div class="panel-footer text-center info-modal">
            <a href="#" class="glyphicon glyphicon-info-sign" data-toggle="modal" data-target="#{modalid}"></a>
        </div>
    </div>

    <div class="modal fade" id="{modalid}" tabindex="-1" role="dialog" aria-labelledby="MediaInfoModal" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                    <h4 class="modal-title">{movie_title}</h4>
                </div>
                <div class="modal-body">
                    <table class="table table-hover">
                        <tr>
                            <td>Type:</td>
                            <td>{type}</td>
                        </tr>
                        <tr>
                            <td>Storyline:</td>
                            <td>{storyline}</td>
                        </tr>
                        <tr>
                            <td>Actors:</td>
                            <td>{actors}</td>
                        </tr>
                        <tr>
                            <td>IMDB Rating:</td>
                            <td>{imdb_rating}</td>
                        </tr>
                        <tr>
                            <td>Genre:</td>
                            <td>{genre}</td>
                        </tr>
                        <tr>
                            <td>Year(s)</td>
                            <td>{year}</td>
                        </tr>
                        <tr>
                            <td>Seasons</td>
                            <td>{seasons}</td>
                        </tr>
                    </table>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</div>
'''


def create_media_tiles_content(media):
    # The HTML content for this section of the page
    content = ''
    for media_item in media:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', media_item.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', media_item.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        if media_item.__class__.__name__ == 'TvShow':
            seasons = media_item.seasons
            if media_item.end_year:
                year = media_item.start_year + "-" + media_item.end_year
            else:
                year = media_item.start_year + "-"
        else:
            seasons = "N/A"
            year = media_item.year

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=media_item.title,
            poster_image_url=media_item.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            type=media_item.type,
            storyline=media_item.storyline,
            actors=list2str(media_item.actors),
            imdb_rating=media_item.imdb_rating,
            genre=list2str(media_item.genre),
            year=year,
            seasons=seasons,
            modalid=create_modal_id(media_item.title)
        )
    return content


def open_movies_page(media):

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(movie_tiles=create_media_tiles_content(media))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible

def list2str(list):
    """Takes in a list and returns a comma separated string of list items"""
    string = ''
    for i, item in enumerate(list):
        string += item
        if i < len(list)-1:
            string += ", "
    return string

def create_modal_id(title):
    """Returns string of title where blankspace is replaced with _ """
    return title.replace(" ", "_")