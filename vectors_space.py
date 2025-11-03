class R2Vector:
    """2D vector in real space (ℝ²)."""
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    @property
    def norm(self):
        """Return the Euclidean norm."""
        return sum(val ** 2 for val in vars(self).values()) ** 0.5

    def __str__(self):
        """Readable tuple-style representation."""
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        """Constructor-style representation."""
        args = ", ".join(f"{k}={v}" for k, v in vars(self).items())
        return f"{self.__class__.__name__}({args})"

    #def __getattribute__(self, attr):
        #"""Intercepts all lookups. Delegate to keep normal behavior."""
        #return object.__getattribute__(self, attr)

    #def __getattr__(self, attr):
        #"""Called only if attribute not found normally."""
        #return f'No attribute named {attr}'

    def __add__(self, other):
        """Add two vectors component-wise."""
        # Must be same type to add
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """Subtract two vectors component-wise."""
        # If not same type, cannot subtract
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """Multiply vectors: scalar multiplication or dot product."""
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
            # x1*x2 + y1*y2 -> returns scalar (e.g 2*0.5 + 3*1.25)
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            # Return just the sum of the products
            return sum(args)
        # If we get here, types are incompatible (e.g., vector * "string")
        return NotImplemented

class R3Vector(R2Vector):
    """3D vector extending R2Vector with a z component."""
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

v1 = R2Vector(x=2, y=3)
v2 = R2Vector(x=0.5, y=1.25)

# Addition and subtraction examples
v3 = v1 + v2
v4 = v1 - v2

print(f'v1 = {v1}')
print(f'v2 = {v2}')
print(f'v3 = {v3}')
print(f'v4 = {v4}')

# Display examples of both __str__ and __repr__ behavior
# print(f"{v1!r}") # uses __repr__ flag
# print(f'v1 = {v1}', f'\nrepr = {repr(v1)}\n')
# print(f'v2 = {v2}', f'\nrepr = {repr(v2)}')

# Using dot operator to access attributes
# print(v1.x) # Access x
# print(getattr(v1, 'x'))  # Access x using getattr

# Accessing an attribute that doesn't exist to trigger __getattr__
# print(v1.z)             # No attribute named z
# print(getattr(v1, 'z')) # No attribute named z
