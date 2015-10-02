set output "both.noscrollbar.svg"
set terminal svg

set grid
set xlabel "Time (s)"
set ylabel "Memory usage (kB)"

plot "memory.before.noscrollbar.log" using 0:($1 - 28480) with lines title "Before patch", \
     "memory.after.noscrollbar.log"  using 0:($1 - 26120) with lines title "After patch"
