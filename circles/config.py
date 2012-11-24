#######################################
# Credits:
#   aaronasterling http://stackoverflow.com/users/376728/aaronasterling
#   Michal Karm Babacek karm@email.cz
#
# License:
#   http://creativecommons.org/licenses/by-sa/3.0/
#   Provided the code remains open.
#######################################

# TL;DR
# Manipulate CIRCLES and SORT_PARAM_1 and SORT_PARAM_2





# Long: After sorting the radii in descending order by size, the list 
#       is split along SORT_PARAM_1 and the second piece # is randomized.
#       The pieces are then added back together and the list is split along
#       SORT_PARAM_2 and the first piece is shuffled.
#       The lists are then added together and returned.
#
# Short: These constants manipulate how much we care about ideal shape,
#        keeping things in the circle. With less ordered result we get more natural
#        look though it might not be desired.
# (1, 0) = totally sorted   - appealing border, very dense center, sparse midradius
# (0, 1), (1, 1) = totally randomized  - well packed center, ragged border
SORT_PARAM_1 = .80 
SORT_PARAM_2 = .20 

# These constants control how close our points are placed to each other
RADIAL_RESOLUTION = .4
ANGULAR_RESOLUTION = .4

# This keeps the boundaries from touching (space between boundaries)
PADDING = 2

# Svg canvas size
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 1000

# Where to put the workplace
X_OFFSET = CANVAS_WIDTH / 2
Y_OFFSET = CANVAS_HEIGHT / 2

# Color is static, yet we can play with it in future,
# e.g. accordingly to radius :-)
COLOR_FILL = "#FF0000"
COLOR_STROKE = "#000000"

# Circles
# This is probably the most important part of our configuration:
# You may distribute various sizes of circles. The default features
# three categories: big, medium and small. You can add another
# line and get e.g. some micro circles:
#    {'min_radius': 1, 'max_radius': 3, 'how_many': 40 },
CIRCLES = [
{'min_radius': 40, 'max_radius': 100, 'how_many': 3 },
{'min_radius': 20, 'max_radius': 35, 'how_many': 20 },
{'min_radius': 5, 'max_radius': 18, 'how_many': 100 }
]

# Output for our svg
OUTPUT_FILE = "circle.svg"