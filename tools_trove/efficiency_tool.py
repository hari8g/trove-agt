def calculate_efficiency(consumption: float, production: float) -> str:
    """
    Calculates energy efficiency as a percentage.
    
    :param consumption: The amount of energy consumed.
    :param production: The total energy available or generated.
    :return: A formatted string with the efficiency percentage.
    """
    if production == 0:
        return "Error: Production value cannot be zero."
    
    efficiency = (consumption / production) * 100
    return f"Energy efficiency is {efficiency:.2f}%."
