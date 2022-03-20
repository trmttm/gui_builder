from view_tkinter import View

from stacker import Stacker
from stacker import widgets as w

paned_window_01 = 'paned_window_01'

# Widget ID
btn_001 = 'btn_001'
btn_002 = 'btn_002'
btn_003 = 'btn_003'
btn_004 = 'btn_004'
btn_005 = 'btn_005'
btn_006 = 'btn_006'
btn_007 = 'btn_007'
btn_action_01 = 'btn_action_01'
btn_action_02_01 = 'btn_action_02_01'
btn_action_02_02 = 'btn_action_02_02'
btn_action_03_01 = 'btn_action_03_01'
btn_action_03_02 = 'btn_action_03_02'
btn_action_03_03 = 'btn_action_03_03'
btn_action_04_01 = 'btn_action_04_01'
btn_action_04_02 = 'btn_action_04_02'
btn_action_04_03 = 'btn_action_04_03'
btn_action_05 = 'btn_action_05'
btn_action_06_01 = 'btn_action_06_01'
btn_action_06_02 = 'btn_action_06_02'
btn_action_06_03 = 'btn_action_06_03'
btn_cmd_list1 = 'btn_cmd_list1'
btn_cmd_list2 = 'btn_cmd_list2'
btn_cmd_list3 = 'btn_cmd_list3'
btn_action_07 = 'btn_action_07'

frame_switcher_input = 'frame_switcher_input'

label_input_add_module = 'label_input_add_module'
label_input_configure_account_01 = 'label_input_configure_account_01'
label_input_configure_account_02 = 'label_input_configure_account_02'
label_input_configure_account_03 = 'label_input_configure_account_03'
label_input_configure_account_04 = 'label_input_configure_account_04'
label_input_configure_account_05 = 'label_input_configure_account_05'
label_input_configure_account_06 = 'label_input_configure_account_05'
label_input_add_relay_01 = 'label_input_add_relay_01'
label_input_add_relay_02 = 'label_input_add_relay_02'
label_input_add_relay_03 = 'label_input_add_relay_03'
label_input_add_relay_04 = 'label_input_add_relay_04'
label_input_add_relay_05 = 'label_input_add_relay_05'
label_input_connect_shape_01 = 'label_input_connect_shape_01'
label_input_connect_shape_02 = 'label_input_connect_shape_02'
label_input_connect_shape_03 = 'label_input_connect_shape_03'
label_input_import_module = 'label_input_import_module'
label_edit_dictionary_01 = 'label_edit_dictionary_01'
label_edit_dictionary_02 = 'label_edit_dictionary_02'
label_edit_dictionary_03 = 'label_edit_dictionary_03'
label_set_sheet_name_01 = 'label_set_sheet_name_01'
label_set_sheet_name_02 = 'label_set_sheet_name_02'
label_set_sheet_name_03 = 'label_set_sheet_name_03'
label_commands_list = 'macro'

entry_input_add_module = 'entry_input_add_module'
entry_input_configure_account_01 = 'entry_input_configure_account_01'
entry_input_configure_account_02 = 'entry_input_configure_account_02'
entry_input_configure_account_03 = 'entry_input_configure_account_03'
entry_input_configure_account_04 = 'entry_input_configure_account_04'
entry_input_configure_account_05 = 'entry_input_configure_account_05'
entry_input_configure_account_06 = 'entry_input_configure_account_06'
entry_input_add_relay_01 = 'entry_input_add_relay_01'
entry_input_add_relay_02 = 'entry_input_add_relay_02'
entry_input_add_relay_03 = 'entry_input_add_relay_03'
entry_input_add_relay_04 = 'entry_input_add_relay_04'
entry_input_add_relay_05 = 'entry_input_add_relay_05'
entry_input_connect_shape_01 = 'entry_input_connect_shape_01'
entry_input_connect_shape_02 = 'entry_input_connect_shape_02'
entry_input_connect_shape_03 = 'entry_input_connect_shape_03'
entry_input_import_module = 'entry_input_import_module'
entry_edit_dictionary_01 = 'entry_edit_dictionary_01'
entry_edit_dictionary_02 = 'entry_edit_dictionary_02'

tree_macro = 'tree_macro'
tree_action_01 = 'tree_action_01'
tree_action_02 = 'tree_action_02'
tree_action_03_01 = 'tree_action_03__01'
tree_action_03_02 = 'tree_action_03_02'
tree_action_04 = 'tree_action_04'
tree_action_05 = 'tree_action_05'
tree_action_06 = 'tree_action_06'

btn_macro_list_padding = 10, 5
input_frames = []

