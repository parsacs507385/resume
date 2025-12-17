import um

def test_count():
    assert um.count("um?") == 1
    assert um.count("um") == 1
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert um.count("Um, thanks, um...") == 2


def test_count_fail():
    assert um.count("yummy") == 0
    assert um.count("Album") == 0
    assert um.count("Plum") == 0
    assert um.count("Humble") == 0
