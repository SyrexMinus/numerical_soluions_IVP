# Python IVP GUI
Python GUI app. Display the solution of initial value (Cauchy) problem. Solution for the assignment in differential equations course in Innopolis University.

## Requirements:
- Python 3.9.6
- tkinter
- matplotlib
- numpy

## Usage:
1. install requirements
2. `python manage.py`

## Work description
### Work aim: 
Automate the application of computational methods to solve the initial value problem, visualize the constructed solutions. Compare the values of local truncation error for different numerical methods, estimate the change in total error with an increase in the number of steps in the interval.
### Given
![](https://habrastorage.org/webt/qg/b0/xs/qgb0xsa05s0wd-jkmosdzgdqmcs.png)

#### Initial value problem:
![](https://habrastorage.org/webt/cx/y_/tf/cxy_tftpk5dnrlgkygw1c0ocvd0.png)

### My exact solution
Exact solution in terms of x0 and y0
system:
```
  y’ = (y^2-y) / x
  y(1) = 0.5
  x belongs to [1; 9]
  Domain restriction: 
    x != 0
  rewrite y’:
    dy / dx = (y^2-y) / x
  bring the equation above to the separable form (assume that y != 0 and y != 1)
    dy / (y^2-y) = dx / x
  integrate both sides of the equation above:
    integral (dy / ((y-1/2)^2-1/4)) = ln|x| + C
    make a substitution:
      u = y - ½, du = dy
    integral (du / (u^2 - 1/4)) = ln|x| + C
    make a substitution:
      s = 2u, ds = 2du
    -2 * integral (ds / (1-s^2)) = ln|x| + C
    -2 * (tanh(s))^(-1) = ln|x| + C
    substitute back u:
      -2 * (tanh(2u))^(-1) = ln|x| + C
    substitute back y:
      -2 * (tanh(1 - 2y))^(-1) = ln|x| + C
    ln(1-y) - ln(y) = ln|x| + C
    ln((1-y)/y) = ln|x| + C
    (1-y)/y = C1*|x|
  find C1:
    substitute x0 and y0:
      (1-0.5) / 0.5 = C1
    C1 = 1
    |x| = 1/y - 1
  explicit solution:
    y = 1 / (|x|+1) for x belongs R \ 0
```
	
### Analysis of points of discontinuity, if they exist
```
check x = 0
lim (1/(-x+1)) as x->-0 = 1
lim (1/(x+1)) as x->+0 = 1
since limits are equal to each other, it is removable discontinuity
```

### Source code
#### Code implements:
Methods: 
- Euler’s
- improved Euler’s
- Runge-Kutta

GUI:
- that allows the user to change x0, y0, X, N
- inputting starting and finishing values of the number of grid cells

Plot the graphs of: 
- exact solution
- numerical solution
- local errors for each method
- total errors for each method
- Analyze the total approximation error depending on the number of grid cells
- Results section should be named “final report”

Code style:
- OOP-design standards
- SOLID principles

### UML-diagrams of classes
![](https://habrastorage.org/webt/ym/b1/wb/ymb1wbkgxsngn_g_urvnq80jsas.png)

### Most interesting parts of source code
The class y_i is used to calculate the numerical solution of the ODE. It contains attributes: the derivative of the y, current x and y and step size. It contains 3 methods that compute the next approximate value. 

```
# calculations.py
class y_i:
   def __init__(self, step, f, y0, x0):
       ...
   def next_euler(self):
       ...
   def next_improved_euler(self):
       ...
   def next_runge_kutter(self):
       ...
```

The class GUI is used to build the program’s window and display it. It contains attributes: objects in the window and graphs’ parameters. It contains methods for initialization objects in the window (_init_window, _init_final_report_frame), for initialization graphs’ parameters (_init_graph_values), and 2 methods for updating graphs (_read_input, update_final_report). 

```
# GUI.py
class GUI:
   def __init__(self):
      ...
   def _init_user_input_frame(self):
      ...
   def _init_graph_values(self):
      ...
   def _init_final_report_frame(self):
      ...
   def _init_window(self):
      ...
   def _read_input(self):
      ...
   def update_final_report(self):
      ...
```

To avoid computation of functions where they do not exist, I used a special trick to avoid it. Trick: code checks if the x turns to an impossible value. If so then it adds a small delta to each step, so x never turns into impossible values.

```
# calculations.py get_solutions_info
if 0.0 in arange(x0_, X_ + step, step):
   x0_ += 0.00001
   X_ += 0.00001
```
  
### Screenshots of numerical investigations
![](https://habrastorage.org/webt/e0/93/xh/e093xhfcxwvshlwgneb9hnxmsb0.png)

### Conclusion
I automated the application of computational methods to solve the initial value problem, and visualized the constructed solutions. Comparing the values of local truncation error for different numerical methods shows that Runge-Kutta method is the most accurate, Improved Euler’s have comparable accuracy with Runge-Kutta, and Euler’s method has relatively big truncation error. Estimation of the change in total error with an increase in the number of steps in the interval shows that increase of the number of steps yields less total error for all methods.
