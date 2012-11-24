import pylab
from numpy import random
import math
from xml.etree import ElementTree as et
from config import *

#######################################
# Credits:
#   aaronasterling http://stackoverflow.com/users/376728/aaronasterling
#   Michal Karm Babacek karm@email.cz
#
# License:
#   http://creativecommons.org/licenses/by-sa/3.0/
#   Provided the code remains open.
#######################################

# pretty tuple indices, index in tuples
X = 0
Y = 1
# next to each other, not = 1 on top of each other
RADIUS = 2

def plotCircles(circles):
    et.register_namespace("svg","http://www.w3.org/2000/svg")
    doc = et.Element('svg', width=str(CANVAS_WIDTH), height=str(CANVAS_HEIGHT), version='1.1', xmlns='http://www.w3.org/2000/svg')
    for circle in circles:
        et.SubElement(doc, 'circle', cx=str(circle[0]+X_OFFSET), cy=str(circle[1]+Y_OFFSET), r=str(circle[2]), fill=COLOR_FILL, stroke=COLOR_STROKE )
    f = open(OUTPUT_FILE, 'w')
    et.ElementTree(doc).write(f, xml_declaration = True)
    f.close()

def assert_no_intersections(f):
    def asserter(*args, **kwargs):
        circles = f(*args, **kwargs)
        intersections = 0
        for c1 in circles:
            for c2 in circles:
                if c1 is not c2 and distance(c1, c2) < c1[RADIUS] + c2[RADIUS]:
                    intersections += 1
                    break
        print "{0} intersections".format(intersections)
        if intersections:
            raise AssertionError('Doh!')
        return circles
    return asserter

@assert_no_intersections
def positionCircles(rn):

    points = base_points(ANGULAR_RESOLUTION, RADIAL_RESOLUTION)
    free_points = []
    radii = fix_radii(rn)

    circles = []
    point_count = 0
    for radius in radii:
        print "{0} free points available, {1} circles placed, {2} points examined".format(len(free_points), len(circles), point_count)
        i, L = 0, len(free_points)
        while i < L:
            if available(circles, free_points[i], radius):
                make_circle(free_points.pop(i), radius, circles, free_points)
                break  
            else:
                i += 1   
        else:
            for point in points:
                point_count += 1
                if available(circles, point, radius):
                    make_circle(point, radius, circles, free_points) 
                    break
                else:
                    if not contained(circles, point):
                        free_points.append(point)
    return circles

def fix_radii(radii):
    radii = sorted(rn, reverse=True)
    radii_len = len(radii)

    section1_index = int(radii_len * SORT_PARAM_1)
    section2_index = int(radii_len * SORT_PARAM_2)

    section1, section2 = radii[:section1_index], radii[section1_index:]
    random.shuffle(section2)
    radii = section1 + section2

    section1, section2 = radii[:section2_index], radii[section2_index:]
    random.shuffle(section1)
    return section1 + section2

def make_circle(point, radius, circles, free_points):
    new_circle = point + (radius, )
    circles.append(new_circle)
    i = len(free_points) - 1
    while i >= 0:
        if contains(new_circle, free_points[i]):
            free_points.pop(i)
        i -= 1
                   
def available(circles, point, radius):
    for circle in circles:
        if distance(point, circle) < radius + circle[RADIUS] + PADDING:
            return False
    return True
        

def base_points(radial_res, angular_res):
    circle_angle = 2 * math.pi
    r = 0
    while 1:
        theta = 0
        while theta <= circle_angle:
            yield (r * math.cos(theta), r * math.sin(theta))
            r_ = math.sqrt(r) if r > 1 else 1
            theta += angular_res/r_
        r += radial_res    


def distance(p0, p1):
    return math.sqrt((p0[X] - p1[X])**2 + (p0[Y] - p1[Y])**2) 

def contains(circle, point):
    return distance(circle, point) < circle[RADIUS] + PADDING

def contained(circles, point):
    return any(contains(c, point) for c in circles)


if __name__ == '__main__':
    
    rn = []

    for circle in CIRCLES:
        for x in range(circle['how_many']):
            rn.append(random.randint(circle['min_radius'], circle['max_radius']))

    """ USING LOGNORMAL DISTRIBUTION
    rn = random.lognormal(1.9, 0.9, numCircles)
    rn = map(None, rn)
    """

    print rn

    circles = positionCircles(rn)    
    plotCircles(circles)

