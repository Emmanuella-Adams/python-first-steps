def create_character(name, strength, intelligence, charisma):
    # Name validations
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"

    # Stats validations
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    # Formatting output
    full = "●"
    empty = "○"
    
    str_bar = (full * strength) + (empty * (10 - strength))
    int_bar = (full * intelligence) + (empty * (10 - intelligence))
    cha_bar = (full * charisma) + (empty * (10 - charisma))

    return f"{name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"