"""

*   raylib [core] example - Windows drop files
*
*   This example only works on platforms that support drag & drop (Windows, Linux, OSX, Html5?)
*
*   This example has been created using raylib 1.3 (www.raylib.com)
*   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
*
*   Copyright (c) 2015 Ramon Santamaria (@raysan5)

"""
import pyray
from raylib.colors import (
    RAYWHITE,
    DARKGRAY,
    LIGHTGRAY,
    GRAY
)

screenWidth = 800
screenHeight = 450

pyray.init_window(screenWidth, screenHeight,
                  'raylib [core] example - drop files')
pyray.set_target_fps(60)  # Set our game to run at 60 frames-per-second

droppedFiles = []

def get_dropped_files():
    count_pointer = pyray.ffi.new("int *", 0)
    droppedFiles_pointer = pyray.get_dropped_files(count_pointer)
    d = []
    for i in range(0, count_pointer[0]):
        d.append(pyray.ffi.string(droppedFiles_pointer[i]).decode('utf-8'))
    return d


while not pyray.window_should_close():

    if pyray.is_file_dropped():
        droppedFiles = get_dropped_files()

    pyray.begin_drawing()

    pyray.clear_background(RAYWHITE)

    if len(droppedFiles) == 0:
        pyray.draw_text("Drop your files to this window!", 100, 40, 20, DARKGRAY)
    else:
        pyray.draw_text("Dropped files:", 100, 40, 20, DARKGRAY);

    for i in range(0, len(droppedFiles)):
        if i % 2 == 0:
            pyray.draw_rectangle(0, 85 + 40*i, screenWidth, 40, pyray.fade(LIGHTGRAY, 0.5))
        else:
            pyray.draw_rectangle(0, 85 + 40*i, screenWidth, 40, pyray.fade(LIGHTGRAY, 0.3))
        pyray.draw_text(droppedFiles[i], 120, 100 + 40*i, 10, GRAY)

    pyray.draw_text("Drop new files...", 100, 110 + 40*len(droppedFiles), 20, DARKGRAY);
    pyray.end_drawing()

# De-Initialization
pyray.clear_dropped_files()
pyray.close_window()  # Close window and OpenGL context
