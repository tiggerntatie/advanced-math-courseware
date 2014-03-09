Quadratic Functions
===================

Part A: Quadratic Forms and Graphing
------------------------------------

.. topic:: Definition of a Quadratic Function (Standard Form)

    .. math::
    
        f(x)=a x^2 + bx + c, a \ne 0
        
    The :math:`a \ne 0` bit is just a slick way of saying that :math:`f(x)=bx+c` 
    is *not* considered a quadratic function!
    
Simple Quadratic Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~

You have already seen transformations of the **ultra-simple quadratic 
function**: :math:`f(x)=x^2`

Example: *Write a definition of* :math:`g(x)` *as a transformation of* 
:math:`f(x)=x^2` *by shifting its vertex to (-2, 3) and stretching it vertically
by a factor of* :math:`\frac 1 2`. *Also write in terms of x:*

.. math::

    g(x) &= \frac 1 2 f(x+2)+3  ~~~~\text{as a transformation of f(x)}\\
    g(x) &= \frac 1 2 (x + 2)^2 + 3 ~~~~ \text{in terms of x only}
    
You can expand the transformed function to write it in *standard form*. First,
expand by distributing the (x+2) with itself (FOIL):

.. math::
    
    g(x)&= \frac 1 2 (x^2 + 4x +4)+3 ~~~~ \text{(then simplify)} \\
    g(x)&= \frac 1 2 x^2 + 2x + 5
    
.. topic:: Quadratic Function in Vertex Form

    When you write a quadratic function as a transformation of :math:`f(x)=x^2`:
    
    .. math::
        
        f(x)=a(x-h)^2 + k, ~~~~ a \ne 0
    
    it is known as a quadratic in **vertex form**, because its graph is a 
    parabola with vertex at (h, k).
    
.. note::

    **All quadratic functions are just transformations of** :math:`f(x)=x^2` **!**

Examples
~~~~~~~~

*Work these additional examples in your notebook or on a separate sheet of
paper.*

.. include:: examples/A.1p.rst

1. .. include:: examples/A.1q.rst
2. .. include:: examples/A.2q.rst
3. .. include:: examples/A.3q.rst
4. .. include:: examples/A.4q.rst

Solutions: :doc:`1<examples/A.1s>`, :doc:`2<examples/A.2s>`, :doc:`3<examples/A.3s>`,
:doc:`4<examples/A.4s>`


Converting Standard Form to Vertex Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you start with a quadratic function written in standard form, converting 
to vertex form takes a little more work. For example:

.. math::

    f(x)&= 2x^2-12x+3 ~~~~ \text{starting with this quadratic in standard form}\\
    f(x)&= 2(x^2-6x)+3 ~~~~ \text{factor from the first two terms if you can}\\
    f(x)&= 2(x^2-6x+?)+3-? ~~~~ \text{prepare to rewrite } ~ x^2-6x ~ \text{ as part of a perfect square }\\
    f(x)&= 2(x^2-6x+9)+3-18

Notice how we had to add and subtract 18 to keep the function the same?

Now rewrite :math:`x^2-6x+9` as :math:`(x-3)^2` and simplify a bit: 
:math:`f(x)=2(x-3)^2-15`

.. note:: 

    **You learned something like this in Algebra, called "completing the square"!**
    
Examples
~~~~~~~~

*Work these additional examples in your notebook or on a separate sheet of
paper.*

.. include:: examples/A.5p.rst

5. .. include:: examples/A.5q.rst
6. .. include:: examples/A.6q.rst
7. .. include:: examples/A.7q.rst

Solutions: :doc:`5<examples/A.5s>`, :doc:`6<examples/A.6s>`, :doc:`7<examples/A.7s>`


Some Tips for Graphing Quadratics: Standard Form vs. Vertex Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=====================       ===============================      ===============================
To find the...              :math:`a x^2 + b x + c`              :math:`f(x)=a(x-h)^2+k`
=====================       ===============================      ===============================
Vertex x coordinate         :math:`\frac {-b}{2a}`               :math:`h`
Vertex y coordinate         :math:`f(\frac{-b}{2a})`             :math:`k`
Axis of symmetry            :math:`x=\frac{-b}{2a}`              :math:`x=a`
y intercept                 :math:`f(0)=c`                       :math:`f(0)=ah^2+k`
x intercept(s)              set :math:`f(x)=0`, solve for x      set :math:`f(x)=0`, solve for x
=====================       ===============================      ===============================

General process for graphing:

*   Locate the vertex.
*   The leading coefficient "a" is the "stretch" factor: provides 2 to 4 points
    close to the vertex.
*   Locate the y intercept and a point on the opposite side of the axis of 
    symmetry (optional, if in standard form).

Examples
~~~~~~~~

*Work these additional examples in your notebook or on a separate sheet of
paper.*

.. include:: examples/A.8p.rst

8. .. include:: examples/A.8q.rst
9. .. include:: examples/A.9q.rst

Answers: :doc:`8<examples/A.8s>`, :doc:`9<examples/A.9s>`

Part B: Solving Quadratic Functions (with some more graphing, too!)
-------------------------------------------------------------------

.. topic:: Solving Quadratics

    "Solving" a quadratic function means finding the value(s) of x that make
    the function equal to zero. That is: find any value(s) of x such that: 
    :math:`f(x)=0=ax^2+bx+c`. Any value(s) of x that do this are called 
    **zeros** of the function.
   
