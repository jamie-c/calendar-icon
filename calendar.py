#!/usr/bin/env python3

import datetime
import subprocess
import pprint
import os


# --- LOCATION TO SAVE CALENDAR ICONS ---
# ---------------------------------------
calendar_save_folder = "/Pictures/app-icons/calendar"
# ---------------------------------------
# update the above path to the location where you want to save the calendar icons


day_number = datetime.datetime.today().day  # current day number as 2 digit integer
day_name = datetime.datetime.today().strftime("%a")  # current day name as 3 letter string
home_dir = os.path.expanduser("~")  # get current user's home directory
base_path = f"{home_dir}/{calendar_save_folder}/"  # base path for all files
svg_file_path = base_path + "calendar.svg"  # path to svg file
png_file_path = svg_file_path.replace(".svg", ".png")  # path to png file

# dictionary of day names and their relative x position in the svg 
# (used to center the day name on the day number)
day_position = {
    "Mon": -10,
    "Tue": 10,
    "Wed": -20,
    "Thu": -10,
    "Fri": 50,
    "Sat": 15,
    "Sun": -5,
}

# svg file contents
calendar_icon = f"""<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="800" height="800" viewBox="0 0 800 800" xml:space="preserve">
<desc>Created with Fabric.js 3.6.6</desc>
<defs></defs>
<g transform="matrix(1 0 0 1 399.69 398.69)">
    <g style="">
		<g transform="matrix(0.25 0 0 0.25 0.76 3.05)" id="rect830">
            <rect style="stroke: rgb(232,232,232); stroke-width: 22.6772; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(255,255,255); fill-rule: evenodd; opacity: 1;"  x="-1510.8351" y="-1510.8351" rx="586.14447" ry="586.14447" width="3021.6702" height="3021.6702" />
        </g>
	    <g transform="matrix(0.25 0 0 0.25 0.56 -256.97)" id="path967">
            <path style="stroke: none; stroke-width: 4; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(233,87,78); fill-rule: nonzero; opacity: 1;"  transform=" translate(141.92, 947.4)" d="m 781.87682 -1397.3636 c 323.12298 0 586.93278 253.5792 586.55598 589.27998 v 311.35956 H -1652.2814 V -880.3523 c 0 -236.8882 242.8187 -519.2938 566.7828 -517.7072 z" stroke-linecap="round" />
        </g>
	    <g transform="matrix(0.25 0 0 0.25 -2.97 116.76)" style="" id="text879">
		    <text xml:space="preserve" font-family="'Fira Sans Condensed'" font-size="1994.74" font-style="normal" font-weight="normal" style="stroke: none; stroke-width: 49.8683; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(90,90,90); fill-rule: nonzero; opacity: 1; white-space: pre;" >
                <tspan x="-1269.38" y="626.63" >{day_number}</tspan>
            </text>
        </g>
	    <g transform="matrix(0.25 0 0 0.24 {day_position[day_name]} -250.91)" style="" id="text931-5"  >
            <text xml:space="preserve" font-family="'Helvetica Neue'" font-size="694.258" font-style="normal" font-weight="normal" style="text-anchor: right; stroke: none; stroke-width: 2.08279; stroke-dasharray: none; stroke-linecap: butt; stroke-dashoffset: 0; stroke-linejoin: miter; stroke-miterlimit: 4; fill: rgb(252,252,252); fill-rule: nonzero; opacity: 1; white-space: pre;" >
                <tspan x="-649.67" y="218.09" >{day_name}</tspan>
            </text>
        </g>
    </g>
</g>
</svg>
"""

# list of sizes to convert png to
convert_to_file_sizes = ["16", "32", "48", "64", "128"]

# write contents of calendar_icon to calendar.svg using pprint
with open(svg_file_path, "w", encoding="utf-8") as f:
    f.write(calendar_icon)

# convert svg to png using imagemagick
try:
    subprocess.run(["convert", "-background", "none", svg_file_path, png_file_path], check=True)

    print("Successfully converted svg to png")

except subprocess.CalledProcessError as e:
    print(f"Failed to convert svg to png: {e}")

# use a generator statement to convert calendar.png to all the sizes from file_names
try:
    for size in convert_to_file_sizes:
        subprocess.run(["convert", png_file_path, "-resize", size, f"{base_path}calendar-{size}x{size}.png"], check=True)

    print("Successfully resized pngs!")

except subprocess.CalledProcessError as e:
    print(f"Failed to resize png: {e}")
