def walk_json(data, history=None, depth=0, path=None):
    if history is None:
        history = []
    if path is None:
        path = []

    # если словарь
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = path + [key]
            history.append({
                "depth": depth,
                "key_or_index": key,
                "value": value,
                "path": current_path.copy()
            })
            walk_json(value, history, depth + 1, current_path)

    # если список
    elif isinstance(data, list):
        for index, value in enumerate(data):
            current_path = path + [index]
            history.append({
                "depth": depth,
                "key_or_index": index,
                "value": value,
                "path": current_path.copy()
            })
            walk_json(value, history, depth + 1, current_path)

    return history


# пример данных (JSON-подобная структура)
data = {
    "user": {
        "name": "Alex",
        "skills": ["Python", "C++", {"level": "junior"}]
    },
    "active": True
}

history = walk_json(data)

# вывод истории обхода
for record in history:
    print(record)
