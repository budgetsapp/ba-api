all_categories = [{
    "id": "123e4567-e89b-12d3-a456-426655440001",
    "user_id": "123e4567-e89b-12d3-a456-426655440000",
    "display_name": "taxi"
}, {
    "id": "123e4567-e89b-12d3-a456-426655440002",
    "user_id": "123e4567-e89b-12d3-a456-426655440000",
    "display_name": "cafe"
}, {
    "id": "123e4567-e89b-12d3-a456-426655440003",
    "user_id": "123e4567-e89b-12d3-a456-426655440000",
    "display_name": "cinema"
}, {
    "id": "123e4567-e89b-12d3-a456-426655440004",
    "user_id": "123e4567-e89b-12d3-a456-426655440000",
    "display_name": "bus"
}]


def getCategoryById(categery_id):
    for cat in all_categories:
        if cat["id"] == categery_id:
            return cat
    return None
