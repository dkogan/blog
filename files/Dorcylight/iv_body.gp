reset
set output "input_iv.svg"
set terminal svg
set title "Dorcy 41-4001 driver circuit characterization"
set xlabel "Input V"
set ylabel "Input i"
set grid

# from previous fit
a = 24.9834
b = -20.1936
c = 4.07537
id(vd) = a + b*vd + c*vd**2



# i = id(vd)
# i = (v - vd)/r
#
# -> a + b*vd + c*vd**2 = v/r - vd/r
# -> a + (b + 1/r)*vd + c*vd**2 = v/r
# -> c * vd**2 + (b + 1/r) * vd + a-v/r = 0
# -> vd = ( -(b + 1/r) + sqrt( (b + 1/r)**2 - 4*c * (a-v/r)) ) / (2*c)

vd(r,v) = ( -(b + 1/r) + sqrt( (b + 1/r)**2 - 4*c * (a-v/r)) ) / (2*c)

r=1
fit (x-vd(r,x))/r "iv_body.dat" noerror via r

plot "iv_body.dat" with points notitle, (x-vd(r,x))/r notitle
