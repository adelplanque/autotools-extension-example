from setuptools import setup, Extension

from autotools_extension.autoconf import Distribution

setup(
    distclass=Distribution,
    name='waouh',
    version='0.1',
    description='My beautiful extension',
    packages=['waouh'],
    ext_modules=[Extension(
        'waouh',
        sources=['waouh/waouh.cpp'],
        libraries=['@BOOST_PYTHON_LIB@', '@CURSES_LIBS@', '@CURSES_LIB@']
    )],
    configure_ac="""
        AC_PREREQ([2.63])
        AC_INIT([waouh], [1.0.0])
        AM_INIT_AUTOMAKE([foreign -Wall -Werror])

        dnl Boost
        AX_BOOST_BASE([1.41], [],
            AC_MSG_ERROR([Needs Boost but it was not found in your system])
        )

        dnl Boost Python
        AX_BOOST_PYTHON
        if test "$ac_cv_boost_python" != "yes"; then
            AC_MSG_ERROR([Boost Python needed])
        fi

        dnl ncurses
        AX_WITH_CURSES
        if test "x$ax_cv_ncursesw" != xyes && test "x$ax_cv_ncurses" != xyes; then
            AC_MSG_ERROR([requires either NcursesW or Ncurses library])
        fi

        AC_CONFIG_FILES([Makefile])
        AC_OUTPUT
    """,
    configure_options = [
        ('with-boost=', None, "Boost install prefix"),
        ('with-curses=', None, "NCurses install prefix"),
    ],
    setup_requires=['autotools-extension']
)
