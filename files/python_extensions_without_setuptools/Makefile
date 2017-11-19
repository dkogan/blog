# This is a demo Makefile. The stuff on top pulls out the build flags from
# Python and tell Make to use them. The stuff on the bottom is generic build
# rules, that would come from a common build system.



# The python libraries (compiled ones and ones written in python all live in
# project/).

# I build the python extension module without any setuptools or anything.
# Instead I ask python about the build flags it likes, and build the DSO
# normally using those flags.
#
# There's some sillyness in Make I need to work around. First, I produce a
# python script to query the various build flags, but replacing all whitespace
# with __whitespace__. The string I get when running this script will then have
# a number of whitespace-separated tokens, each setting ONE variable
define PYVARS_SCRIPT
import sysconfig
import re
for v in ("CC","CFLAGS","CCSHARED","INCLUDEPY","BLDSHARED","LDFLAGS"):
    print re.sub("[\t ]+", "__whitespace__", "PY_{}:={}".format(v, sysconfig.get_config_var(v)))
endef
PYVARS := $(shell python -c '$(PYVARS_SCRIPT)')

# I then $(eval) these tokens one at a time, restoring the whitespace
$(foreach v,$(PYVARS),$(eval $(subst __whitespace__, ,$v)))

# The compilation flags are all the stuff python told us about. Some of its
# flags live inside its CC variable, so I pull those out. I also pull out the
# optimization flag, since I want THIS build system to control it
FLAGS_FROM_PYCC := $(wordlist 2,$(words $(PY_CC)),$(PY_CC))
c_library_pywrap.o: CFLAGS += $(filter-out -O%,$(FLAGS_FROM_PYCC) $(PY_CFLAGS) $(PY_CCSHARED) -I$(PY_INCLUDEPY))

# I add an RPATH to the python extension DSO so that it runs in-tree. The build
# system should pull it out at install time
project/c_library.so: c_library_pywrap.o libc_library.so
	$(PY_BLDSHARED) $(PY_LDFLAGS) $< -lc_library -o $@ -L$(abspath .) -Wl,-rpath=$(abspath .)

all: project/c_library.so
EXTRA_CLEAN += project/*.so



##########################################################################
##########################################################################
##########################################################################
# vanilla build-system stuff. Your own build system goes here!

LIB_OBJECTS  := c_library.o
ABI_VERSION  := 0
TAIL_VERSION := 0



# if no explicit optimization flags are given, optimize
define massageopts
$1 $(if $(filter -O%,$1),,-O3)
endef

%.o:%.c
	$(CC) $(call massageopts, $(CFLAGS) $(CPPFLAGS)) -c -o $@ $<

LIB_NAME           := libc_library
LIB_TARGET_SO_BARE := $(LIB_NAME).so
LIB_TARGET_SO_ABI  := $(LIB_TARGET_SO_BARE).$(ABI_VERSION)
LIB_TARGET_SO_FULL := $(LIB_TARGET_SO_ABI).$(TAIL_VERSION)
LIB_TARGET_SO_ALL  := $(LIB_TARGET_SO_BARE) $(LIB_TARGET_SO_ABI) $(LIB_TARGET_SO_FULL)

BIN_TARGETS := $(basename $(BIN_SOURCES))

CFLAGS += -std=gnu99

# all objects built for inclusion in shared libraries get -fPIC. We don't build
# static libraries, so this is 100% correct
$(LIB_OBJECTS): CFLAGS += -fPIC
$(LIB_TARGET_SO_FULL): LDFLAGS += -shared -Wl,--default-symver -fPIC -Wl,-soname,$(notdir $(LIB_TARGET_SO_BARE)).$(ABI_VERSION)

$(LIB_TARGET_SO_BARE) $(LIB_TARGET_SO_ABI): $(LIB_TARGET_SO_FULL)
	ln -fs $(notdir $(LIB_TARGET_SO_FULL)) $@

# Here instead of specifying $^, I do just the %.o parts and then the
# others. This is required to make the linker happy to see the dependent
# objects first and the dependency objects last. Same as for BIN_TARGETS
$(LIB_TARGET_SO_FULL): $(LIB_OBJECTS)
	$(CC) $(LDFLAGS) $(filter %.o, $^) $(filter-out %.o, $^) $(LDLIBS) -o $@

all: $(LIB_TARGET_SO_ALL)
.PHONY: all
.DEFAULT_GOAL := all


clean:
	rm -rf *.a *.o *.so *.so.* *.d $(EXTRA_CLEAN)


