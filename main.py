#!/usr/bin/env python3

import gi
import os
import subprocess

from thumbnail import create_thumbnail

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

WALLPAPER_DIR = os.path.expanduser(
    "~/Pictures/Wallpapers/animated"
)


class HyprWall(Gtk.Application):

    def __init__(self):
        super().__init__(application_id="com.hypr.wall")

    def do_activate(self):

        win = Gtk.ApplicationWindow(application=self)
        win.set_title("HyprWall")
        win.set_default_size(1000, 700)

        scroll = Gtk.ScrolledWindow()

        flow = Gtk.FlowBox()
        flow.set_max_children_per_line(4)
        flow.set_selection_mode(Gtk.SelectionMode.NONE)
        flow.set_row_spacing(12)
        flow.set_column_spacing(12)

        scroll.set_child(flow)

        for file in sorted(os.listdir(WALLPAPER_DIR)):

            if not file.lower().endswith((".mp4", ".webm", ".mkv")):
                continue

            path = os.path.join(WALLPAPER_DIR, file)

            thumb = create_thumbnail(path)

            image = Gtk.Image.new_from_file(thumb)
            image.set_pixel_size(220)

            label = Gtk.Label(label=file)
            label.set_wrap(True)
            label.set_max_width_chars(25)

            box = Gtk.Box(
                orientation=Gtk.Orientation.VERTICAL,
                spacing=8
            )

            box.append(image)
            box.append(label)

            button = Gtk.Button()
            button.set_child(box)

            button.connect(
                "clicked",
                self.apply_wallpaper,
                path
            )

            flow.append(button)

        win.set_child(scroll)
        win.present()

    def apply_wallpaper(self, button, path):

        subprocess.Popen([
            os.path.expanduser(
                "~/Projects/HyprWall/apply.sh"
            ),
            path
        ])


app = HyprWall()
app.run()
