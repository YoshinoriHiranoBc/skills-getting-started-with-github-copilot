def test_signup_adds_participant_and_prevents_duplicate(client):
    # Arrange
    activity = "Chess Club"
    payload = {"name": "Alice", "email": "alice@example.com"}

    # Act: first signup (email passed as query param per app signature)
    r1 = client.post(f"/activities/{activity}/signup", params={"email": payload["email"]})

    # Assert: success
    assert r1.status_code == 200
    # Act: duplicate signup
    r2 = client.post(f"/activities/{activity}/signup", params={"email": payload["email"]})

    # Assert: duplicate handled (either 400 or 409 depending on implementation)
    assert r2.status_code in (400, 409)


def test_remove_participant(client):
    # Arrange
    activity = "Chess Club"
    payload = {"name": "Bob", "email": "bob@example.com"}
    client.post(f"/activities/{activity}/signup", params={"email": payload["email"]})

    # Act: remove participant (email passed as query param)
    r = client.delete(f"/activities/{activity}/participants", params={"email": payload["email"]})

    # Assert
    assert r.status_code == 200
