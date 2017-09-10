# ScreenPDF

ScreenPDF is a library for easy screenplay generation under Python,
using PyFPDF as base (see [PyFPDF][1] \[1]).  
ScreenPDF uses [Moreno's how to write a screenplay][2] \[2] as reference
for proper screenplay format.

## How to use

### Installing ScreenPDF

    $ git clone https://github.com/arthurazs/ScreenPDF.git
    $ cd ScreenPDF
    $ pip install -e .

### Running ScreenPDF

    $ screenpdf -h
    $ screenpdf losing-space.spdf
    $ evince Losing\ Space.pdf

You can write your own script following the `losing-space.spdf` syntax.

## References

\[1] Reingart, M. (2013). pyfpdf: FPDF for Python [online] Available at: 
<https://github.com/reingart/pyfpdf> [Accessed 25 Sep. 2016].  
\[2] Moreno, M.; Tuxford, K. (2010). How to Write a
Screenplay: Script Writing Example & Screenwriting Tips [online]
Available at:
<https://www.writersstore.com/how-to-write-a-screenplay-a-guide-to-scriptwriting/>
[Accessed 25 Sep. 2016].

[1]: https://github.com/reingart/pyfpdf
[2]: https://www.writersstore.com/how-to-write-a-screenplay-a-guide-to-scriptwriting/
