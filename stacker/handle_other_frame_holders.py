def sort_view_model_for_paned_window(view_model: list) -> list:
    """
    1) PanedWindow and Notebook (PN, pn) widget model must be placed right after its parent frame_id
    2) PanedWindow and Notebook's children frames are automatically created,
    3) but we need to pass their frame_options in order to properly configure row and column.
    """
    # Preparation 1
    pn_ids = []
    pn_parents = set()
    frame_id_to_frame_options = {}
    widget_id_to_widget_model = {}
    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]
        widget_type = widget_model[2]

        widget_id_to_widget_model[widget_id] = widget_model

        if widget_type in ['paned_window', 'notebook']:
            pn_ids.append(widget_id)
            pn_parents.add(parent_id)

        if widget_type == 'frame':
            frame_options: dict = widget_model[-1]['frame options']  # this logic looks so easy to break...
            frame_id_to_frame_options[widget_id] = frame_options

    # Preparation 2
    all_pn_children = []
    pn_parent_to_pn_id = {}
    pn_id_to_children_frames = {}
    for widget_model in view_model:
        parent_id = widget_model[0]
        widget_id = widget_model[1]
        if parent_id in pn_ids:
            pn_child_frame_id = widget_id
            pn_id = parent_id

            all_pn_children.append(pn_child_frame_id)

            if pn_id in pn_id_to_children_frames:
                pn_id_to_children_frames[pn_id].append(pn_child_frame_id)
            else:
                pn_id_to_children_frames[pn_id] = [pn_child_frame_id]
        if widget_id in pn_ids:
            pn_id = widget_id
            if parent_id in pn_parent_to_pn_id:
                pn_parent_to_pn_id[parent_id].append(pn_id)
            else:
                pn_parent_to_pn_id[parent_id] = [pn_id]

    # Sorting view_model
    if pn_ids:
        sorted_viewed_model = []

        for widget_model in view_model:
            widget_id = widget_model[1]
            if widget_id not in pn_ids + all_pn_children:  # Ignore PanedWindows and their children
                sorted_viewed_model.append(widget_model)
            if widget_id in pn_parents:
                parent_of_pn = widget_id

                children_pn_ids = pn_parent_to_pn_id[parent_of_pn]
                # Add children frame options
                for pn_id in children_pn_ids:
                    list_of_frame_options = []
                    for pn_child_frame in pn_id_to_children_frames[pn_id]:
                        list_of_frame_options.append(frame_id_to_frame_options[pn_child_frame])

                    pn_widget_model = widget_id_to_widget_model[pn_id]
                    options: dict = pn_widget_model[-1]
                    additional_options = {'frame_options': list_of_frame_options, }
                    options.update(additional_options)
                    pw_widget_model_frame_options_added = pn_widget_model[:-1] + (options,)

                    sorted_viewed_model.append(pw_widget_model_frame_options_added)
    else:
        sorted_viewed_model = view_model
    return sorted_viewed_model
