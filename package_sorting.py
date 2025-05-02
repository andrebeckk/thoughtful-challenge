def sort(width: float, height: float, length: float, mass: float):
    """Classify a package into one of the three stacks based on its dimensions and mass.

    Args:
        width (float): Width of the package in centimeters.
        height (float): Height of the package in centimeters.
        length (float): Length of the package in centimeters.
        mass (float): Mass of the package in kilograms.

    Returns:
        str: Name of the stack where the package should be placed ('STANDARD', 'SPECIAL' or 'REJECTED').
    """

    # Define maximum reasonable values that could be changed in the future based on requirements
    MAX_DIMENSION = 1000  # cm
    MAX_MASS = 1000       # kg
    
    if max(width, height, length) > MAX_DIMENSION or mass > MAX_MASS:
        raise ValueError("Dimensions or mass are too large")
    
    # Type validation
    try:
        width, height, length, mass = float(width), float(height), float(length), float(mass)
    except (ValueError, TypeError):
        raise TypeError("All inputs must be numeric values")
        
    # Positive values validation
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All dimensions and mass must be positive values")
        
    # Sorting logic
    volume = width * height * length
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    

# Test cases
def test_sort():
    # Standard package
    assert sort(10, 10, 10, 1) == "STANDARD"
    
    # Bulky by volume package
    assert sort(100, 100, 100, 5) == "SPECIAL"
    
    # Heavy package
    assert sort(20, 20, 20, 25) == "SPECIAL"
    
    # Both bulky and heavy package
    assert sort(100, 100, 100, 25) == "REJECTED"
    
    # Bulky by dimension package
    assert sort(160, 10, 10, 5) == "SPECIAL"

    try:
        sort(-1, 10, 10, 10)
        assert False, "Should have raised ValueError for negative dimensions."
    except ValueError:
        pass
    
    try:
        sort(0, 10, 10, 10)
        assert False, "Should have raised ValueError for zero dimensions."
    except ValueError:
        pass
    
    try:
        sort("10", 10, 10, 10)
        assert False, "Should have raised TypeError for non-numeric dimensions."
    except TypeError:
        pass
    
    try:
        sort(1000001, 10, 10, 10)
        assert False, "Should have raised ValueError for too large dimensions."
    except ValueError:
        pass
    
    print("All tests passed!")

# Run tests
test_sort()