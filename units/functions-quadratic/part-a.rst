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


