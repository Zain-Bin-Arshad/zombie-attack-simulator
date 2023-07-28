class Edible:

    def __init__(self, edible_type: str, position: list[int], edible_data: dict[str, str | int]):
        self.position = position
        self.edible_type = edible_type
        self.label = edible_type.title()
        self.color = edible_data["color"]
        self.marker = edible_data["marker"]
        self.health_increase_capacity = edible_data["health_capacity"]
        self.is_dead = False  # Food never gets spoiled

    def __str__(self):
        return f"Type: {self.edible_type}\nPosition: {self.position}"
