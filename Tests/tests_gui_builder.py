import unittest


def launch_app(view_model):
    from view_tkinter import View
    app = View()
    app.add_widgets(view_model)
    app.launch_app()


def label_entry(stacker, w, label_id, entry_id, label_text, ):
    return stacker.hstack(
        w.Label(label_id).text(label_text).padding(5, 0).align('w').width(6),
        w.Entry(entry_id).padding(5, 0),
        w.Spacer().adjust(-1),
    )


class MyTestCase(unittest.TestCase):
    def test_vstacker(self):
        from Tests.concepts import vstacker
        from stacker.widgets import Button
        from stacker.widgets import Entry
        from stacker.widgets import Label
        from stacker.widgets import Spacer

        view_model = vstacker(
            Label('label_1').text('Name:').width(10),
            Entry('entry_1').default_value('Name').width(20),
            Button('button_1').text('Name').command(lambda: print('button pushed!')).width(15),
            Spacer(),
        )

        launch_app(view_model)

    def test_hstacker(self):
        from Tests.concepts import hstacker
        from stacker.widgets import Button
        from stacker.widgets import Entry
        from stacker.widgets import Label
        from stacker.widgets import Spacer

        view_model = hstacker(
            Label('label_1').text('Name:').width(10),
            Entry('entry_1').default_value('Name').width(20),
            Button('button_1').text('Name').command(lambda: print('button pushed!')).width(15),
            Spacer(),
        )

        launch_app(view_model)

    def test_combination_of_vstacker_and_hstacker(self):
        from stacker import Stacker
        from stacker.widgets import Button
        from stacker.widgets import Entry
        from stacker.widgets import Label
        from stacker.widgets import Spacer

        stacker = Stacker()

        stacker.hstack(
            Spacer(),
            stacker.vstack(
                Spacer(),
                stacker.hstack(
                    Label('label_0').text('Name1').width(10),
                    Entry('entry_0').default_value('First Last1').width(15),
                    Button('button_0').text('Add1').width(10).command(lambda: print('Pushed1'))
                ),
                stacker.hstack(
                    Label('label_1').text('Name2').width(10),
                    Entry('entry_1').default_value('First Last2').width(15),
                    Button('button_1').text('Add2').width(10).command(lambda: print('Pushed2'))
                ),
                stacker.hstack(
                    Label('label_2').text('Name3').width(10),
                    Entry('entry_2').default_value('First Last3').width(15),
                    Button('button_2').text('Add3').width(10).command(lambda: print('Pushed3'))
                ),
                Spacer(),
            ),
            stacker.vstack(
                Spacer(),
                stacker.hstack(
                    Label('label_3').text('Name a').width(10),
                    Entry('entry_3').default_value('First Last a').width(15),
                    Button('button_3').text('Add a').width(10).command(lambda: print('pushed a'))
                ),
                stacker.hstack(
                    Label('label_4').text('Name b').width(10),
                    Entry('entry_4').default_value('First Last b').width(15),
                    Button('button_4').text('Add b').width(10).command(lambda: print('pushed b'))
                ),
                stacker.hstack(
                    Label('label_5').text('Name c').width(10),
                    Entry('entry_5').default_value('First Last c').width(15),
                    Button('button_5').text('Add c').width(10).command(lambda: print('pushed c'))
                ),
                Spacer(),
            ),
            Spacer(),
        )

        launch_app(stacker.view_model)

    def test_paned_window(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.hstack(
            w.PanedWindow('paned_window1', stacker).is_horizontal().stackers(
                stacker.hstack(
                    stacker.vstack(
                        w.Label('label1').text('Label1'),
                        w.Button('button1').text('Button1').command(lambda: print('button1')),
                        w.Spacer(),
                    ),
                    w.Spacer(),
                ),
                stacker.vstack(
                    stacker.hstack(
                        w.Label('label2').text('Label2'),
                        w.Button('button2').text('Button2').command(lambda: print('button2')),
                        w.Spacer(),
                    ),
                    w.Spacer(),
                ),
            ),
        )
        launch_app(stacker.view_model)

    def test_canvas(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.hstack(
            w.PanedWindow('paned_window1', stacker).is_horizontal().weights((1, 8)).stackers(
                stacker.vstack(
                    stacker.hstack(
                        w.Label('label1').text('Label1'),
                        w.Button('button1').text('Button1').command(lambda: print('button1')).width(10),
                    ),
                    stacker.hstack(
                        w.Label('label2').text('Label2'),
                        w.Button('button2').text('Button2').command(lambda: print('button2')).width(10),
                    ),
                    stacker.hstack(
                        w.Label('label3').text('Label3'),
                        w.Button('button3').text('Button3').command(lambda: print('button3')).width(10),
                    ),
                    w.Spacer(),
                    w.Button('button4').text('Button4').command(lambda: print('button4')).width(10),
                ),
                stacker.vstack(
                    w.Canvas('canvas').color('pink'),
                ),
            ),
        )
        launch_app(stacker.view_model)

    def test_notebook(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.hstack(
            w.NoteBook('paned_window1', stacker).frame_names(('A', 'B', 'C', 'D')).stackers(
                stacker.vstack(
                    stacker.hstack(
                        w.Label('label1').text('Label1'),
                        w.Button('button1').text('Button1').command(lambda: print('button1')).width(10),
                    ),
                    stacker.hstack(
                        w.Label('label2').text('Label2'),
                        w.Button('button2').text('Button2').command(lambda: print('button2')).width(10),
                    ),
                    stacker.hstack(
                        w.Label('label3').text('Label3'),
                        w.Button('button3').text('Button3').command(lambda: print('button3')).width(10),
                    ),
                    w.Spacer(),
                    w.Button('button4').text('Button4').command(lambda: print('button4')).width(10),
                ),
                stacker.vstack(
                    w.Canvas('canvas1').color('pink'),
                ),
                stacker.hstack(
                    stacker.vstack(
                        w.Canvas('canvas2').color('light yellow'),
                        w.Button('button5').text('Button5').command(lambda: print('button5')).width(10),
                    ),
                ),
                w.Canvas('canvas').color('light green'),
            ),
        )
        launch_app(stacker.view_model)

    def test_tree_view(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.hstack(
            w.PanedWindow('paned_window1', stacker).is_horizontal().weights((6, 1)).stackers(
                stacker.hstack(
                    w.NoteBook('notebook1', stacker).frame_names(('A', 'B', 'Tree')).stackers(
                        stacker.vstack(
                            stacker.hstack(
                                w.Label('label1').text('Label1'),
                                w.Button('button1').text('Button1').command(lambda: print('button1')).width(10),
                            ),
                            stacker.hstack(
                                w.Label('label2').text('Label2'),
                                w.Button('button2').text('Button2').command(lambda: print('button2')).width(10),
                            ),
                            stacker.hstack(
                                w.Label('label3').text('Label3'),
                                w.Button('button3').text('Button3').command(lambda: print('button3')).width(10),
                            ),
                            w.Spacer(),
                            w.Button('button4').text('Button4').command(lambda: print('button4')).width(10),
                        ),
                        stacker.vstack(
                            w.Canvas('canvas1').color('pink'),
                        ),
                        stacker.hstack(
                            stacker.vstack(
                                w.TreeView('tree1'),
                                w.Button('button5').text('Button5').command(lambda: print('button5')).width(10),
                            ),
                        ),
                    ),
                ),
                stacker.vstack(
                    w.TreeView('tree2').padding(2, 2),
                    w.TextBox('text').padding(2, 2),
                ),
            ),
        )
        launch_app(stacker.view_model)

    def test_text(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.hstack(
            w.TextBox('text1').back_ground_color('light yellow').border_width(10),
            w.TextBox('text1').back_ground_color('light blue').text_color('red').cursor_color('brown').select_color(
                'yellow'),
        )
        launch_app(stacker.view_model)

    def test_radio_button(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.vstack(
            stacker.hstack(
                w.TextBox('text1').back_ground_color('pink'),
                w.TextBox('text2'),
            ),
            stacker.hstack(
                w.Spacer(),
                w.RadioButton('radio_buttond1').names(('Japan', 'US', 'China')).is_horizontal(),
                w.Spacer(),
            ),
        )
        launch_app(stacker.view_model)

    def test_check_button(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.vstack(
            stacker.hstack(
                w.TextBox('text1').back_ground_color('pink'),
                w.TextBox('text2'),
            ),
            stacker.hstack(
                w.Spacer(),
                w.Label('label1').text('Export'),
                w.CheckButton('check_buttond1').value(False),
                w.Spacer(),
            ),
        )
        launch_app(stacker.view_model)

    def test_combo_box(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        stacker.vstack(
            stacker.hstack(
                w.TextBox('text1').back_ground_color('pink'),
                w.TextBox('text2'),
            ),
            stacker.hstack(
                w.Spacer(),
                w.ComboBox('combobox_1').values(tuple(range(100))).height(30).width(30),
                w.Spacer(),
            ),
        )
        launch_app(stacker.view_model)

    def test_fmide_gui(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        def macro_buttons():
            return stacker.vstack(
                w.TreeView('tree_macro'),
                stacker.hstack(
                    w.Spacer(),
                    w.Button('macro_tree_1').text('↑').width(3).command(lambda: print(('↑'))),
                    w.Button('macro_tree_2').text('↓').width(3).command(lambda: print(('↓'))),
                    w.Button('macro_tree_3').text('Copy').command(lambda: print('Copy')),
                    w.Button('macro_tree_4').text('Delete').command(lambda: print('Delete')),
                    w.Button('macro_tree_5').text('Clear').command(lambda: print('Clear')),
                ),
            )

        def four_horizontal_buttons(t1, t2, t3, t4, prefix):
            return stacker.hstack(
                w.Button(f'{prefix}_{t1}').text(t1).width(3).command(lambda: print(t1)),
                w.Button(f'{prefix}_{t2}').text(t2).width(3).command(lambda: print(t2)),
                w.Button(f'{prefix}_{t3}').text(t3).width(3).command(lambda: print(t3)),
                w.Button(f'{prefix}_{t4}').text(t4).width(3).command(lambda: print(t4)),
                w.Spacer().adjust(-4),
                w.Spacer().adjust(-4),
                w.Spacer().adjust(-4),
                w.Spacer().adjust(-4),
            )

        def label_entry(label_id, entry_id, label_text, ):
            return stacker.hstack(
                w.Label(label_id).text(label_text).padding(5, 0).align('e').width(6),
                w.Entry(entry_id).padding(5, 0),
                w.Spacer().adjust(-1),
            )

        def label_combobox(label_id, combo_box_id, label_text, ):
            return stacker.hstack(
                w.Label(label_id).text(label_text).padding(5, 0).align('e').width(6),
                w.ComboBox(combo_box_id).padding(5, 0).width(10),
                w.Spacer().adjust(-1),
            )

        def notebook_canvas_status():
            frame_names = ('Ac', 'Pr', 'WS', 'CN',)
            return w.NoteBook('note_book_canvas_status', stacker).frame_names(frame_names).stackers(
                stacker.vstack(
                    w.TreeView(f'tree_{frame_names[0]}'),
                    stacker.hstack(
                        w.Button('btn_Ac_up').text('↑').command(lambda: print('↑')),
                        w.Button('btn_Ac_down').text('↓').command(lambda: print('↓')),
                        w.Button('btn_Ac_space').text('[_]').command(lambda: print('[_]')),
                    ),
                ),
                stacker.vstack(
                    label_entry('label_state_name', 'entry_state_name', 'Text:'),
                    label_entry('label_state_x', 'entry_state_x', 'x:'),
                    label_entry('label_state_y', 'entry_state_y', 'y:'),
                    label_entry('label_state_width', 'entry_state_width', 'width:'),
                    label_entry('label_state_height', 'entry_state_height', 'height:'),
                    label_entry('label_state_Sheet', 'entry_state_Sheet', 'Sheet:'),
                    label_entry('label_stateΔx', 'entry_stateΔx', 'Δx:'),
                    label_entry('label_stateΔy', 'entry_stateΔy', 'Δy:'),
                    label_entry('label_state_id', 'entry_state_id', 'id:'),
                    label_entry('label_state_UOM', 'entry_state_UOM', 'UOM:'),
                    label_combobox('cb_box_state_Format', 'cb_box_state_Format', 'Format:'),
                    label_combobox('cb_box_state_#', 'cb_box_state_#', '#:'),
                    stacker.hstack(
                        w.Label('label_vertical').text('Vertical:').padding(5, 0).width(6),
                        w.CheckButton('check_btn_vertical').value(False),
                        w.Entry('entry_vertical').width(4),
                        w.Button('btn_vertical_add').text('Add').width(4),
                        w.Button('btn_vertical_remove').text('Rem').width(4),
                        w.Spacer().adjust(-5),
                    ),
                    w.Spacer(),
                ),
                w.TreeView(f'tree_{frame_names[2]}'),
                w.TreeView(f'tree_{frame_names[3]}'),
            )

        def canvas_controller():
            return stacker.vstack(
                stacker.hstack(
                    w.Entry('entry_account_name').default_value('Account Name').width(4),
                    w.Button('btn_add_shape').text('Add').width(5),
                ),
                stacker.vstack(
                    four_horizontal_buttons('+', '-', 'x', '/', 'btn_operator'),
                    four_horizontal_buttons('BB', 'max', 'min', 'ave', 'btn_operator'),
                    four_horizontal_buttons('<=', '<', '>=', '>', 'btn_operator'),
                    four_horizontal_buttons('=', '^', 'abc', 'ana', 'btn_operator'),
                    four_horizontal_buttons('↩︎', '↪︎', 'New', 'Rel', 'btn_operator'),
                    four_horizontal_buttons('Del', 'XL', 'IE', 'Mod', 'btn_operator'),
                    four_horizontal_buttons('←', '↑', '↓', '→', 'btn_operator'),
                    four_horizontal_buttons('-', '=', '|', '||', 'btn_operator'),
                    four_horizontal_buttons('>w<', '<W>', '-w', '+W', 'btn_operator'),
                    notebook_canvas_status(),
                    w.Spacer().adjust(-1),
                ),
                w.Spacer().adjust(-1),
            )

        main_menu = ('Canvas', 'State', 'Macro')  # 'Template', 'State', 'Macro', 'Setting')
        stacker.vstack(
            w.NoteBook('main_notebook', stacker).frame_names(main_menu).stackers(
                stacker.hstack(
                    w.PanedWindow('pw_canvas', stacker).is_horizontal().weights((0, 1)).stackers(
                        canvas_controller(),
                        w.Canvas('canvas_main').color('pink'),
                    ),
                ),
                stacker.vstack(
                    w.TextBox('state_text'),
                ),
                stacker.vstack(
                    stacker.hstack(
                        w.Label('macro_label_record_macro').text('Record Macro:'),
                        w.CheckButton('macro_check_btn_record_macro').value(False),
                        w.Spacer(),
                        w.Entry('macro_entry_record_macro').default_value('New Macro Name'),
                        w.Button('macro_btn_set_name').text('set name'),
                        w.Button('macro_btn_set_args').text('set args'),
                        w.Button('macro_btn_set_kwargs').text('set kwargs'),
                    ),
                    w.PanedWindow('macro_paned_window', stacker).is_horizontal().stackers(
                        macro_buttons(),
                        stacker.hstack(
                            stacker.vstack(
                                w.Spacer(),
                                w.Button('btn_macro_right').width(2).text('->').command(
                                    lambda: print('macro_right')),
                                w.Button('btn_macro_left').width(2).text('<-').command(lambda: print('macro_left')),
                                w.Spacer(),
                            ),
                            stacker.vstack(
                                w.TreeView('tree_saved_macros'),
                                stacker.hstack(
                                    w.Button('btn_delete_macro_file').text('Delete').command(
                                        lambda: print('del_mac')),
                                ),
                            ),
                            w.Spacer().adjust(-1),
                        ),
                    ),
                    w.Spacer().adjust(-1),
                ),
            ),
        )

        launch_app(stacker.view_model)

    def test_work_automator_gui(self):
        from stacker import Stacker
        from stacker import widgets as w
        stacker = Stacker()

        notebook_tabs = ('Add', 'Calendar',)

        def main_tab_one_add_form():
            bp = 0, 20, 20, 0
            frame_names = ('Properties', 'Notes', 'Files')
            switchable_frames = []

            def switch_frame(frame_index):
                app.switch_frame(switchable_frames[frame_index])

            return stacker.vstack(
                stacker.hstack(
                    w.Button('add_Milestone').text('Add Milestone').wh_padding(*bp).command(lambda: print('Milestone')),
                    w.Button('add_Task').text('Add Task').wh_padding(*bp).command(lambda: print('Add Task')),
                    w.Spacer().adjust(-2),
                    w.Spacer().adjust(-2),
                ),
                stacker.hstack(
                    w.Spacer(),
                    w.Button('btn_swithcer').text('Pr').width(2).command(lambda: switch_frame(0)),
                    w.Button('btn_swithcer').text('txt').width(2).command(lambda: switch_frame(1)),
                    w.Button('btn_swithcer').text('Tr').width(2).command(lambda: switch_frame(2)),
                    w.Spacer(),
                ),
                w.FrameSwitcher('frame_switcher', stacker, switchable_frames).stackers(
                    # w.NoteBook('note_book_add', stacker).frame_names(frame_names).stackers(
                    stacker.vstack(
                        label_entry(stacker, w, 'label_add_form_name', 'entry_add_form_name', 'Name:'),
                        label_entry(stacker, w, 'label_add_due', 'entry_add_due', 'Due:'),
                        label_entry(stacker, w, 'label_add_duration', 'entry_add_duration', 'Duration:'),
                        label_entry(stacker, w, 'label_add_Owner', 'entry_add_Owner', 'Owner:'),
                        w.Spacer(),
                    ),
                    w.TextBox('add_text').width(10).padding(10, 0),
                    w.TreeView('add_file_tree').padding(10, 0),
                ),
                w.Spacer().adjust(-1),
            )

        def main_tab_one():
            return w.PanedWindow('pw_tab_one', stacker).is_horizontal().weights((0, 1)).stackers(
                main_tab_one_add_form(),
                w.Canvas('canvas_tab_one').color('light yellow'),
            )

        stacker.vstack(
            w.NoteBook('note_book_top', stacker).frame_names(notebook_tabs).stackers(
                main_tab_one(),
            ),
        )

        from view_tkinter import View
        app = View()
        view_model = stacker.view_model
        app.add_widgets(view_model)
        app.launch_app()

    def test_frame_switcher(self):
        from view_tkinter import View
        from stacker import Stacker
        from stacker import widgets as w

        app = View()
        stacker = Stacker()

        frames_switchable1 = []
        frames_switchable2 = []

        def switch_frame1(n):
            index_ = n - 1
            frame_selected = frames_switchable1[index_]
            app.switch_frame(frame_selected)

        def switch_frame2(n):
            index_ = n - 1
            frame_selected = frames_switchable2[index_]
            app.switch_frame(frame_selected)

        stacker.vstack(
            w.FrameSwitcher('frame_stacker_id1', stacker, frames_switchable1).stackers(
                w.Canvas('canvas1').color('light green'),
                w.Canvas('canvas2').color('white'),
                w.Canvas('canvas3').color('orange'),
            ),
            w.FrameSwitcher('frame_stacker_id2', stacker, frames_switchable2).stackers(
                stacker.hstack(w.Spacer(), w.Label('label1').text('Frame1'), w.Spacer()),
                stacker.hstack(w.Spacer(), w.Label('label2').text('Frame2'), w.Spacer()),
                stacker.hstack(w.Spacer(), w.Label('label3').text('Frame3'), w.Spacer()),
            ),
            stacker.hstack(
                w.Spacer(),
                w.Button('btn_switcher1').width(15).text('Switch Canvas 1').command(lambda: switch_frame1(1)),
                w.Button('btn_switcher2').width(15).text('Switch Canvas 2').command(lambda: switch_frame1(2)),
                w.Button('btn_switcher3').width(15).text('Switch Canvas 3').command(lambda: switch_frame1(3)),
                w.Spacer(),
            ),
            stacker.hstack(
                w.Spacer(),
                w.Button('btn_switcher4').width(15).text('Switch Label 1').command(lambda: switch_frame2(1)),
                w.Button('btn_switcher5').width(15).text('Switch Label 2').command(lambda: switch_frame2(2)),
                w.Button('btn_switcher6').width(15).text('Switch Label 3').command(lambda: switch_frame2(3)),
                w.Spacer(),
            ),
        )

        view_model = stacker.view_model
        app.add_widgets(view_model)
        app.launch_app()

    def test_ui_ludo_mom(self):
        from view_tkinter import View
        from stacker import Stacker
        from stacker import widgets as w

        ### Data structure
        categories = (
            '商品製造',
            '設備投資',
            '売上',
            '借入',
            '出資',
            '配当',
        )

        response_model_gui0 = {
            'account_ids': [0, 1, 2],
            'account_names': {0: '販売数量', 1: '販売単価', 2: '売上高'},
            'uoms': {0: 'ton', 1: '$/ton', 2: '$'},
            'input_values': {0: [1, 2, 3], 1: [4, 5, 6], },
            'input_min_max': {0: (0, 10), 1: (0, 10), }
        }
        response_model_gui1 = {
            'account_ids': [3, 4, 5],
            'account_names': {3: '販売数量', 4: '原価', 5: '売上原価'},
            'uoms': {3: 'kg', 4: '$/kg', 5: '$'},
            'input_values': {3: [1, 2, 3], 4: [4, 5, 6], },
            'input_min_max': {3: (0, 10), 4: (0, 10), }
        }
        response_model_gui2 = {
            'account_ids': [6, 7, 8],
            'account_names': {6: 'A', 7: 'B', 8: 'C'},
            'uoms': {6: 'kg', 7: 'JPY/kg', 8: 'JPY'},
            'input_values': {6: [1, 2, 3], 7: [4, 5, 6], },
            'input_min_max': {6: (0, 10), 7: (0, 10), }
        }
        response_models = [response_model_gui0, response_model_gui1, response_model_gui2]

        app = View()
        stacker = Stacker()

        frames_switchable = []

        def switch_frame(n):
            index_ = n
            try:
                frame_selected = frames_switchable[index_]
            except IndexError:
                frame_selected = frames_switchable[0]
            app.switch_frame(frame_selected)

        bp = 0, 0, 0, 0

        # Category Buttons
        category_buttons_elements = []
        for n, category in enumerate(categories):
            btn = w.Button(f'btn_category_{n}').text(categories[n]).wh_padding(*bp).command(lambda i=n: switch_frame(i))
            category_buttons_elements.append(btn)
        category_buttons_elements.append(w.Spacer())
        category_buttons = stacker.vstack(*tuple(category_buttons_elements))

        # Response Model GUI
        response_model_elements = []
        for request_model in response_models:
            vertical_elements_in_a_response_model = []
            account_ids = request_model.get('account_ids')
            account_names = request_model.get('account_names')
            uoms = request_model.get('uoms')
            input_values = request_model.get('input_values')
            input_min_max = request_model.get('input_min_max')
            for account_id in account_ids:
                horizontal_elements = []
                name = account_names.get(account_id)
                uom = uoms.get(account_id)

                horizontal_elements.append(w.Label(f'lbl_{account_id}').width(20).text(f'アカウント名:{name}'))
                horizontal_elements.append(w.Entry(f'entry_{account_id}').default_value(name))
                horizontal_elements.append(w.Label(f'lbl_uom_{account_id}').width(10).text('単位名:').width(5))
                horizontal_elements.append(w.Entry(f'entry_uom_{account_id}').default_value(uom).width(10))

                if account_id in input_values:
                    input_id = account_id
                    values = input_values.get(input_id)
                    input_min, input_max = input_min_max.get(input_id)

                vertical_elements_in_a_response_model.append(tuple(horizontal_elements))
            response_model_elements.append(tuple(vertical_elements_in_a_response_model))

        def user_input_frames():
            vstacks = []
            for vertical_elements in response_model_elements:
                hstacks = []
                for horizontal_elements in vertical_elements:
                    horizontal_elements += (w.Spacer(),)
                    hstacks.append(stacker.hstack(*horizontal_elements))
                hstacks.append(w.Spacer())
                vstacks.append(stacker.vstack(*tuple(hstacks)))
            return tuple(vstacks)

        stacker.hstack(
            w.PanedWindow('pw_01', stacker).is_horizontal().weights((0, 1, 1)).stackers(
                category_buttons,
                w.FrameSwitcher('frame_switcher_01', stacker, frames_switchable).stackers(*user_input_frames(), ),
                w.NoteBook('nb_state', stacker).frame_names(('Tree', 'B')).stackers(
                    w.TreeView('tree_01'),
                    w.TreeView('tree_02'),
                ),
            ),

        )

        view_model = stacker.view_model
        app.add_widgets(view_model)
        app.launch_app()

    def test_fmIDE_states(self):
        from view_tkinter import View
        from stacker import Stacker
        from stacker import widgets as w

        app = View()
        stacker = Stacker()

        stacker.hstack(
            w.PanedWindow('pw_state', stacker).is_horizontal().weights((0, 1)).stackers(
                stacker.vstack(
                    w.Button('btn_state_shape_id').text('Shape ID'),
                    w.Button('btn_state_connection').text('Connections'),
                    w.Button('btn_state_formula').text('Formula'),
                    w.Button('btn_state_worksheets').text('Worksheets'),
                    w.Button('btn_state_inputs').text('Inputs'),
                    w.Spacer(),
                ),
                stacker.hstack(
                    w.TreeView('tree_state'),
                ),
            )
        )

        view_model = stacker.view_model
        app.add_widgets(view_model)
        app.launch_app()

    def test_macro_builder(self):
        import pickle
        from view_tkinter import View
        app = View()

        pickle_path = '/Users/yamaka/Documents/GitHub/gui_builder/Tests/macro_builder/gui_macro_builder'
        with open(pickle_path, 'rb') as f:
            view_model = pickle.load(f)

        switchable_frames = [
            'frame_3',
            'frame_9',
            'frame_14',
            'frame_19',
            'frame_21',
            'frame_25',
            'frame_28',
        ]
        button_ids = [
            'btn_001',
            'btn_002',
            'btn_003',
            'btn_004',
            'btn_005',
            'btn_006',
            'btn_007',
        ]

        def switch_frame(n):
            if len(switchable_frames) >= n + 1:
                widget_id = switchable_frames[n]
            else:
                widget_id = switchable_frames[0]
            app.switch_frame(widget_id)

        app.add_widgets(view_model)
        for n, button_id in enumerate(button_ids):
            app.bind_command_to_widget(button_id, lambda nn=n: switch_frame(nn))
        app.launch_app()


if __name__ == '__main__':
    unittest.main()
