class FrameOptions(dict):
    def __init__(self):
        self['parent_id'] = {}
        self['options'] = {}
        self['static_args'] = {}
        self['row1'] = {}
        self['row2'] = {}
        self['col1'] = {}
        self['col2'] = {}

        dict.__init__(self)

    @property
    def all_frame_ids(self) -> tuple:
        return tuple(self['parent_id'].keys())

    def set_parent_id(self, frame_id, parent_id):
        self['parent_id'].update({frame_id: parent_id})

    def set_options(self, frame_id, options: dict):
        self['options'].update({frame_id: options})

    def set_row(self, frame_id, row):
        self['row1'].update({frame_id: row})
        self['row2'].update({frame_id: row})

    def set_col(self, frame_id, col):
        self['col1'].update({frame_id: col})
        self['col2'].update({frame_id: col})

    def set_static_args(self, frame_id, static_args: dict):
        self['static_args'].update({frame_id: static_args})

    def get_parent_id(self, frame_id, ):
        return self['parent_id'].get(frame_id)

    def get_options(self, frame_id, ):
        return self['options'].get(frame_id)

    def get_static_args(self, frame_id, ):
        return self['static_args'].get(frame_id)

    def get_row1(self, frame_id):
        return self['row1'].get(frame_id)

    def get_row2(self, frame_id):
        return self['row2'].get(frame_id)

    def get_col1(self, frame_id):
        return self['col1'].get(frame_id)

    def get_col2(self, frame_id):
        return self['col2'].get(frame_id)