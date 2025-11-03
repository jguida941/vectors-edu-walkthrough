# Inspired by a FreeCodeCamp exercise.
# Expanded with additional documentation and commentary
# to improve conceptual understanding for beginners.
# Author: Justin Guida

from math import sqrt # used for __slots__ example (R5Vector)

class R2Vector:
    """
    Represents a two-dimensional vector in real space (ℝ²).

        Attributes
        ----------
        x : float
            Horizontal component.
        y : float
            Vertical component.

        Methods
        -------
        norm():
            Compute the Euclidean length √(x² + y²).
        __str__():
            Return a human-readable string like "(x, y)".
        __repr__():
            Return a constructor-style string like R2Vector(x=2, y=3).
        """

    # Constructor to initialize the vector components x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        """Compute the Euclidean norm (length) of the vector."""
        # Original (2D only):
        # return (self.x ** 2 + self.y ** 2) ** 0.5

        # Instead of explicitly using self.x and self.y,
        # we can use self.__dict__, which stores all instance attributes
        # and their current values
        # Example: {'x': 2, 'y': 3} for 2D, or {'x': 2, 'y': 2, 'z': 3} for 3D
        # This makes the same formula work for any vector dimension
        #return sum(val ** 2 for val in self.__dict__.values()) ** 0.5

        # The vars() built-in returns the __dict__ of an object,
        # improving readability while doing the same thing as self.__dict__.
        return sum(val ** 2 for val in vars(self).values()) ** 0.5

    def __str__(self):
        """Return a readable string like "(x, y)"."""
        # vars(self) → the attribute dictionary, e.g. {'x': 1, 'y': 2}
        # for i in vars(self) → loops over its keys ('x', 'y')
        # getattr(self, i) → fetches each value (1, 2) by name
        # The generator builds a tuple (1, 2)
        # str(...) converts that tuple into the string "(1, 2)".
        return str(tuple(getattr(self, i) for i in vars(self)))

    # __repr__ is designed to show the exact constructor-style call
    # that would recreate the same object.
    # you can think of __repr__ as
    # the string form of the original constructor call.
    def __repr__(self):
        """Return an unambiguous string like R2Vector(x=2, y=3)."""
        # loop through the attributes dictionary of the object and store in list
        # items() gives key–value pairs:
        # for every key, value pair in that dictionary, build a formatted string like "x = 2".
        arg_list = [f"{key} = {val}" for key, val in vars(self).items()]

        # Join all those strings with commas to make a single argument string
        arg_str = ", ".join(arg_list)

        # Build the final string with class name and argument string
        # self.__class__.__name__ dynamically gets the actual class name of the object
        # Example: for an R3Vector instance, it would return 'R3Vector'
        # The formatted string then produces something like:
        # "R2Vector(x=2, y=3)" or "R3Vector(x=2, y=3, z=4)"
        return f"{self.__class__.__name__}({arg_str})"

# Inheritance lets a class inherit methods and properties from a parent class
class R3Vector(R2Vector):
    """Represents a 3D vector that inherits behavior from R2Vector."""

    # Since this is a 3D vector, we add one more variable z
    # * is a keyword-only argument marker
    # all parameters after * must be passed by name, not by position.
    def __init__(self, *, x, y, z):
        # super() calls the parent class (R2Vector) to initialize x and y
        super().__init__(x=x, y=y)
        self.z = z

"""
Practice here making a 4D vector class that inherits from R2Vector.
This class should add two new attributes: z and w.
It should reuse the R2Vector constructor to initialize x and y.
"""
class R4Vector(R2Vector):
    """Represents a 4D vector that inherits behavior from R2Vector."""

    # Since this is a 4D vector, we add two more variables z and w
    # * is a keyword-only argument marker
    # all parameters after * must be passed by name, not by position.
    def __init__(self, *, x, y, z, w):
        # super() calls the parent class (R2Vector) to initialize x and y
        super().__init__(x=x, y=y)
        self.z = z
        self.w = w