Examples
~~~~~~~~

*Work these examples in your notebook*

.. include:: examples/B.1p.rst

1. .. include:: examples/B.1q.rst
2. .. include:: examples/B.2q.rst

Answers: :doc:`1<examples/B.1s>`, :doc:`2<examples/B.2s>`

Solving Quadratics by Factoring from Standard Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the quadratic is in standard form, you may be able to factor it to find
the zeros. The **function will be zero when either factor is zero**:

.. topic:: Example

    *Use factoring to solve*: :math:`h(x)=x^2-2x-3`
    
    .. math::
    
        &\text{Factor:}~~x^2-2x-3\\
        &x^2-2x-3 = (x-3)(x+1)\\
        &\text{Find values of x that make factors = zero}\\
        &x-3=0 \text{, so } x=3\\
        &x+1=0 \text{, so } x = -1 ~~~\text{so zeros of h(x) are 3 and -1}
        
Examples
~~~~~~~~

.. include:: examples/B.3p.rst

3. .. include:: examples/B.3q.rst
4. .. include:: examples/B.4q.rst
5. .. include:: examples/B.5q.rst
6. .. include:: examples/B.6q.rst

Answers: :doc:`3<examples/B.3s>`, :doc:`4<examples/B.4s>`, 
:doc:`5<examples/B.5s>`, :doc:`6<examples/B.6s>`

Solving Quadratics in Vertex Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If the quadratic is in vertex form, then you can use garden variety algebra
to solve it.

.. topic:: Example

    *Use algebra to solve*: :math:`r(x)=2(x+4)^2-3`
    
    Prepare to solve by setting equal to zero: :math:`2(x+4)^2-3 = 0`
    
    .. math::
    
        2(x+4)^2 &= 3\\
        (x+4)^2 &= \frac 3 2\\
        x+4 &= \pm \sqrt \frac 3 2 ~~ \text{don't forget the}\pm\\
        x &= -4 \pm \sqrt \frac 3 2\\
        
    So zeros of :math:`r(x)` are :math:`-4+\sqrt \frac 3 2 ~\text{and} ~ -4-\sqrt\frac 3 2`
    
Examples
~~~~~~~~

.. include:: examples/B.7p.rst

7. .. include:: examples/B.7q.rst
8. .. include:: examples/B.8q.rst

Answers: :doc:`7<examples/B.7s>`, :doc:`8<examples/B.8s>`

Solving Quadratics in Standard Form, Take 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If a quadratic in standard form doesn't succumb to factoring, you can always
convert to vertex form then use algebra to solve it. Use the "completing the 
square" method from yesterday, or find the vertex and rewrite in vertex form.

.. topic:: Example

    *Solve by converting to vertex form first*: :math:`s(x)=x^2-2x-1`
    
    Find the axis of symmetry (x coord of vertex) of :math:`x^2-2x-1`:
    
    .. math::
    
        &x_{vertex} = \frac {-b}{2a} = \frac {-(-2)}{2(1)} = \frac 2 2 = 1 \\
        &y_{vertex} = s(x_{vertex}) = s(1) = 1^2-2(1)-1=1-2-1=-2 \\
        &\text{Write in vertex form: }s(x)=(x-1)^2-2 \text{ (make sure you keep "a" from the original quadratic)} \\
        &\text{Set }s(x)=0 \text{ to solve: } (x-1)^2-2=0 \\
        &(x-1)^2=2 \\
        &x-1=\pm \sqrt2 \\
        &x=1 \pm\sqrt 2 \text{, so zeros of } s(x) \text{ are } 1 + \sqrt 2 \text{ and } 1 - \sqrt 2

Examples
~~~~~~~~

.. include:: examples/B.9p.rst

9. .. include:: examples/B.9q.rst
10. .. include:: examples/B.10q.rst

Answers: :doc:`9<examples/B.9s>`, :doc:`10<examples/B.10s>`

.. include:: examples/B.11p.rst

11. .. include:: examples/B.11q.rst
12. .. include:: examples/B.12q.rst

Answers: :doc:`11<examples/B.11s>`, :doc:`12<examples/B.12s>`


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

Practice Examples (Homework)
----------------------------

Part A
~~~~~~

1. .. include:: practice/A.1q.rst
2. .. include:: practice/A.2q.rst
3. .. include:: practice/A.3q.rst
4. .. include:: practice/A.4q.rst
5. .. include:: practice/A.5q.rst

-----------------------------------

In Algebra you saw how completing the square can lead to a generic formula for
solving quadratics called:

.. topic:: The Quadratic Formula(s)

    The zeros of the function :math:`f(x)=ax^2+bx+c` are given by:
    :math:`\frac {-b \pm \sqrt{b^2-4ac}}{2a} ~~~(a \ne 0)`

Part B
~~~~~~

For the next two questions, solve using any technique. Use factoring and
completing the square at least once.

6. .. include:: practice/B.1q.rst

.. include:: practice/B.2p.rst

7. .. include:: practice/B.2q.rst
8. .. include:: practice/B.3q.rst
9. .. include:: practice/B.4q.rst
10. .. include:: practice/B.5q.rst



