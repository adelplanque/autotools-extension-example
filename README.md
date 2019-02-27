Example of using `autotools-extension` to configure build process.

* First install `autotools-extension`:
  https://github.com/adelplanque/autotools-extension

* Then run:

    python setup.py develop --user

Build process will start with a configure step.

You can see the link command used by `distutil`:

    x86_64-linux-gnu-g++ -pthread -shared -Wl,-O1 -Wl,-Bsymbolic-functions
        -Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,-Bsymbolic-functions
        -Wl,-z,relro -g -fstack-protector-strong -Wformat -Werror=format-security
        -Wdate-time -D_FORTIFY_SOURCE=2 build/temp.linux-x86_64-3.6/waouh/waouh.o
        -lboost_python3-py36 -lncursesw -ltinfo
        -o build/lib.linux-x86_64-3.6/waouh.cpython-36m-x86_64-linux-gnu.so

* `@BOOST_PYTHON_LIB@` has been subtitute by `boost_python3-py36`
* `@CURSES_LIBS@` has been subtitute by `ncursesw` and `ltinfo`

Then

    python -c 'import waouh; waouh.waouh("Hello world")'

will print a beautiful "Hello world".

After creating a source distribution, `autoconf` is no longer useful: the `configure` script is embedded in the sources.