# 5D vector using __slots__ to save memory
class R5Vector(R2Vector):
    """Represents a 5D vector using __slots__ for memory efficiency
    __slots__ can't use __dict__
    One way to work around this is to explicitly list the attributes in __slots__.
    This prevents dynamic attribute creation but saves memory."""

    __slots__ = ('x', 'y', 'z', 'w', 'v')  # Predefine allowed attributes
    def __init__(self, *, x, y, z, w, v):
        super().__init__(x=x, y=y)
        self.z = z
        self.w = w
        self.v = v

    def norm(self):
        """Compute the Euclidean norm (length) of the 5D vector."""
        return sqrt(self.x**2 + self.y**2 + self.z**2 + self.w**2 + self.v**2)

    def __str__(self):
        """Return a readable string like "(x, y, z, w, v)"."""
        return str((self.x, self.y, self.z, self.w, self.v))

    def __repr__(self):
        """Return an unambiguous string like R5Vector(x=1, y=2, z=3, w=4, v=5)."""
        return f"R5Vector(x={self.x}, y={self.y}, z={self.z}, w={self.w}, v={self.v})"

    # __add__(self, other)
    # Runs for "left + right".
    # v1 + v2  -->  v1.__add__(v2)
    #              ^self         ^other (what's on the RIGHT of +)
    # Adds matching fields and returns a NEW object.
    # If types don't match, return NotImplemented so Python knows this add doesn't apply.
    # Example: (1,2) + (5,7) -> (6,9)
    def __add__(self, other):
        """Vector addition of two vectors of the same type."""
        # Check if both vectors are of the same type
        # You can add R2Vector + R2Vector.
        # But not R2Vector + R3Vector or R5Vector + int
        if type(self) != type(other):
            return NotImplemented
        # Create a new instance of the same class with summed attributes
        # key arguments are looped through from vars(self) and added together
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        # pass **kwargs to unpack the dictionary into keyword arguments
        return self.__class__(**kwargs) # example R5Vector(x=6, y=9, z=..., w=..., v=...)

    def __sub__(self, other):
        """Vector subtraction of two vectors of the same type."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """
        Multiply vector by a scalar.

        A scalar (int or float) multiplies each component of the vector.
        Example:
            v = (x, y, z)
            k = 3
            k * v = (3x, 3y, 3z)

        This changes the vector's magnitude but not its direction.
        """
        # Scalar multiplication case
        if type(other) in (int, float):
            # x = x * number, y = y * number → returns new vector..
            # x=2*2, y=3*2
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            # return the vector class with the arguments unpacked
            return self.__class__(**kwargs)

        # Dot product case
        elif type(self) == type(other):
            # Dot product
            # x1*x2 + y1*y2 -> returns scalar
            # 2*0.5 + 3*1.25
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            # return just the sum of the products
            return sum(args)
        return NotImplemented


# 6D vector using __slots__, using show_attributes method to display attributes
class R6Vector(R2Vector):
    """Represents a 6D vector using __slots__ for memory efficiency.
    Uses show_attr method to display attributes, without having
    to explicitly reference each attribute."""

    __slots__ = ('z', 'w', 'v', 'u')  # Only need to list new attributes

    # static method doesn't require self parameter
    # static method allows calling the method on the class itself
    @staticmethod
    def show_attr(obj):
        # Get regular attributes (for classes that have __dict__)
        dict_attrs = getattr(obj, "__dict__", {})

        # Get slotted attributes (for classes that use __slots__)
        slot_attrs = {
            name: getattr(obj, name)
            for name in getattr(obj, "__slots__", ())
            if name != "__dict__"
        }

        # Combine both into one dictionary and return it
        return {**dict_attrs, **slot_attrs}

    # Constructor for R6Vector
    def __init__(self, *, x, y, z, w, v, u):
        super().__init__(x=x, y=y)
        # You can also initialize attributes all in one clean line
        self.z, self.w, self.v, self.u = z, w, v, u


# Instantiate using keyword arguments (required because of *)
v1 = R2Vector(x=2, y=3)
# v2 = R3Vector(x=2, y=2, z=3) # commented out for step 47

# Step 47 we modify v2 variable assignment to be R2Vector instance
# to have x = 0.5, and y = 1.25
v2 = R2Vector(x=0.5, y=1.25)
v3 = R4Vector(x=1, y=2, z=3, w=4)

# R5Vector using __slots__
v4 = R5Vector(x=1, y=2, z=3, w =4, v=5)

# R6Vector using __slots__ and show_attr method
v5 = R6Vector(x=1, y=2, z=3, w=4, v=5, u=6)

# Print bound method reference (shows module and memory address)
print("v1.norm method reference:")
print(v1.norm)

# Call the method through the object
print("\nv1.norm() call result:")
print(v1.norm())  # 3.605551275463989

# __str__ makes print(v1) show coordinates instead of a memory address
print("\nv1 printed:")
print(v1)  # (2, 3)

# Demonstrate inheritance and method reuse
print("\nv2 printed and v2.norm() call result:")
print(v2)         # uses R2Vector.__str__
print(v2.norm())  # reuses parent method

# Inspect each instance’s internal attribute dictionary (__dict__).
# This shows all attributes stored in the object and their values.
# Example:
#   v1 = R2Vector(x=2, y=3) → {'x': 2, 'y': 3}
#   v2 = R3Vector(x=2, y=2, z=3) → {'x': 2, 'y': 2, 'z': 3}
print("\nv1 and v2 __dict__ contents:")
print("v1.__dict__:", v1.__dict__)
print("v2.__dict__:", v2.__dict__)

# Demonstrate __repr__ and __str__ usage with f-string formatting
print("\nrepr(v1), str(v1), and f'{v1!r}':")
print("repr(v1):", repr(v1))  # Explicitly calls __repr__
print("str(v1):", str(v1))    # Calls __str__
print("f'{v1!r}':", f"{v1!r}")  # !r calls __repr__


# Show both __str__ and __repr__ for all vector instances
print("\nDisplaying all vector instances with __str__ and __repr__:")
print(f"\nv1 = {v1}\nrepr = {repr(v1)}\n") #R2Vector
print(f"v2 = {v2}\nrepr = {repr(v2)}\n")   #R3Vector
print(f"v3 = {v3}\nrepr = {repr(v3)}\n")   #R4Vector
print(f"v4 = {v4}\nrepr = {repr(v4)}\n")   #R5Vector using __slots__
print(f"v5 = {v5}\nrepr = {repr(v5)}\n")   #R6Vector using __slots__ and show_attr method

# directly call show_attr method to display attributes
print("v5 attributes using R6Vector.show_attr method:")
print(R6Vector.show_attr(v5))

# Educational purpose:
# This file demonstrates Python OOP basics — constructors, inheritance,
# instance attributes, __dict__, __str__, __repr__, and f-string formatting.
