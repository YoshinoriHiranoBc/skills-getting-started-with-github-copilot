def test_root_redirects_to_static_index(client):
    # Arrange: client fixture provided

    # Act
    resp = client.get("/")

    # Assert
    assert resp.status_code in (200, 307, 308)


def test_get_activities_returns_mapping_and_schema(client):
    # Arrange

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # pick one activity and verify schema
    key, item = next(iter(data.items()))
    assert "description" in item
    assert "participants" in item
    assert isinstance(item["participants"], list)
