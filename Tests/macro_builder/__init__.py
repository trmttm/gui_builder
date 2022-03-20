from view_tkinter import View

from stacker import Stacker
from stacker import widgets as w


class MacroBuilder:
    def __init__(self, widget_data: dict):
        self._stacker = Stacker()
        self._widget_ids = widget_data['ids']
        self._widget_id_to_text = widget_data['texts']
        self._view_model = None

    @property
    def view_model(self) -> list:
        if self._view_model:
            return self._view_model
        else:
            self._main()
            return self._stacker.view_model

    def _action_buttons(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        btn_padding = 0, 10, 10, 0

        return self._stacker.vstack(
            w.Label('label_actions').text('Actions'),
            w.Button(f('btn_001')).text(t('text_btn001')).wh_padding(*btn_padding),
            w.Button(f('btn_002')).text(t('text_btn002')).wh_padding(*btn_padding),
            w.Button(f('btn_003')).text(t('text_btn003')).wh_padding(*btn_padding),
            w.Button(f('btn_004')).text(t('text_btn004')).wh_padding(*btn_padding),
            w.Button(f('btn_005')).text(t('text_btn005')).wh_padding(*btn_padding),
            w.Button(f('btn_006')).text(t('text_btn006')).wh_padding(*btn_padding),
            w.Button(f('btn_007')).text(t('text_btn007')).wh_padding(*btn_padding),
            w.Spacer(),
        )

    def _input_frame_switcher(self):
        f = self._widget_ids.get
        stacker = self._stacker
        return w.FrameSwitcher(f('frame_switcher_input'), stacker, input_frames).stackers(
            self._input_add_module(),
            self._input_configure_account(),
            self._add_relay(),
            self._connect_shapes(),
            self._import_macro(),
            self._edit_dictionary(),
            self._set_sheet_name(),
        )

    def _input_add_module(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            stacker.hstack(
                w.Label(f('label_input_add_module')).text(t('text_input_add_module')),
                w.Entry(f('entry_input_add_module')),
            ),
            stacker.vstack(
                w.TreeView(f('tree_action_01')),
            ),
            w.Button(f('btn_action_01')).text(t('text_btn_action_01')),
            w.Spacer(),
        )

    def _input_configure_account(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker

        return stacker.vstack(
            stacker.hstack(
                w.Label(f('label_input_configure_account_01')).text(t('text_input_configure_account_01')),
                w.Entry(f('entry_input_configure_account_01')),
            ),
            w.TreeView(f('tree_action_02')),
            w.Button(f('btn_action_02_01')).text(t('text_btn_action_02_01')),
            w.Label(f('label_input_configure_account_02')).text(t('text_input_configure_account_02')),
            stacker.hstack(
                w.Label(f('label_input_configure_account_03')).text(t('text_input_configure_account_03')),
                w.Entry(f('entry_input_configure_account_03')),
            ),
            stacker.hstack(
                w.Label(f('label_input_configure_account_04')).text(t('text_input_configure_account_04')),
                w.Entry(f('entry_input_configure_account_04')),
            ),
            stacker.hstack(
                w.Label(f('label_input_configure_account_05')).text(t('text_input_configure_account_05')),
                w.Entry(f('entry_input_configure_account_05')),
            ),
            stacker.hstack(
                w.Label(f('label_input_configure_account_06')).text(t('text_input_configure_account_06')),
                w.Entry(f('entry_input_configure_account_06')),
            ),
            w.Button(f('btn_action_02_02')).text(t('text_btn_action_02_02')),
            w.Spacer(),
        )

    def _add_relay(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            # Pick Account
            stacker.hstack(
                w.Label(f('label_input_add_relay_02')).text(t('text_input_add_relay_02')),
                w.Entry(f('entry_input_add_relay_02')),
            ),
            w.TreeView(f('tree_action_03_02')),
            w.Button(f('btn_action_03_02')).text(t('text_btn_action_03_02')),

            # Target Module
            stacker.hstack(
                w.Label(f('label_input_add_relay_01')).text(t('text_input_add_relay_01')),
                w.Entry(f('entry_input_add_relay_01')),
            ),
            w.TreeView(f('tree_action_03_01')),
            w.Button(f('btn_action_03_01')).text(t('text_btn_action_03_01')),

            w.Label(f('label_input_add_relay_03')).text(t('text_input_add_relay_03')),
            stacker.hstack(
                w.Label(f('label_input_add_relay_04')).text(t('text_input_add_relay_04')),
                w.Entry(f('entry_input_add_relay_04')),
            ),

            # Entries and Execute Button
            stacker.hstack(
                w.Label(f('label_input_add_relay_05')).text(t('text_input_add_relay_05')),
                w.Entry(f('entry_input_add_relay_05')),
            ),
            w.Button(f('btn_action_03_03')).text(t('text_btn_action_03_03')),
            w.Spacer(),
        )

    def _connect_shapes(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            stacker.hstack(
                w.Label(f('label_input_connect_shape_01')).text(t('text_input_connect_shape_01')),
                w.Entry(f('entry_input_connect_shape_01')),
            ),
            w.TreeView(f('tree_action_04')),
            stacker.hstack(
                w.Button(f('btn_action_04_01')).text(t('text_btn_action_04_01')),
                w.Button(f('btn_action_04_02')).text(t('text_btn_action_04_02')),
                w.Spacer().adjust(-2),
                w.Spacer().adjust(-2),
            ),
            stacker.hstack(
                w.Label(f('label_input_connect_shape_02')).text(t('text_input_connect_shape_02')),
                w.Entry(f('entry_input_connect_shape_02')),
            ),
            stacker.hstack(
                w.Label(f('label_input_connect_shape_03')).text(t('text_input_connect_shape_03')),
                w.Entry(f('entry_input_connect_shape_03')),
            ),
            w.Button(f('btn_action_04_03')).text(t('text_btn_action_04_03')),
            w.Spacer(),
        )

    def _import_macro(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            stacker.hstack(
                w.Label(f('label_input_import_module')).text(t('text_input_import_module')),
                w.Entry(f('entry_input_import_module')),
            ),
            w.TreeView(f('tree_action_05')),
            w.Button(f('btn_action_05')).text(t('text_btn_action_05')),
            w.Spacer(),
        )

    def _edit_dictionary(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            w.Label(f('label_edit_dictionary_01')).text(t('text_edit_dictionary_01')),
            w.TreeView(f('tree_action_06')),
            stacker.hstack(
                w.Label(f('label_edit_dictionary_02')).text(t('text_edit_dictionary_02')),
                w.Entry(f('entry_edit_dictionary_01')),
            ),
            stacker.hstack(
                w.Label(f('label_edit_dictionary_03')).text(t('text_edit_dictionary_03')),
                w.Entry(f('entry_edit_dictionary_02')),
            ),
            stacker.hstack(
                w.Button(f('btn_action_06_01')).text(t('text_btn_action_06_01')),
                w.Button(f('btn_action_06_02')).text(t('text_btn_action_06_02')),
                w.Button(f('btn_action_06_03')).text(t('text_btn_action_06_03')),
                w.Spacer().adjust(-3),
                w.Spacer().adjust(-3),
                w.Spacer().adjust(-3),
            ),
            w.Spacer(),
        )

    def _set_sheet_name(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            w.Label(f('label_set_sheet_name_01')).text(t('text_set_sheet_name_01')),
            stacker.hstack(
                w.Label(f('label_set_sheet_name_02')).text(t('text_set_sheet_name_02')),
                w.Entry(f('entry_edit_dictionary_01')),
            ),
            stacker.hstack(
                w.Label(f('label_set_sheet_name_03')).text(t('text_set_sheet_name_03')),
                w.Entry(f('entry_edit_dictionary_02')),
            ),
            w.Button(f('btn_action_07')).text(t('text_btn_action_07')),
            w.Spacer(),
        )

    def _frame_macro_list(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        return stacker.vstack(
            w.Label(f('label_commands_list')).text(t('text_label_commands_list')),
            w.TreeView(f('tree_macro')).padding(10, 0),
            self._macro_commands_buttons(),
            w.Spacer().adjust(-2),
        )

    def _macro_commands_buttons(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker
        btn_pad = 0, 10, 10, 0
        btn_macro_padding = 10,5
        return stacker.hstack(
            w.Button(f('btn_cmd_list1')).text(t('text_btn_cmd_list1')).padding(*btn_macro_padding).wh_padding(*btn_pad),
            w.Spacer(),
            w.Button(f('btn_cmd_list2')).text(t('text_btn_cmd_list2')).padding(*btn_macro_padding).wh_padding(*btn_pad),
            w.Button(f('btn_cmd_list3')).text(t('text_btn_cmd_list3')).padding(*btn_macro_padding).wh_padding(*btn_pad),
        )

    def _main(self):
        f = self._widget_ids.get
        t = self._widget_id_to_text.get
        stacker = self._stacker

        return stacker.hstack(
            w.PanedWindow(f('paned_window_01'), stacker).is_horizontal().weights((0, 0, 1)).stackers(
                self._action_buttons(),
                self._input_frame_switcher(),
                self._frame_macro_list(),
            )
        )


if __name__ == '__main__':
    input_frames = []
    widget_data = {
        'ids': {'paned_window_01': 'paned_window_01',

                'btn_001': 'btn_001',
                'btn_002': 'btn_002',
                'btn_003': 'btn_003',
                'btn_004': 'btn_004',
                'btn_005': 'btn_005',
                'btn_006': 'btn_006',
                'btn_007': 'btn_007',
                'btn_action_01': 'btn_action_01',
                'btn_action_02_01': 'btn_action_02_01',
                'btn_action_02_02': 'btn_action_02_02',
                'btn_action_03_01': 'btn_action_03_01',
                'btn_action_03_02': 'btn_action_03_02',
                'btn_action_03_03': 'btn_action_03_03',
                'btn_action_04_01': 'btn_action_04_01',
                'btn_action_04_02': 'btn_action_04_02',
                'btn_action_04_03': 'btn_action_04_03',
                'btn_action_05': 'btn_action_05',
                'btn_action_06_01': 'btn_action_06_01',
                'btn_action_06_02': 'btn_action_06_02',
                'btn_action_06_03': 'btn_action_06_03',
                'btn_cmd_list1': 'btn_cmd_list1',
                'btn_cmd_list2': 'btn_cmd_list2',
                'btn_cmd_list3': 'btn_cmd_list3',
                'btn_action_07': 'btn_action_07',

                'frame_switcher_input': 'frame_switcher_input',

                'label_input_add_module': 'label_input_add_module',
                'label_input_configure_account_01': 'label_input_configure_account_01',
                'label_input_configure_account_02': 'label_input_configure_account_02',
                'label_input_configure_account_03': 'label_input_configure_account_03',
                'label_input_configure_account_04': 'label_input_configure_account_04',
                'label_input_configure_account_05': 'label_input_configure_account_05',
                'label_input_add_relay_01': 'label_input_add_relay_01',
                'label_input_add_relay_02': 'label_input_add_relay_02',
                'label_input_add_relay_03': 'label_input_add_relay_03',
                'label_input_add_relay_04': 'label_input_add_relay_04',
                'label_input_add_relay_05': 'label_input_add_relay_05',
                'label_input_connect_shape_01': 'label_input_connect_shape_01',
                'label_input_connect_shape_02': 'label_input_connect_shape_02',
                'label_input_connect_shape_03': 'label_input_connect_shape_03',
                'label_input_import_module': 'label_input_import_module',
                'label_edit_dictionary_01': 'label_edit_dictionary_01',
                'label_edit_dictionary_02': 'label_edit_dictionary_02',
                'label_edit_dictionary_03': 'label_edit_dictionary_03',
                'label_set_sheet_name_01': 'label_set_sheet_name_01',
                'label_set_sheet_name_02': 'label_set_sheet_name_02',
                'label_set_sheet_name_03': 'label_set_sheet_name_03',
                'macro': 'macro',

                'entry_input_add_module': 'entry_input_add_module',
                'entry_input_configure_account_01': 'entry_input_configure_account_01',
                'entry_input_configure_account_02': 'entry_input_configure_account_02',
                'entry_input_configure_account_03': 'entry_input_configure_account_03',
                'entry_input_configure_account_04': 'entry_input_configure_account_04',
                'entry_input_configure_account_05': 'entry_input_configure_account_05',
                'entry_input_configure_account_06': 'entry_input_configure_account_06',
                'entry_input_add_relay_01': 'entry_input_add_relay_01',
                'entry_input_add_relay_02': 'entry_input_add_relay_02',
                'entry_input_add_relay_03': 'entry_input_add_relay_03',
                'entry_input_add_relay_04': 'entry_input_add_relay_04',
                'entry_input_add_relay_05': 'entry_input_add_relay_05',
                'entry_input_connect_shape_01': 'entry_input_connect_shape_01',
                'entry_input_connect_shape_02': 'entry_input_connect_shape_02',
                'entry_input_connect_shape_03': 'entry_input_connect_shape_03',
                'entry_input_import_module': 'entry_input_import_module',
                'entry_edit_dictionary_01': 'entry_edit_dictionary_01',
                'entry_edit_dictionary_02': 'entry_edit_dictionary_02',

                'tree_macro': 'tree_macro',
                'tree_action_01': 'tree_action_01',
                'tree_action_02': 'tree_action_02',
                'tree_action_03__01': 'tree_action_03__01',
                'tree_action_03_02': 'tree_action_03_02',
                'tree_action_04': 'tree_action_04',
                'tree_action_05': 'tree_action_05',
                'tree_action_06': 'tree_action_06', },
        'texts': {
            'text_btn001': 'Add Template',
            'text_btn002': 'Configure Account',
            'text_btn003': 'Add Relay',
            'text_btn004': 'Connect Shapes',
            'text_btn005': 'Import Macro',
            'text_btn006': 'Dictionary',
            'text_btn007': 'Set Sheet Name',
            'text_btn_cmd_list1': '-',
            'text_btn_cmd_list2': 'Execute',
            'text_btn_cmd_list3': 'Save',
            'text_btn_action_01': 'Add Module',
            'text_btn_action_02_01': 'Select Account',
            'text_btn_action_02_02': 'Configure Account',
            'text_btn_action_03_01': 'Pick Module',
            'text_btn_action_03_02': 'Pick Account',
            'text_btn_action_03_03': 'Add Relay',
            'text_btn_action_04_01': 'Pick Account From',
            'text_btn_action_04_02': 'Pick Account To',
            'text_btn_action_04_03': 'Connect Shapes',
            'text_btn_action_05': 'Import Macro',
            'text_btn_action_06_01': '+',
            'text_btn_action_06_02': '-',
            'text_btn_action_06_03': 'edit',
            'text_btn_action_07': 'Set Sheet Name',
            'text_input_add_module': 'Module Name',
            'text_input_configure_account_01': 'Account Name',
            'text_input_configure_account_02': '',
            'text_input_configure_account_03': 'Account',
            'text_input_configure_account_04': 'X',
            'text_input_configure_account_05': 'Y',
            'text_input_configure_account_06': 'Width',
            'text_input_add_relay_01': 'Destination Module',
            'text_input_add_relay_02': 'Account Name',
            'text_input_add_relay_03': '',
            'text_input_add_relay_04': 'Module',
            'text_input_add_relay_05': 'Account',
            'text_input_connect_shape_01': 'Connect Shapes',
            'text_input_connect_shape_02': 'From',
            'text_input_connect_shape_03': 'To',
            'text_input_import_module': 'Import Macro',
            'text_edit_dictionary_01': 'Dictionary',
            'text_edit_dictionary_02': 'Key',
            'text_edit_dictionary_03': 'Value',
            'text_label_commands_list': 'Macro Commands',
            'text_set_sheet_name_01': 'Set Sheet Name',
            'text_set_sheet_name_02': 'Current',
            'text_set_sheet_name_03': 'New',
        },
    }
    import pickle

    save_pickle = True
    load_pickle = False
    launch_app = False

    macro_builder = MacroBuilder(widget_data)
    view_model = macro_builder.view_model

    if launch_app:
        app = View()
        app.add_widgets(view_model)
        app.launch_app()

    if save_pickle:
        with open('gui_macro_builder', 'wb') as file:
            pickle.dump(view_model, file, protocol=pickle.HIGHEST_PROTOCOL)
        with open('switchable_frames', 'wb') as file:
            pickle.dump(input_frames, file, protocol=pickle.HIGHEST_PROTOCOL)

        with open('widget_ids', 'wb') as file:
            pickle.dump(widget_data, file, protocol=pickle.HIGHEST_PROTOCOL)

        print('Pickled successfully')
        print(f'input_frame = {input_frames}')

    if load_pickle:
        pickle_path = '/Users/yamaka/Documents/GitHub/gui_builder/Tests/macro_builder/gui_macro_builder'
        with open(pickle_path, 'rb') as f:
            view_model_from_pickle = pickle.load(f)

        print(view_model == view_model_from_pickle)
