from src.math_operations import add,subtract

def test_add():
    assert add(2,3)==5  ##assert will check that this statement gets true 
    assert add(-1,1)==0
    
    
def test_subtract():
    assert subtract(5,3)==2
    assert subtract(4,3)==1
    assert subtract(1,9)==-8