text_btn001 = 'Add Template'
text_btn002 = 'Configure Account'
text_btn003 = 'Add Relay'
text_btn004 = 'Connect Shapes'
text_btn005 = 'Import Macro'
text_btn006 = 'Dictionary'
text_btn007 = 'Set Sheet Name'
text_btn_cmd_list1 = '-'
text_btn_cmd_list2 = 'Execute'
text_btn_cmd_list3 = 'Save'
btn_action_01_text = 'Add Module'
btn_action_02_01_text = 'Select Account'
btn_action_02_02_text = 'Configure Account'
btn_action_03_text_01 = 'Pick Module'
btn_action_03_text_02 = 'Pick Account'
btn_action_03_text_03 = 'Add Relay'
btn_action_04_text_01 = 'Pick Account From'
btn_action_04_text_02 = 'Pick Account To'
btn_action_04_text_03 = 'Connect Shapes'
btn_action_05_text = 'Import Macro'
btn_action_06_01_text = '+'
btn_action_06_02_text = '-'
btn_action_06_03_text = 'edit'
btn_action_07_text = 'Set Sheet Name'

text_input_add_module = 'Module Name'
text_input_configure_account_01 = 'Account Name'
text_input_configure_account_02 = ''
text_input_configure_account_03 = 'Account'
text_input_configure_account_04 = 'X'
text_input_configure_account_05 = 'Y'
text_input_configure_account_06 = 'Width'
text_input_add_relay_01 = 'Module Name'
text_input_add_relay_02 = 'Account Name'
text_input_add_relay_03 = ''
text_input_add_relay_04 = 'Module'
text_input_add_relay_05 = 'Account'
text_input_connect_shape_01 = 'Connect Shapes'
text_input_connect_shape_02 = 'From'
text_input_connect_shape_03 = 'To'
text_input_import_module = 'Import Macro'
text_edit_dictionary_01 = 'Dictionary'
text_edit_dictionary_02 = 'Key'
text_edit_dictionary_03 = 'Value'
text_label_commands_list = 'Macro Commands'
text_set_sheet_name_01 = 'Set Sheet Name'
text_set_sheet_name_02 = 'Current'
text_set_sheet_name_03 = 'New'


def action_buttons(stacker: Stacker):
    btn_padding = 0, 10, 10, 0
    return stacker.vstack(
        w.Label('label_actions').text('Actions'),
        w.Button(btn_001).text(text_btn001).wh_padding(*btn_padding),
        w.Button(btn_002).text(text_btn002).wh_padding(*btn_padding),
        w.Button(btn_003).text(text_btn003).wh_padding(*btn_padding),
        w.Button(btn_004).text(text_btn004).wh_padding(*btn_padding),
        w.Button(btn_005).text(text_btn005).wh_padding(*btn_padding),
        w.Button(btn_006).text(text_btn006).wh_padding(*btn_padding),
        w.Button(btn_007).text(text_btn007).wh_padding(*btn_padding),
        w.Spacer(),
    )


def input_frame_switcher(stacker: Stacker):
    return w.FrameSwitcher(frame_switcher_input, stacker, input_frames).stackers(
        input_add_module(stacker),
        input_configure_account(stacker),
        add_relay(stacker),
        connect_shapes(stacker),
        import_macro(stacker),
        edit_dictionary(stacker),
        set_sheet_name(stacker),
    )


def input_add_module(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label(label_input_add_module).text(text_input_add_module),
            w.Entry(entry_input_add_module),
        ),
        w.TreeView(tree_action_01),
        w.Button(btn_action_01).text(btn_action_01_text),
        w.Spacer(),
    )


def input_configure_account(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label(label_input_configure_account_01).text(text_input_configure_account_01),
            w.Entry(entry_input_configure_account_01),
        ),
        w.TreeView(tree_action_02),
        w.Button(btn_action_02_01).text(btn_action_02_01_text),
        w.Label(label_input_configure_account_02).text(text_input_configure_account_02),
        stacker.hstack(
            w.Label(label_input_configure_account_03).text(text_input_configure_account_03),
            w.Entry(entry_input_configure_account_03),
        ),
        stacker.hstack(
            w.Label(label_input_configure_account_04).text(text_input_configure_account_04),
            w.Entry(entry_input_configure_account_04),
        ),
        stacker.hstack(
            w.Label(label_input_configure_account_05).text(text_input_configure_account_05),
            w.Entry(entry_input_configure_account_05),
        ),
        stacker.hstack(
            w.Label(label_input_configure_account_06).text(text_input_configure_account_06),
            w.Entry(entry_input_configure_account_06),
        ),
        w.Button(btn_action_02_02).text(btn_action_02_02_text),
        w.Spacer(),
    )


def add_relay(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label(label_input_add_relay_01).text(text_input_add_relay_01),
            w.Entry(entry_input_add_relay_01),
        ),
        w.TreeView(tree_action_03_01),
        w.Button(btn_action_03_01).text(btn_action_03_text_01),
        stacker.hstack(
            w.Label(label_input_add_relay_02).text(text_input_add_relay_02),
            w.Entry(entry_input_add_relay_02),
        ),
        w.TreeView(tree_action_03_02),
        w.Button(btn_action_03_02).text(btn_action_03_text_02),
        w.Label(label_input_add_relay_03).text(text_input_add_relay_03),
        stacker.hstack(
            w.Label(label_input_add_relay_04).text(text_input_add_relay_04),
            w.Entry(entry_input_add_relay_04),
        ),
        stacker.hstack(
            w.Label(label_input_add_relay_05).text(text_input_add_relay_05),
            w.Entry(entry_input_add_relay_05),
        ),
        w.Button(btn_action_03_03).text(btn_action_03_text_03),
        w.Spacer(),
    )


