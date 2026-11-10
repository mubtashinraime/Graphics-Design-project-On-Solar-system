import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# -----------------------------
# Planet Angles
# -----------------------------
mercury_angle = 0
venus_angle = 0
earth_angle = 0
moon_angle = 0
mars_angle = 0
jupiter_angle = 0
saturn_angle = 0

# -----------------------------
# Stars (Reduced)
# -----------------------------
stars = []

for _ in range(100):
    stars.append(
        (
            random.randint(-400, 400),
            random.randint(-400, 400)
        )
    )

# -----------------------------
# Draw Circle
# -----------------------------
def draw_circle(radius):

    glBegin(GL_POLYGON)

    for i in range(100):

        angle = 2 * math.pi * i / 100

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        glVertex2f(x, y)

    glEnd()

# -----------------------------
# Draw Orbit
# -----------------------------
def draw_orbit(radius):

    glColor3f(0.25, 0.25, 0.25)

    glBegin(GL_LINE_LOOP)

    for i in range(100):

        angle = 2 * math.pi * i / 100

        glVertex2f(
            radius * math.cos(angle),
            radius * math.sin(angle)
        )

    glEnd()

# -----------------------------
# Draw Text
# -----------------------------
def draw_text(x, y, text):

    glColor3f(1, 1, 1)

    glRasterPos2f(x, y)

    for ch in text:
        glutBitmapCharacter(
            GLUT_BITMAP_HELVETICA_12,
            ord(ch)
        )

# -----------------------------
# Draw Stars
# -----------------------------
def draw_stars():

    glPointSize(2)

    glColor3f(1, 1, 1)

    glBegin(GL_POINTS)

    for x, y in stars:
        glVertex2f(x, y)

    glEnd()

# -----------------------------
# Display Function
# -----------------------------
def display():

    global moon_angle

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_stars()

    # Sun
    glColor3f(1.0, 1.0, 0.0)

    glPushMatrix()
    draw_circle(25)
    glPopMatrix()

    draw_text(-10, -40, "Sun")

    # Orbits
    draw_orbit(50)
    draw_orbit(80)
    draw_orbit(120)
    draw_orbit(170)
    draw_orbit(230)
    draw_orbit(300)

    # Mercury
    mercury_x = 50 * math.cos(math.radians(mercury_angle))
    mercury_y = 50 * math.sin(math.radians(mercury_angle))

    glPushMatrix()
    glTranslatef(mercury_x, mercury_y, 0)

    glColor3f(0.7, 0.7, 0.7)
    draw_circle(4)

    glPopMatrix()

    draw_text(mercury_x + 8, mercury_y, "Mercury")

    # Venus
    venus_x = 80 * math.cos(math.radians(venus_angle))
    venus_y = 80 * math.sin(math.radians(venus_angle))

    glPushMatrix()
    glTranslatef(venus_x, venus_y, 0)

    glColor3f(1.0, 0.6, 0.2)
    draw_circle(6)

    glPopMatrix()

    draw_text(venus_x + 8, venus_y, "Venus")

    # Earth
    earth_x = 120 * math.cos(math.radians(earth_angle))
    earth_y = 120 * math.sin(math.radians(earth_angle))

    glPushMatrix()
    glTranslatef(earth_x, earth_y, 0)

    glColor3f(0.1, 0.4, 1.0)
    draw_circle(8)

    # Moon Orbit
    glColor3f(0.6, 0.6, 0.6)

    glBegin(GL_LINE_LOOP)

    for i in range(100):

        a = 2 * math.pi * i / 100

        glVertex2f(
            20 * math.cos(a),
            20 * math.sin(a)
        )

    glEnd()

    # Moon
    moon_x = 20 * math.cos(math.radians(moon_angle))
    moon_y = 20 * math.sin(math.radians(moon_angle))

    glPushMatrix()

    glTranslatef(moon_x, moon_y, 0)

    glColor3f(0.9, 0.9, 0.9)
    draw_circle(3)

    glPopMatrix()

    glPopMatrix()

    draw_text(earth_x + 10, earth_y, "Earth")

    # Mars
    mars_x = 170 * math.cos(math.radians(mars_angle))
    mars_y = 170 * math.sin(math.radians(mars_angle))

    glPushMatrix()
    glTranslatef(mars_x, mars_y, 0)

    glColor3f(1.0, 0.2, 0.2)
    draw_circle(6)

    glPopMatrix()

    draw_text(mars_x + 10, mars_y, "Mars")

    # Jupiter
    jupiter_x = 230 * math.cos(math.radians(jupiter_angle))
    jupiter_y = 230 * math.sin(math.radians(jupiter_angle))

    glPushMatrix()
    glTranslatef(jupiter_x, jupiter_y, 0)

    glColor3f(0.8, 0.5, 0.3)
    draw_circle(12)

    glPopMatrix()

    draw_text(jupiter_x + 12, jupiter_y, "Jupiter")

    # Saturn
    saturn_x = 300 * math.cos(math.radians(saturn_angle))
    saturn_y = 300 * math.sin(math.radians(saturn_angle))

    glPushMatrix()
    glTranslatef(saturn_x, saturn_y, 0)

    glColor3f(0.93, 0.85, 0.55)
    draw_circle(10)

    # Saturn Ring
    glColor3f(0.75, 0.75, 0.65)

    glBegin(GL_LINE_LOOP)

    for i in range(100):

        a = 2 * math.pi * i / 100

        glVertex2f(
            18 * math.cos(a),
            12 * math.sin(a)
        )

    glEnd()

    glPopMatrix()

    draw_text(saturn_x + 12, saturn_y, "Saturn")

    glutSwapBuffers()

# -----------------------------
# Update Animation
# -----------------------------
def update(value):

    global mercury_angle
    global venus_angle
    global earth_angle
    global moon_angle
    global mars_angle
    global jupiter_angle
    global saturn_angle

    mercury_angle += 1.2
    venus_angle += 0.9

    earth_angle += 0.7
    moon_angle += 2.5

    mars_angle += 0.5

    jupiter_angle += 0.25

    saturn_angle += 0.15

    glutPostRedisplay()

    glutTimerFunc(25, update, 0)

# -----------------------------
# Initialization
# -----------------------------
def init():

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluOrtho2D(
        -400,
        400,
        -400,
        400
    )

    glMatrixMode(GL_MODELVIEW)

# -----------------------------
# Main Program
# -----------------------------
glutInit()

glutInitDisplayMode(
    GLUT_DOUBLE | GLUT_RGB
)

glutInitWindowSize(900, 900)

glutCreateWindow(
    b"Realistic Solar System Animation"
)

init()

glutDisplayFunc(display)

glutTimerFunc(
    25,
    update,
    0
)

glutMainLoop()