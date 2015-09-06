TARGETS := \
	response_histogram.svg \
	perf_overview.png \
	perf_ftdi.svg \
	perf_zoom_success.svg \
	perf_zoom_failure.svg

SVG_TERM := 'svg noenhanced font ",10" size 1000,750'
PNG_TERM := 'png noenhanced font ",10" size 1000,750'

SHELL := /bin/zsh

all: $(TARGETS)




response_histogram.svg: intrackx.scap
	sysdig -t r -r $< fd.name contains isense.log or \
	  \( fd.name contains ttyUSB2 and \
	    \( \( evt.type = read and evt.dir = '<' and evt.rawres \!= 0\) or \
	       \( evt.type = write and evt.dir = '>' \) \) \) | \
	  perl -anE 'if(/write.*USB2/) { $$t0 = $$F[1]; } elsif(defined $$t0 && /read|isense.log/ ) { $$d = $$F[1] - $$t0; say $$d*1000; $$t0 = undef; }' | \
	  feedgnuplot --histo 0 --binwidth 0.1 --with boxes --set 'style fill solid border -1' \
		      --title "Histogram of /dev/ttyUSB2 reply times" --xlabel "Reply (ms)" -ylabel Count \
	              --hardcopy $@ --terminal $(SVG_TERM)

perf_overview.png: perf.plum.orig.fg
	< $< egrep -v ' sched|irq| cs\b| cpu\b' | \
	feedgnuplot --domain --dataid --with 'points ps 2' \
	            --hardcopy $@ --terminal $(PNG_TERM) \
	            --xlabel Cycle --ylabel 'Time (ms)' \
	            --ymin 0 --ymax 4

perf_ftdi.svg: perf.plum.orig.fg
	< $< egrep ftdi | \
	feedgnuplot --domain --dataid --autolegend --with 'points ps 2' \
	            --hardcopy $@ --terminal $(SVG_TERM) \
	            --xlabel Cycle --ylabel 'Time (ms)' \
	            --ymin 0 --ymax 4

perf_zoom_success.svg: perf.plum.orig.fg
	x=1; ymin=0.935; ymax=0.98; \
	< $< \
	awk "!/^#/ && \$$1 >= $$x && \$$1 < $$(($$x+1)) && \$$3 >= $$ymin && \$$3 <= $$ymax { if(\$$2 == \"cpu\") { cpu = \$$4; print cpu,id,y } else { id=\$$2; y=\$$3} } " | \
	feedgnuplot --domain --dataid --autolegend --with 'points ps 2' \
	            --hardcopy $@ --terminal $(SVG_TERM) \
	            --xlabel CPU --ylabel 'Time (ms)' \
	            --set 'xtics 0,1,4' \
	            --xmin -0.1 --xmax 4.1 --ymin $$ymin --ymax $$ymax

perf_zoom_failure.svg: perf.plum.orig.fg
	x=11; ymin=1.07; ymax=1.12; \
	< $< \
	awk "!/^#/ && \$$1 >= $$x && \$$1 < $$(($$x+1)) && \$$3 >= $$ymin && \$$3 <= $$ymax { if(\$$2 == \"cpu\") { cpu = \$$4; print cpu,id,y } else { id=\$$2; y=\$$3} } " | \
	feedgnuplot --domain --dataid --autolegend --with 'points ps 2' \
	            --hardcopy $@ --terminal $(SVG_TERM) \
	            --xlabel CPU --ylabel 'Time (ms)' \
	            --set 'xtics 0,1,4' \
	            --xmin -0.1 --xmax 4.1 --ymin $$ymin --ymax $$ymax



clean:
	rm -rf $(TARGETS)
.PHONY: clean
