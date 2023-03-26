def check_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, int):
        return str(value)
    else:
        return f"'{value}'"


def format_to_plain(tree, path=""):
    result = []
    for node in tree:
        current_path = f'{path}{node["key"]}'
        if node["type"] == "added":
            result.append(
                f"Property '{current_path}' "
                f"was added with value: "
                f"{check_value(node['value'])}")

        if node["type"] == "removed":
            result.append(f"Property '{current_path}' was removed")

        if node["type"] == "changed":
            result.append(
                f"Property '{current_path}'"
                f" was updated. From {check_value(node['old_value'])} "
                f"to {check_value(node['new_value'])}")

        if node["type"] == "nested":
            new_value = format_to_plain(node['children'], f"{current_path}.")
            result.append(f"{new_value}")

    return "\n".join(result)
