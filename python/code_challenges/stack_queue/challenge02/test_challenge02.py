from challenge02 import is_valid

def test_valid_parentheses():
    assert is_valid("()") == True 
    assert is_valid("()[]{}") == True 
    assert is_valid("[({}]") == False 
    assert is_valid("[(hello)()]") == True 
    assert is_valid("[{(())}]") == True 
    assert is_valid("[(])") == False 
    assert is_valid("([)]") == False 