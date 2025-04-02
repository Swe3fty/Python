import png
import json
import turtle


#=========================================================================#
#                                    Part 1                               # 
#=========================================================================#
#================================Creation of the maze=====================#

def load_maze_txt(file_path):
    f = open(file_path, 'r')
    content = f.read().splitlines() #get all the line from a document
    maze = []
    for line in content:
        maze.append([int(char) for char in line]) #Transform a list of string into a list of int
    return maze

#==============Fonction that save the labyrinth into png=============#
def save_maze_png(maze_list,png_path,pixel_length: int =20):
    color = {       #define all the colors
        'black': (0,0,0),
        'red': (255,0,0),
        'green': (0,255,0),
        'blue': (0,0,255),
        'white': (255,255,255)
    }
    rows = []
    for i in range(len(maze_list)):
        row = []
        for j in range(len(maze_list[i])):
            value = str(maze_list[i][j])
            if(value == "0"):
                row.extend(color['white'] * pixel_length) #for each color * pixel width and height
            elif(value == "1"):
                row.extend(color['red'] * pixel_length)
            elif(value == "2"):
                row.extend(color['black']* pixel_length )
            elif(value == "3"):
                row.extend(color['green'] * pixel_length)
        for _ in range(pixel_length):   #at the end add the row constructed with the pixel length
            rows.append(row)
    image = png.from_array(rows, "RGB") #Transform my list into an image
    image.save(png_path) #save my image



#=========================================================================#
#                                    Part 2                               # 
#=========================================================================#
#=====================Get the information of a json file==================#

def load_maze_parameter(json_file_path):
    with open(json_file_path) as f:
        json_data = json.load(f)
    maze_info = json_data
    return maze_info





#=========================================================================#
#                                    Part 3                               # 
#=========================================================================#

#============Convert a coord into pixel_coord in x========================#

def coord_to_pixel_x(x,maze_json,maze_list):
    pixel_size = maze_json['style']["cell_size_png"]
    number_of_square = len(maze_list)
    x_pixel = x*pixel_size-((number_of_square-1)*pixel_size)/2
    return x_pixel

#============Convert a coord into pixel_coord in y========================#

def coord_to_pixel_y(y,maze_json,maze_list):
    pixel_size = maze_json['style']["cell_size_png"]
    number_of_square = len(maze_list)
    y_pixel = -y*pixel_size+((number_of_square-1)*pixel_size)/2
    return y_pixel

#===========Search for the exit of the labyrinth=========================#

def search_exit(maze_json,maze_list):
    
    x_begin = 0
    y_begin = 1

    turtle_attributes(maze_json)
    
    turtle.up()
    moveTurtle(x_begin,y_begin,maze_list)
    turtle.down()
    moveTurtle(1,1,maze_list)
    turtle.up
    find_Path(maze_json,maze_list)

    turtle.exitonclick()

    return

#===========Find Path algorithm function=================================#
def find_Path(maze_json,maze_list):
    directions = {
        "north" : (0,1),
        "south" : (0,-1),
        "east" : (1,0),
        "west" : (-1,0)
    }

#===========Move the turtle to a place to another========================#

def moveTurtle(x,y,maze_list):
    x_pixel = coord_to_pixel_x(x,maze_json,maze_list)
    y_pixel = coord_to_pixel_y(y,maze_json,maze_list)
    turtle.goto(x_pixel,y_pixel)

#===========Turtle attributes============================================#
def turtle_attributes(maze_json):
    turtle.setup(900,900)
    turtle.bgpic(maze_json["maze_files"]["maze_file_png"])
    turtle.title('Maze')
    turtle.pencolor(maze_json["style"]["pen_colors"]["forward_pen_color"])
    turtle.shape(maze_json["style"]["pen_shape"])

#==========================Global program================================#

maze_json = load_maze_parameter("labyrinth.json")
maze_list = load_maze_txt(maze_json['maze_files']["description_file"])
print(maze_list)
save_maze_png(maze_list,maze_json['maze_files']["maze_file_png"],maze_json['style']["cell_size_png"])
search_exit(maze_json,maze_list)






