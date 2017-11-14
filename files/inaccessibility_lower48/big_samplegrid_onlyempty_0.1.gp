# Generated by osmgnuplot.pl from
#   https://github.com/dkogan/osmgnuplot
#
# Command used:
#   osmgnuplot.pl --zoom 4 --center 40,-96 --rad 1600miles



# Note that this script plots data on top of an image. The color scaling logic
# that applies to such plots was changed (for the better) in gnuplot very
# recently, and this script would only produce the expected output on very
# recent builds of gnuplot. See
# https://sourceforge.net/p/gnuplot/mailman/message/35996823/


set autoscale noextend

lat_offset_px = 1114
lon_offset_px = 612

s1_cos(x)     = (sin(x)+1)/cos(x)
inv_s1_cos(x) = asin( (x**2 - 1)/(x**2 + 1) )

px_to_lon(x) = (x + lon_offset_px)/(256. * 2.**4)*360. - 180.
lon_to_px(x) = (x+180.)/360. * 2.**4 * 256 - lon_offset_px

px_to_lat(x) = inv_s1_cos(exp((1 - (x + lat_offset_px)/(2.**4 * 256) *2)*pi))*180./pi
lat_to_px(x) = (1 - log( (sin(x*pi/180) + 1.)/cos(x*pi/180) )/pi)/2. * 2.**4 * 256 - lat_offset_px


set link x2 via px_to_lon(x) inverse lon_to_px(x)
set link y2 via px_to_lat(y) inverse lat_to_px(y)

set xrange [12:688]
set y2range [25:50]

unset xtics
unset ytics

set grid front
set x2tics mirror 4.99999999999997
set y2tics mirror 4.99999999999997

set size ratio -1

set x2label "Longitude (degrees)"
set y2label "Latitude (degrees)"
set title "Cells that contain no roads"


set terminal png enhanced size 800,510
set output "big_samplegrid_onlyempty_0.1.png"

plot \
     "montage_40_-96_1600miles_4.png" binary filetype=png flipy using 1:2:3 with rgbimage notitle axis x1y1, \
     "< awk '!$3' samples_0.1.dat" using 2:1 with points pt 2 ps 0.3 notitle axis x2y2