def connect_shapes(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label(label_input_connect_shape_01).text(text_input_connect_shape_01),
            w.Entry(entry_input_connect_shape_01),
        ),
        w.TreeView(tree_action_04),
        stacker.hstack(
            w.Button(btn_action_04_01).text(btn_action_04_text_01),
            w.Button(btn_action_04_02).text(btn_action_04_text_02),
            w.Spacer().adjust(-2),
            w.Spacer().adjust(-2),
        ),
        stacker.hstack(
            w.Label(label_input_connect_shape_02).text(text_input_connect_shape_02),
            w.Entry(entry_input_connect_shape_02),
        ),
        stacker.hstack(
            w.Label(label_input_connect_shape_03).text(text_input_connect_shape_03),
            w.Entry(entry_input_connect_shape_03),
        ),
        w.Button(btn_action_04_03).text(btn_action_04_text_03),
        w.Spacer(),
    )


def import_macro(stacker: Stacker):
    return stacker.vstack(
        stacker.hstack(
            w.Label(label_input_import_module).text(text_input_import_module),
            w.Entry(entry_input_import_module),
        ),
        w.TreeView(tree_action_05),
        w.Button(btn_action_05).text(btn_action_05_text),
        w.Spacer(),
    )


def edit_dictionary(stacker: Stacker):
    return stacker.vstack(
        w.Label(label_edit_dictionary_01).text(text_edit_dictionary_01),
        w.TreeView(tree_action_06),
        stacker.hstack(
            w.Label(label_edit_dictionary_02).text(text_edit_dictionary_02),
            w.Entry(entry_edit_dictionary_01),
        ),
        stacker.hstack(
            w.Label(label_edit_dictionary_03).text(text_edit_dictionary_03),
            w.Entry(entry_edit_dictionary_02),
        ),
        stacker.hstack(
            w.Button(btn_action_06_01).text(btn_action_06_01_text),
            w.Button(btn_action_06_02).text(btn_action_06_02_text),
            w.Button(btn_action_06_03).text(btn_action_06_03_text),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-3),
            w.Spacer().adjust(-3),
        ),
        w.Spacer(),
    )


def set_sheet_name(stacker: Stacker):
    return stacker.vstack(
        w.Label(label_set_sheet_name_01).text(text_set_sheet_name_01),
        stacker.hstack(
            w.Label(label_set_sheet_name_02).text(text_set_sheet_name_02),
            w.Entry(entry_edit_dictionary_01),
        ),
        stacker.hstack(
            w.Label(label_set_sheet_name_03).text(text_set_sheet_name_03),
            w.Entry(entry_edit_dictionary_02),
        ),
        w.Button(btn_action_07).text(btn_action_07_text),
        w.Spacer(),
    )


def frame_macro_list(stacker: Stacker):
    return stacker.vstack(
        w.Label(label_commands_list).text(text_label_commands_list),
        w.TreeView(tree_macro).padding(10, 0),
        macro_commands_buttons(stacker),
        w.Spacer().adjust(-2),
    )


def macro_commands_buttons(stacker: Stacker):
    return stacker.hstack(
        w.Button(btn_cmd_list1).text(text_btn_cmd_list1).padding(*btn_macro_list_padding).wh_padding(
            *btn_pad),
        w.Spacer(),
        w.Button(btn_cmd_list2).text(text_btn_cmd_list2).padding(*btn_macro_list_padding).wh_padding(
            *btn_pad),
        w.Button(btn_cmd_list3).text(text_btn_cmd_list3).padding(*btn_macro_list_padding).wh_padding(
            *btn_pad),
    )


btn_pad = (0, 10, 10, 0)


def main(stacker: Stacker):
    return stacker.hstack(
        w.PanedWindow(paned_window_01, stacker).is_horizontal().weights((0, 0, 1)).stackers(
            action_buttons(stacker),
            input_frame_switcher(stacker),
            frame_macro_list(stacker),
        )
    )


if __name__ == '__main__':
    import pickle

    save_pickle = False
    load_pickle = False
    launch_app = False

    stacker = Stacker()
    main(stacker)

    view_model = stacker.view_model

    if launch_app:
        app = View()
        app.add_widgets(view_model)
        app.launch_app()

    if save_pickle:
        with open('gui_macro_builder', 'wb') as file:
            pickle.dump(view_model, file, protocol=pickle.HIGHEST_PROTOCOL)

    if load_pickle:
        pickle_path = '/Users/yamaka/Documents/GitHub/gui_builder/Tests/macro_builder/gui_macro_builder'
        with open(pickle_path, 'rb') as f:
            view_model_from_pickle = pickle.load(f)

        print(view_model == view_model_from_pickle)
