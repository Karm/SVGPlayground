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
SORT_PARAM_1 = .70 
SORT_PARAM_2 = .30 


# Circles
# This is probably the most important part of our configuration:
# You may distribute various sizes of circles. The default features
# three categories: big, medium and small. You can add another
# line and get e.g. some micro circles:
#    {'min_radius': 1, 'max_radius': 3, 'how_many': 40 },
CIRCLES = [
{'min_radius': 60, 'max_radius': 100, 'how_many': 4 },
{'min_radius': 15, 'max_radius': 60, 'how_many': 200 },
{'min_radius': 3, 'max_radius': 14, 'how_many': 600 }
]









# These constants control how close our points are placed to each other
RADIAL_RESOLUTION = 2
ANGULAR_RESOLUTION = 2

# This keeps the boundaries from touching (space between boundaries)
PADDING = 2

# Svg canvas size
CANVAS_WIDTH = 2000
CANVAS_HEIGHT = 2000

# Where to put the workplace
X_OFFSET = CANVAS_WIDTH / 2
Y_OFFSET = CANVAS_HEIGHT / 2


# If COLOR_FILLis not None, e.g. : COLOR_FILL = "#FF0000", we use it.
# Othervice, the color is calculateg as HSV (radius, 60, 60).
COLOR_FILL = None
COLOR_STROKE = "#000000"
STROKE_WIDTH = 2

# Output for our svg
OUTPUT_FILE = "circle.svg"

TOOLTIP_SCRIPT = """
    function init(evt)
    {
        if ( window.svgDocument == null )
        {
        svgDocument = evt.target.ownerDocument;
        }

        tooltip = svgDocument.getElementById('tooltip');
        tooltip_bg = svgDocument.getElementById('tooltip_bg');

    }

    function ShowTooltip(evt, mouseovertext)
    {
        tooltip.setAttributeNS(null,\"x\",evt.pageX+11);
        tooltip.setAttributeNS(null,\"y\",evt.pageY+27);
        tooltip.firstChild.data = mouseovertext;
        tooltip.setAttributeNS(null,\"visibility\",\"visible\");

        length = tooltip.getComputedTextLength();
        tooltip_bg.setAttributeNS(null,\"width\",length+8);
        tooltip_bg.setAttributeNS(null,\"x\",evt.pageX+8);
        tooltip_bg.setAttributeNS(null,\"y\",evt.pageY+14);
        tooltip_bg.setAttributeNS(null,\"visibility\",\"visibile\");
    }

    function HideTooltip(evt)
    {
        tooltip.setAttributeNS(null,\"visibility\",\"hidden\");
        tooltip_bg.setAttributeNS(null,\"visibility\",\"hidden\");
    }
"""

TOOLTIP_STYLE = """
    .caption {
        font-size: 14px;
        font-family: Georgia, serif;
    }
    .tooltip {
        font-size: 12px;
    }
    .tooltip_bg {
        fill: white;
        stroke: black;
        stroke-width: 1;
        opacity: 0.85;
    }
"""