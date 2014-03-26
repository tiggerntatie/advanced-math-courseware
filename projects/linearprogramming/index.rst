PROJECT: Going to Extremes - An Investigation In Linear Programming
===================================================================

Part I: Maximize Profit
-----------------------

.. topic:: Scenario:

    It's that time of year! The Class of 2015 is selling gourmet candy as a
    fundraiser. They offer two different gift packages: The Classic (two
    chocolate-covered strawberries and four assorted chocolate truffles)
    and The Sweetheart (five chocolate-covered strawberries and five 
    assorted chocolate truffles). They sell The Classic for $5.00 and The 
    Sweetheart for $10.00.
    
    If 600 chocolate covered strawberries are purchased for $300 and 800 
    truffles are purchased for $200, what is the maximum profit the Class of
    2015 could make?
    
Gather Restrictions
~~~~~~~~~~~~~~~~~~~

The scenario contains a lot of information! Let's organize it in your notebook:

The total number of chocolate-covered strawberries available is 600. The 
cost (for the Class of 2015) is $300. 
    
1.  What is the cost per strawberry?

The total number of chocolate truffles avaialble is 800. The cost to the 
class is $200. 
    
2.  What is the cost per truffle?

A Classic gift package contains 2 strawberries and 4 truffles. 

3.  What does it cost to create a single Classic gift package?

The Classic gift package sells for $5. 

4.  What is the profit per Classic gift package?

A Sweetheart gift package contains 5 strawberries and 5 truffles. 

5.  What does it cost to create a single Sweetheart gift package?

The Sweetheart gift package sells for $10. 

6.  What is the profit per Sweetheart gift package? 

What are the UNKNOWNS? We know how many strawberries and truffles we have 
available. We know the profit for each Classic or Sweetheart gift package.
We do NOT know how many Classic or Sweetheart gift packages the class could 
make with the available candies, so we can assign variables to represent
the number of Classic or Sweetheart gift packages.

Let *x* represent the number of Classic gift packages, and let *y* represent
the number of Sweetheart gift packages:

7.  We already know something about *x* and *y*\: :math:`x \ge \underline{\hspace{1cm}}` and 
    :math:`y \ge \underline{\hspace{1cm}}`.

8.  Using the table below, write an appropriate mathematical expression to
    represent the total number of chocolate-covered strawberries and 
    chocolate truffles used in each gift package:
    
.. list-table::
   :widths: 20 30 30 30 50
   :header-rows: 1
   :stub-columns: 1

   * - 
     - Pieces per Classic
     - Pieces per Sweetheart
     - Pieces of candy available
     - Mathematical Expression
   * - \# of Chocolate-Covered Strawberries
     - 
     - 
     - 600
     - :math:`\underline{\hspace{1cm}}\cdot x + \underline{\hspace{1cm}} \cdot y \le \underline{\hspace{1cm}}`
   * - \# of Chocolate Truffles
     - 
     - 
     - 800
     - :math:`\underline{\hspace{1cm}}\cdot x + \underline{\hspace{1cm}} \cdot y \le \underline{\hspace{1cm}}`

You should now have a system of four inequalities: 
   
.. math:: 
   
    \begin{cases}
    x \ge \underline{\hspace{1cm}}\\
    \\
    y \ge \underline{\hspace{1cm}}\\
    \\
    \underline{\hspace{1cm}}\cdot x + \underline{\hspace{1cm}} \cdot y \le \underline{\hspace{1cm}}\\
    \\
    \underline{\hspace{1cm}}\cdot x + \underline{\hspace{1cm}} \cdot y \le \underline{\hspace{1cm}}
    \end{cases}

Graphing
~~~~~~~~

Carefully graph the system of inequalities on a sheet of graph paper (or in your notebook). 
Start with a simple sketch in order to figure out what scales you will need, then move 
on to the final draft.

When you graph a system of inequalities you will **shade** only the region of the graph that 
contains soluutions to the *entire* system. 

The shaded region is called a **feasible region**, because the only coordinates that are
feasible solutions to the system are contained in that region. 

Identify and label the vertices (corners) of the feasible region in your graph. 
**Show all your work!**

    
Maximizing Profit
~~~~~~~~~~~~~~~~~

Although the shaded region contains every possible solution to the system of inequalities,
we are interested in the solution that yields the *maximum profit*. 

From `Gather Restrictions`_ you determined the profit per Classic and Sweetheart
gift package.

Since the Class of 2015 is selling *x* Classic gift packages: 

9. What is the total profit from selling Classic gift packages?
   
Since the Class of 2015 is selling *y* Sweetheart gift packages:

10. What is the total profit from selling Sweetheart gift packages?
    
11. What is the total profit from selling all gift packages?

    Write this in the form: :math:`P=\underline{\hspace{1cm}} \cdot x + \underline{\hspace{1cm}} \cdot y`
    
:math:`P(x,y)` is called an **objective function** because it addresses our objective
of finding the maximum profit.

Corner Point Principle
~~~~~~~~~~~~~~~~~~~~~~

Although any coordinate in the feasible region will be a solution to our system, it has
been shown that for any objective function, the maximum or minum value of that 
objective function will *always* occur at a corner point (think about *why* that might
be true).

Therefore, we have to test only the coordinates of the corners (vertices) in our objective
function - whichever gives the maximum value of *P* will be our solution.

12. Complete this table in your notebook:

    .. list-table::
       :widths: 20 30 
       :header-rows: 1

       * - Coordinates
         - :math:`P=\underline{\hspace{1cm}} \cdot x + \underline{\hspace{1cm}} \cdot y`
       * - :math:`(\underline{\hspace{1cm}}, \underline{\hspace{1cm}})`
         - :math:`P=`
       * - :math:`(\underline{\hspace{1cm}}, \underline{\hspace{1cm}})`
         - :math:`P=`
       * - :math:`(\underline{\hspace{1cm}}, \underline{\hspace{1cm}})`
         - :math:`P=`
       * - :math:`(\underline{\hspace{1cm}}, \underline{\hspace{1cm}})`
         - :math:`P=`
 
Therefore, in order to make the greatest profit:

13. How many Classic gift packages should be sold?
14. How many Sweetheart gift packages should be sold? 
15. What is the total profit from the entire enterprise?


Minimizing Time
---------------

.. topic:: Scenario: 

    Hanover High School has received a grant to start a community srvice program
    for its juniors and seniors. They would like to send out teams of juniors 
    and seniors with faculty advisors to volunteer at the local library and the
    local elementary school. The library has an after school reading program which
    would require teams of 3 juniors, 3 seniors, and one advisor for two hours
    twice a week. The elementary school has a one-on-one tutoring program after 
    school which would require teams of 8 juniors, 4 seniors, and two advisors
    for two hours three times per week. In order to run the community service 
    program, the school needs to have at least 40 juniors, 28 seniors, and 12 
    faculty members involved.
    
    What is the total *minimum* number of hours that all the teams could work? 
    How many volunter teams for the library and elementary school would there be?
    

.. topic:: Submit: 

    Use what you learned from the first scenario:
    
    * On graph paper, restate the problem situation in your own words.
    * Be sure to identify the **variables**, the **inequalities**, graph the **feasible
      region**, identify the **vertices** and **objective function**, and the 
      **solution**.
    * Show all work!
    
