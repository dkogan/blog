reset
set output "cree_characteristics.svg"
set terminal svg
set title "LED i-V curve (junction temperature = 25 degrees C) from datasheet"
set xlabel "V"
set ylabel "i (mA)"
set grid

f(x) = a + x*(b + x*c)

a=-1
b=1
c=0.1

fit f(x) "diode.dat" noerror via a,b,c

plot "diode.dat" with points notitle, f(x) notitle
