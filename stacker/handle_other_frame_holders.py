from typing import Any
from typing import Dict

from .tree_root_to_leaf import Node

def sort_view_model_for_paned_window(view_model: list) -> list:
    # create Nodes and widget_model_dictionary
    parent_id_to_children_widget_models: Dict[Any, list] = {'root': []}
    parent_id_to_children_widget_ids: dict = {'root': []}
    widget_id_to_widget_model = {}
    frame_id_to_frame_options = {}
    pn_parents = set()

    root = Node('root')
    id_to_node = {'root': root, }
    pn_ids = []
    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]
        widget_type = widget_model[2]

        if widget_type in ['paned_window', 'notebook', ]:
            pn_ids.append(widget_id)
            pn_parents.add(parent_id)
        if widget_type == 'frame':
            frame_options: dict = widget_model[-1].get('frame options', {})  # this logic looks so easy to break...
            frame_id_to_frame_options[widget_id] = frame_options

        # build dictionary
        if parent_id in parent_id_to_children_widget_models:
            parent_id_to_children_widget_models[parent_id].append(widget_model)
        else:
            parent_id_to_children_widget_models[parent_id] = [widget_model]
        if parent_id in parent_id_to_children_widget_ids:
            parent_id_to_children_widget_ids[parent_id].append(widget_id)
        else:
            parent_id_to_children_widget_ids[parent_id] = [widget_id]
        widget_id_to_widget_model[widget_id] = widget_model

        # create Nodes
        new_node = Node(widget_id)
        id_to_node[widget_id] = new_node

    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]

        node = id_to_node[widget_id]
        parent_node = id_to_node[parent_id]
        node.set_previous(parent_node)
        parent_node.add_next(node)

    # Identify leaves
    leaves = []
    all_nodes = tuple(id_to_node.values())
    for node in all_nodes:
        if node == 'root':
            continue
        if not node.next_nodes:
            leaves.append(node)

    # Get all paths from root to leaves
    complete_paths = []
    for each_leaf in leaves:
        path = [each_leaf.name]
        parent_node = each_leaf.previous_node
        while parent_node != 'root':
            path.insert(0, parent_node.name)
            parent_node = parent_node.previous_node

        if path[0] != 'root':
            path.insert(0, 'root')
        complete_paths.append(path)

    already_inserted_widget_id = {'root'}
    already_inserted_pair = set()
    for pn_id in pn_ids:
        already_inserted_widget_id.add(pn_id)  # pn_id's children frame are automatically created

    sorted_view_model = []
    for path in complete_paths:
        for parent_id in path:
            if parent_id not in already_inserted_widget_id:
                parent_widget_model = widget_id_to_widget_model[parent_id]

                parent_of_parent = parent_widget_model[0]
                has_already_been_added = (parent_of_parent, parent_id) in already_inserted_pair
                if has_already_been_added:
                    pass  # Ignore
                elif parent_of_parent in pn_ids:
                    pass  # Ignore
                else:
                    sorted_view_model.append(parent_widget_model)
                    already_inserted_widget_id.add(parent_id)
                    already_inserted_pair.add((parent_of_parent, parent_id))

                widget_models = parent_id_to_children_widget_models.get(parent_id, ())
                for widget_model in widget_models:
                    parent_id = widget_model[0]
                    widget_id = widget_model[1]

                    if widget_id in pn_ids:
                        pn_id = widget_id
                        options: dict = widget_id_to_widget_model[pn_id][-1]
                        frame_ids = options['frame_ids']
                        list_of_frame_options = [frame_id_to_frame_options[frame_id] for frame_id in frame_ids]
                        additional_options = {'frame_options': list_of_frame_options, }
                        options.update(additional_options)
                        widget_model = widget_model[:-1] + (options,)

                    sorted_view_model.append(widget_model)
                    already_inserted_widget_id.add(parent_id)
                    already_inserted_pair.add((parent_id, widget_id))

    return sorted_view_model
