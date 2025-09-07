from crewai.tools import tool


@tool
def count_letters(sentence: str):
    """
    This function is to count the amount of letters in a sentence.
    The input is a 'sentence' string.
    The out put is a number.
    """
    return len(sentence)
