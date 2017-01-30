viewport_layout_types = [
    { 
        "name": "Single View",
        "icon": "icons/panels/scene_view_panel/layout_single_view.svg",
        "shortcut": "Cmd+1",
        "layout": {
            "type": "hbox",
            "views": [
                "persp"
            ]
        }
    },
    {
        "name": "Four Views",
        "icon": "icons/panels/scene_view_panel/layout_four_views.svg",
        "shortcut": "Cmd+2",
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
                        "top", "persp"
                    ]
                }
            ]
        }
    },
    {
        "name": "Two Views Stacked",
        "icon": "icons/panels/scene_view_panel/layout_two_views_stacked.svg",
        "shortcut": "Cmd+3"
    },
    {
        "name": "Two Views Side By Side",
        "icon": "icons/panels/scene_view_panel/layout_two_views_side_by_side.svg",
        "shortcut": "Cmd+4"
    },
    {
        "name": "Three Views Split Bottom",
        "icon": "icons/panels/scene_view_panel/layout_three_views_split_bottom.svg",
        "shortcut": "Cmd+5"
    },
    {
        "name": "Three Views Split Left",
        "icon": "icons/panels/scene_view_panel/layout_three_views_split_left.svg",
        "shortcut": "Cmd+6"
    },
    {
        "name": "Four Views Split Bottom",
        "icon": "icons/panels/scene_view_panel/layout_four_views_split_bottom.svg",
        "shortcut": "Cmd+7"
    },
    {
        "name": "Four Views Split Left",
        "icon": "icons/panels/scene_view_panel/layout_four_views_split_left.svg",
        "shortcut": "Cmd+8"
    }
]