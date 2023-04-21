def test_request_fixture(request):
    print(f"filepath {request.fspath}")
    print(f"fixturenames {request.fixturenames}")
    assert 1 == 1
