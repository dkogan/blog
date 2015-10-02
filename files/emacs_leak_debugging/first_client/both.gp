set output "both.svg"
set terminal svg

set grid
set xlabel "Time (s)"
set ylabel "Memory usage (kB)"

plot "memory.before.log" using 0:($1 - 41984) with lines title "Before patch", \
     "memory.after.log"  using 0:($1 - 27200) with lines title "After patch"
