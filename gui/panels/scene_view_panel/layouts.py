viewport_layout_types = [
    { 
        "name": "Single View",
        "icon": "panels/scene_view_panel/layout_single_view.svg",
        "layout": {
            "type": "hbox",
            "views": [
                1
            ]
        }
    },
    {
        "name": "Four Views",
        "icon": "panels/scene_view_panel/layout_four_views.svg",
        "layout": {
            "type": "hbox",
            "layouts": [
                {
                    "type": "vbox",
                    "views": [
                        1, 2
                    ]
                },
                {
                    "type": "vbox",
                    "views": [
                        1, 2
                    ]
                }
            ]
        }
    },
    {
        "name": "Two Views Stacked",
        "icon": "panels/scene_view_panel/layout_two_views_stacked.svg" 
    },
    {
        "name": "Two Views Side By Side",
        "icon": "panels/scene_view_panel/layout_two_views_side_by_side.svg"
    },
    {
        "name": "Three Views Split Bottom",
        "icon": "panels/scene_view_panel/layout_three_views_split_bottom.svg"
    },
    {
        "name": "Three Views Split Left",
        "icon": "panels/scene_view_panel/layout_three_views_split_left.svg"
    },
    {
        "name": "Four Views Split Bottom",
        "icon": "panels/scene_view_panel/layout_four_views_split_bottom.svg"
    },
    {
        "name": "Four Views Split Left",
        "icon": "panels/scene_view_panel/layout_four_views_split_left.svg"
    }
]