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
        include_dirs=['@BOOST_CPPFLAGS@'],
        library_dirs=['@BOOST_LDFLAGS@'],
        libraries=['@BOOST_PYTHON_LIB@', '@CURSES_LIBS@', '@CURSES_LIB@']
    )],
    configure_ac="""
        dnl Check for python
        AX_PYTHON_DEVEL

        dnl Boost
        AX_BOOST_BASE([1.41], [],
            AC_MSG_ERROR([Needs Boost but it was not found in your system])
        )

        dnl Boost Python
        AX_BOOST_PYTHON
        if test "x$ac_cv_boost_python" != "xyes" -o "x$BOOST_PYTHON_LIB" == "x"; then
            AC_MSG_ERROR([Boost Python needed])
        fi

        dnl ncurses
        AX_WITH_CURSES
        if test "x$ax_cv_ncursesw" != "xyes" -a test "x$ax_cv_ncurses" != "xyes"; then
            AC_MSG_ERROR([requires either NcursesW or Ncurses library])
        fi
    """,
    configure_options = [
        ('with-boost=', None, "Boost install prefix"),
        ('with-curses=', None, "NCurses install prefix"),
    ],
    setup_requires=['autotools-extension']
)
