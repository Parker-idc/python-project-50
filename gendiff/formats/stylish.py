START_INDENT = 4


def get_nested(value, depth, indent=' '):
    if isinstance(value, dict):
        result = ["{"]
        for key, nest_val in value.items():
            if isinstance(nest_val, dict):
                new_value = get_nested(nest_val, depth + START_INDENT)
                result.append(f"{indent * depth}    {key}: {new_value}")
            else:
                result.append(f"{indent * depth}    {key}: {nest_val}")
        result.append(f'{indent * depth}}}')
        return '\n'.join(result)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return value


def get_tag(sign):
    indent = " "
    tag = {
        "added": "+",
        "removed": "-",
        "nothing": " "
    }
    return f'{indent * 2}{tag[sign]}{indent}'


def output_node(dict, key, depth, sign):
    return f"{' ' * depth}{sign}{dict['key']}: \
{get_nested(dict[key], depth + START_INDENT)}"


def format_to_stylish(tree, depth=0): # noqa: format_to_stylish: 15
    result = ['{']
    for node in tree:
        if node["type"] == "same":
            result.append(output_node(
                node, 'value',
                depth, get_tag("nothing")
            ))

        if node["type"] == "added":
            result.append(output_node(
                node, "value",
                depth, get_tag("added")
            ))

        if node["type"] == "removed":
            result.append(output_node(
                node, "value",
                depth, get_tag("removed")
            ))

        if node["type"] == "changed":
            result.append(output_node(
                node, "old_value",
                depth, get_tag("removed")
            ))

            result.append(output_node(
                node, "new_value",
                depth, get_tag("added")
            ))

        if node["type"] == "nested":
            result.append(
                f"{' ' * depth}    {node['key']}:"
                f" {format_to_stylish(node['children'], depth + START_INDENT)}")

    result.append(f'{" " * depth}}}')
    return "\n".join(result)
