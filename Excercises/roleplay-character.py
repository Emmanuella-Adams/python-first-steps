def create_character(character_name, strength, intelligence, charisma):
    """
    Creates a character for an RPG adventure with validation.

    Args:
        character_name (str): The name of the character.
        strength (int): The strength stat.
        intelligence (int): The intelligence stat.
        charisma (int): The charisma stat.

    Returns:
        str: The character sheet or an error message.
    """
    # Character name validation
    if not isinstance(character_name, str):
        return "The character name should be a string."
    if len(character_name) > 10:
        return "The character name is too long."
    if ' ' in character_name:
        return "The character name should not contain spaces."

    stats = [strength, intelligence, charisma]

    # Stats validation
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers."
    if any(stat < 1 for stat in stats):
        return "All stats should be no less than 1."
    if any(stat > 4 for stat in stats):
        return "All stats should be no more than 4."
    if sum(stats) != 7:
        return "The character should start with 7 points."

    # If all validations pass, create the character sheet
    full_dot = '●'
    empty_dot = '○'

    str_dots = full_dot * strength + empty_dot * (10 - strength)
    int_dots = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_dots = full_dot * charisma + empty_dot * (10 - charisma)

    return f"{character_name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"