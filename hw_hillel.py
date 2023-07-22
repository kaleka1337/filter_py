def is_valid_data(item):
    return isinstance(item, (int, float)) and item > 500

some_data = [501, 'fff', 50, 0, -50.5, 'bat', 600, 358]

valid_data = list(filter(is_valid_data, some_data))

print(valid_data)