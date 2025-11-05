class R2Vector:
    """2D vector in real space (ℝ²)."""
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

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

    def __eq__(self, other):
        """Return True if all attributes are equal, False otherwise."""
        if type(self) != type(other):
            return NotImplemented
        if all(getattr(self, i) == getattr(other, i) for i in vars(self)):
            return True
        return False

    def __ne__(self, other):
        """Return True if any attribute differs, False otherwise."""
        return not self == other

    def __lt__(self, other):
        """Less-than comparison based on norm."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __le__(self, other):
        """Less-than-or-equal-to comparison based on norm."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() <= other.norm()

    def __gt__(self, other):
        """Greater-than comparison based on norm."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __ge__(self, other):
        """Greater-than-or-equal-to comparison based on norm."""
        if type(self) != type(other):
            return NotImplemented
        return self.norm() >= other.norm()



class R3Vector(R2Vector):
    """3D vector extending R2Vector with a z component."""
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z

    # A cross product is between two 3D vectors; and the result is another 3D vector.
    def cross(self, other):
        """Return the cross product of two R3 vectors."""
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)

if __name__ == "__main__":
    # Instantiate vectors
    v1 = R2Vector(x=2, y=3)
    v2 = R2Vector(x=0.5, y=1.25)
    v1_cross = R3Vector(x=2, y=3, z=1)
    v2_cross = R3Vector(x=0.5, y=1.25, z=2)

    # Cross product result
    v6_cross = v1_cross.cross(v2_cross)

    # Arithmetic
    v3 = v1 + v2
    v4 = v1 - v2
    v5 = v1 * 3          # Scalar multiplication
    v6 = v1 * v2         # Dot product

    print("Vector Instances")
    print("-------------------------")
    print(f'v1 = {v1}')
    print(f'v2 = {v2}')

    print("\nAddition and Subtraction")
    print("-------------------------")
    print(f'v1 + v2 = {v3}')
    print(f'v1 - v2 = {v4}')

    print("\nScalar multiplication")
    print("-------------------------")
    print(f'v1 * 3 = {v5}')

    print("\nDot product")
    print("-------------------------")
    print(f'v1 * v2 = {v6}')

    print("\nEquality Checks")
    print("-------------------------")
    print(f'v1 == v2: {v1 == v2}')
    print(f'v1 != v2: {v1 != v2}')
    print('v1 == R2Vector(x=2, y=3):', v1 == R2Vector(x=2, y=3))
    print('v1 != R2Vector(x=2, y=3):', v1 != R2Vector(x=2, y=3))

    print("\nComparison Checks")
    print("-------------------------")
    print('v1 <  v2:', v1 < v2)
    print('v1 <= v2:', v1 <= v2)
    print('v1 >  v2:', v1 > v2)
    print('v1 >= v2:', v1 >= v2)

    print('\nCross Product of R3 Vectors')
    print('-------------------------')
    print(f'v1_cross = {v1_cross}')
    print(f'v2_cross = {v2_cross}')
    print(f'v1_cross.cross(v2_cross) = {v6_cross}')

    print("\nString and Representation Examples")
    print("-------------------------")
    print(f"{v1!r}")  # uses __repr__
    print(f'v1 = {v1}', f'\nrepr = {repr(v1)}')
    print(f'v2 = {v2}', f'\nrepr = {repr(v2)}')

    print("\nAttribute Access Examples")
    print("-------------------------")
    print(f"v1.x = {v1.x}")  # normal access
    print(f"getattr(v1, 'x') = {getattr(v1, 'x')}")  # getattr access

    # print("\nInvalid Operation Result")
    # print("-------------------------")
    # v7 = v1 + R3Vector(x=1, y=2, z=3)  # Different types cannot be added
    # print(f'v7 = {v7}')  # Should print: v7 = NotImplemented

    # Attempt to access nonexistent attribute
    # try:
        #print(v1.z)
    # except AttributeError:
        #print("No attribute named z (AttributeError)")

    # try:
        #print(getattr(v1, 'z'))
    # except AttributeError:
        #print("getattr(v1, 'z') raised AttributeError")
