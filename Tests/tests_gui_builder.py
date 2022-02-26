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
            w.PanedWindow('paned_window1').is_horizontal().stackers(
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


if __name__ == '__main__':
    unittest.main()
