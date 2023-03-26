def get_diff_tree(first_file, second_file):
    tree = []
    all_keys = sorted(list(set(first_file) | set(second_file)))
    for key in all_keys:
        if key not in first_file:
            child = {
                'type': 'added',
                'key': key,
                'value': second_file[key]
            }
        elif key not in second_file:
            child = {
                'type': 'removed',
                'key': key,
                'value': first_file[key]
            }
        elif isinstance(first_file[key], dict) and \
                isinstance(second_file[key], dict):
            child = {
                'type': 'nested',
                'key': key,
                'children': get_diff_tree(first_file[key], second_file[key])
            }
        elif first_file[key] == second_file[key]:
            child = {
                'type': 'same',
                'key': key,
                'value': first_file[key]
            }
        else:
            child = {
                'type': 'changed',
                'key': key,
                'old_value': first_file[key],
                'new_value': second_file[key]
            }
        tree.append(child)
    return tree
