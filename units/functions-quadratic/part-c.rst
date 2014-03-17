Part C: Imagine the Unimaginable
--------------------------------

Warmup
~~~~~~

.. include:: examples/C.1p.rst

1. .. include:: examples/C.1q.rst
2. .. include:: examples/C.2q.rst
3. .. include:: examples/C.3q.rst
4. .. include:: examples/C.4q.rst

Answers: :doc:`1<examples/C.1s>`, :doc:`2<examples/C.2s>`, 
:doc:`3<examples/C.3s>`, :doc:`4<examples/C.4s>`

If you said **NO** to the last question then **congratulations**: you did a 
great job of interpreting the graphs.

But.. just for fun, let's see what happens if we try solving for the zeros 
of f(x) using the techniques from yesterday:

.. math:: 

    f(x)&=(x+2)^2+1\\
    (x+2)^2+1&=0~~~\text{Set f(x) equal to zero}\\
    (x+2)^2&=-1\\
    (x+2)&=\pm\sqrt{-1}\\
    x&=-2\pm\sqrt{-1}
    
    
So the zeros of :math:`f(x)` are :math:`-2+\sqrt{-1}` and :math:`-2-\sqrt{-1}`
    
Everyone knows that **no real number is the square root of negative one**, but
let's just see what would happen if we plugged one of those zeros back in for x:

.. math::
    
    f(-2+\sqrt{-1})&=(-2+\sqrt{-1} + 2)^2+1\\
    {}&=(\sqrt{-1})^2+1
 
Since a square root, squared, is equal to whatever is inside:

.. math::

    {}&=-1+1\\
    {}&=0 ~~~ \text{IT WORKS!}
    
.. note:: 

    **The fact that we can't "figure out" what** :math:`\sqrt{-1}` 
    **means doesn't stop us from using it!**

The abbreviation for :math:`\sqrt{-1}` is the imaginary unit, *i*. You can 
use *i* in your math just like any other symbol, but if you ever find 
yourself with the square of *i*, then use the fact: :math:`i^2=-1`.

So, from the example on the previous page, the zeors of :math:`f(x)` are: 
:math:`-2+i` and :math:`-2-i`. These are "imaginary" zeros. The set of all
real and all imaginary numbers is the complex number system.

Examples
~~~~~~~~

.. include:: examples/C.5p.rst

5. .. include:: examples/C.5q.rst
6. .. include:: examples/C.6q.rst

Answers: :doc:`5<examples/C.5s>`, :doc:`6<examples/C.6s>`

.. topic:: What's in a name: why are they called "imaginary"?

    Imaginary numbers are no less "real" than real numbers. They are just
    the next step in a progression of **useful** abstractions:
    
    * "What would happen if we used a number to represent *nothing*?"
    * "What would happen if we used numbers that represent 
      *less than nothing*?"
    * "What would happen if we used numbers that represent *a fraction 
      of a whole number*?"
    * "What would happen if we used numbers that *are not whole or 
      a fraction of a whole number*?"
    * And now: "What would happen if we used numbers that have
      *negative squares*?"
      
    No, you will *not* use imaginary numbers to build a birdhouse or file
    your taxes. You **will** use imaginary numbers in **future math studies**,
    and if you decide to enter fields in which they have been found 
    especially **useful**, such as physics, electrical engineering, mechanical
    engineering, and more.
    
.. topic:: Rules for doing math with complex numbers
 
    * **Adding and Subtracting**: Add and subtract like parts.
    * **Multiplying**: Distribute each term.
    * **Dividing**: Division is when you have a fraction with an imaginary number
      in the denominator. Multiply the numerator and denominator by the 
      **complex conjugate** of the denominator.
      
.. topic:: Example
 
    Evaluate: :math:`(3+2i)\cdot(4-i)`
    
    .. math::
        
        (3+2i)\cdot(4-i) &= 3 \cdot 4 + 3 \cdot {-i} + 2i \cdot 4 + 2i \cdot {-i} \\
        &=12-3i+8i-2i^2~~~~    \text{Notice the last term!!!}\\
        &=12+5i-2\cdot(-1)~~~~ \text{Because }i^2=-1\\
        &=12+5i+2=14+5i~~~~    \text{Your final answer will be in a+bi form}

.. topic:: Example

    Evaluate: :math:`\frac {(3+2i)} {(4-i)}`
    
    The complex conjugate of the denominator is :math:`4+i`
    
    .. math::
    
        \frac {(3+2i)} {(4-i)} = \frac {(3+2i)} {(4-i)} \cdot \frac {(4+i)} {(4+i)}
        = \frac {12+3i+8i+2i^2}{16+4i-4i-i^2} = \frac {12+11i-2^*}{16+1^*}
        = \frac {10+11i}{17} = \frac {10} {17}+ \frac {11} {17} i
        
    \* Don't forget: :math:`i^2=-1`!!


Examples
~~~~~~~~

.. include:: examples/C.7p.rst

7. .. include:: examples/C.7q.rst
8. .. include:: examples/C.8q.rst
9. .. include:: examples/C.9q.rst
10. .. include:: examples/C.10q.rst

Answers: :doc:`7<examples/C.7s>`, :doc:`8<examples/C.8s>`,
:doc:`9<examples/C.9s>`, :doc:`10<examples/C.10s>`
