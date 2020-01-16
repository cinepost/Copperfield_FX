viewport_layouts = {
    "single_view": {
        "title": "Single View",
        "shortcut": "Cmd+1",
        "icon": "gui/icons/panels/scene_view_panel/layout_single_view.svg",
        "layout": None
    },
    "four_views": {
        "title": "Four Views",
        "shortcut": "Cmd+2",
        "icon": "gui/icons/panels/scene_view_panel/layout_four_views.svg",
    },
    "two_stacked": {
        "title": "Two Views Stacked",
        "icon": "gui/icons/panels/scene_view_panel/layout_two_views_stacked.svg",
        "shortcut": "Cmd+3",
    },
    "two_aside": {
        "title": "Two Views Side By Side",
        "icon": "gui/icons/panels/scene_view_panel/layout_two_views_side_by_side.svg",
        "shortcut": "Cmd+4",
    },
    "three_split_bottom": {
        "title": "Three Views Split Bottom",
        "icon": "gui/icons/panels/scene_view_panel/layout_three_views_split_bottom.svg",
        "shortcut": "Cmd+5"
    },
    "three_split_left": {
        "title": "Three Views Split Left",
        "icon": "gui/icons/panels/scene_view_panel/layout_three_views_split_left.svg",
        "shortcut": "Cmd+6"
    },
    "four_split_bottom": {
        "title": "Four Views Split Bottom",
        "icon": "gui/icons/panels/scene_view_panel/layout_four_views_split_bottom.svg",
        "shortcut": "Cmd+7"
    },
    "four_split_left": {
        "title": "Four Views Split Left",
        "icon": "gui/icons/panels/scene_view_panel/layout_four_views_split_left.svg",
        "shortcut": "Cmd+8"
    }
}
"""
viewport_layout_types = [
    { 
        "layout": {
            "type": "hbox",
            "views": [
                "persp"
            ]
        }
    },
    {
        "layout": {
            "type": "hbox",
            "layouts": [
                {
                    "type": "vbox",
                    "views": [
                        "top", "persp"
                    ]
                },
                {
                    "type": "vbox",
                    "views": [
                        "left", "bottom"
                    ]
                }
            ]
        }
    },
]
"""