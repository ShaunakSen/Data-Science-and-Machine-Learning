# Math for ML: Linear Algebra

## W&B Linear Algebra Tutorial

Notes on video by Weights and Bias: https://www.youtube.com/watch?v=uZeDTwWcnuY

![https://i.imgur.com/9ecmRPm.png](https://i.imgur.com/9ecmRPm.png)

![https://i.imgur.com/9ecmRPm.png](https://i.imgur.com/9ecmRPm.png)

**Linear Algebra is like the math of arrays**

Very often, the data we deal with, in ML, is represented by arrays

The core operation in LA is matrix multiplication

Some examples:

![https://i.imgur.com/IFfTMqg.png](https://i.imgur.com/IFfTMqg.png)

This is a pictorial representation of the matrix mul:

![https://i.imgur.com/fz5B3RT.png](https://i.imgur.com/fz5B3RT.png)

This is the rule that we have all learnt and accepted, but seems strangely uninspired

### LA as programming

Linear algebra is more like programming

*Matrices are Functions, Shapes are Types, and Multiplication is Composition*

- In programming, we combine functions with matching types through function composition
- In linear algebra, we combine matrices with matching shapes through matrix multiplication.

In programming, we define one f’n in terms of others:

![https://i.imgur.com/iZieYln.png](https://i.imgur.com/iZieYln.png)

![https://i.imgur.com/dOZLqDG.png](https://i.imgur.com/dOZLqDG.png)

![https://i.imgur.com/GPEZIdA.png](https://i.imgur.com/GPEZIdA.png)

This is in essence the core of programming, we take a bunch of inputs apply them to function and get some output

*Matrix-vector multiplication is just like function application:*

M is the matrix applied as a function to the vector v and op is Mv

![https://i.imgur.com/N51C7OK.png](https://i.imgur.com/N51C7OK.png)

So this matrix is a function that takes in arrays of shape (k,1) as ip and ops arrays of shape (3,1)

Lets take an example value of M and see:

![https://i.imgur.com/LgEuApD.png](https://i.imgur.com/LgEuApD.png)

Here M the function can be named as `select_first_two_elems`

While doing math we simply name them as X,Y etc but this is what it actually does

*Matrix-matrix multiplication is function composition.*

This is like we are applying one function to the op of another function

![https://i.imgur.com/njNYcvI.png](https://i.imgur.com/njNYcvI.png)

X (input: array(3, k)) → (2, k)

Y(input: array(2, k)) → (2, k)

(3, k) input to X can be thought of as a sample 3D coordinates (k=1)

What X does is it strips away the 3rd (Z) axis

Then op of X is 2x1

Y then only considers the first (X) axis and puts a value of 0 in Y axis and returns a vector of shape: 2x1

![https://i.imgur.com/7TS4Coi.png](https://i.imgur.com/7TS4Coi.png)

The combination of these 2 functions is also a matrix (function)

This 3rd matrix is obtained from matrix mul of X and Y

![https://i.imgur.com/HFJJ9Aw.png](https://i.imgur.com/HFJJ9Aw.png)