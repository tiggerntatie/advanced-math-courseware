advanced-math-courseware
========================

Build environment setup.

You will need LaTex installed for epub (use the following command
on Linux - may take more work in a Mac system):

    sudo apt-get install texlive-latex-base texlive-latex-extra dvipng

Create virtualenv directory (any name will do) then
an folder within that called sphinx (though any 
name will do for that too).

Activate the virtualenv by typing

    source bin/activate

Then install the dependencies:

    pip install -r sphinx/requirements.txt


