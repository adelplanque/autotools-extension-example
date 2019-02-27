#include <boost/python.hpp>
#include <ncurses.h>

namespace bp = boost::python;

void waouh(const char* msg) {
    int row, col;
    initscr();
    getmaxyx(stdscr, row, col); /* get the number of rows and columns */
    mvprintw(row / 2, (col - strlen(msg)) / 2, "%s", msg);
    refresh();
    getch();
    endwin();
}

BOOST_PYTHON_MODULE(waouh) {
    bp::def("waouh", &waouh);
}
