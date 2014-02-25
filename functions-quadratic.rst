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

1. Write a definition of :math:`h(x)` as a transformation of :math:`f(x)=x^2`
   by shifting its vertex to (1, 2) and stretching it vertically by a factor
   of -2 (i.e. ":math:`h(x)=...`").   
2. Write :math:`h(x)` from (1) in terms of x only.
3. Sketch the graph of :math:`h(x)` (remember: a transformation of :math:`x^2`).
4. Write :math:`h(x)` from (2) in standard form (think: FOIL).

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

Convert these standard form quadratic functions to vertex form by completing
the square:

5. :math:`f(x)=x^2-2x-2`
6. :math:`c(x)=3x^2+30x+70`
7. What happens to the leading coefficient when you convert to vertex form?

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

Examples
~~~~~~~~

*Work these additional examples in your notebook or on a separate sheet of
paper.*

Sketch graphs of the following, **without generating a table of values!**

8. :math:`f(x)=x^2-2x+5` (where is the vertex? y intercept? points near vertex?)
9. :math:`f(x)=-2(x-2)^2+6` (where is the vertex? points near vertex? **hint**: a = -2)
