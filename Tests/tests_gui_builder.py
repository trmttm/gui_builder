import unittest


def launch_app(view_model):
    from view_tkinter import View
    app = View()
    app.add_widgets(view_model)
    app.launch_app()


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

        def canvas_controller():
            return stacker.vstack(
                stacker.hstack(
                    w.Entry('entry_account_name').default_value('Account Name'),
                    w.Button('btn_add_shape').text('Add'),
                ),
            )

        main_menu = ('Canvas', 'State', 'Macro')  # 'Template', 'State', 'Macro', 'Setting')
        stacker.vstack(
            w.NoteBook('main_notebook', stacker).frame_names(main_menu).stackers(
                stacker.hstack(
                    w.PanedWindow('pw_canvas', stacker).is_horizontal().stackers(
                        canvas_controller(),
                        w.Canvas('canvas_main').color('white'),
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
                        w.Button('macro_btn_set_kwargs®').text('set kwargs'),
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


if __name__ == '__main__':
    unittest.main()
