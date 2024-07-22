from challenge02 import first_repeated_word 

def test_first_repeated_word_case_1():
    """
    Test case 1: Check for repeated word in the string with multiple occurrences.
    """
    input_string = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    expected_output = "ASAC"
    assert first_repeated_word(input_string) == expected_output

def test_first_repeated_word_case_2():
    """
    Test case 2: Check for a string with no repeated words.
    """
    input_string = "I am learning programming at ASAC."
    expected_output = "No Repetition"
    assert first_repeated_word(input_string) == expected_output

def test_first_repeated_word_case_3():
    """
    Test case 3: Check for repeated word in a simple space-separated string.
    """
    input_string = "a b c d e f g a"
    expected_output = "a"
    assert first_repeated_word(input_string) == expected_output

def test_first_repeated_word_case_4():
    """
    Test case 4: Check for a string with all unique words.
    """
    input_string = "unique words only"
    expected_output = "No Repetition"
    assert first_repeated_word(input_string) == expected_output
