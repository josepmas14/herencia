from cesar import Cesar

def test_create_cesar():
    cesar = Cesar(3)
    assert cesar.clave == 3

def test_clave_must_be_integer():
    
    try:
        cesar = Cesar("lolailo")
        mensaje = 0
    except AttributeError:
        mensaje = 1
    assert mensaje == 1 # Se ha lanzado un atribute error
