def define_env(env):
    def badge(text, color="gray", size="md"):
        color_map = {
            "red": ("#f8d7da", "#721c24", "#f5c2c7"),
            "green": ("#d4edda", "#155724", "#c3e6cb"),
            "blue": ("#d1ecf1", "#0c5460", "#bee5eb"),
            "orange": ("#fff3cd", "#856404", "#ffeeba"),
            "gray": ("#e2e3e5", "#383d41", "#d6d8db"),
        }

        size_map = {
            "tiny": {
                "padding": "1.25px 5.5px",
                "font_size": "0.65em",
                "radius": "4px",
            },
            "small": {
                "padding": "2px 8px",
                "font_size": "0.75em",
                "radius": "6px",
            },
            "medium": {
                "padding": "4px 12px",
                "font_size": "0.85em",
                "radius": "8px",
            },
            "large": {
                "padding": "6px 16px",
                "font_size": "1em",
                "radius": "10px",
            },
        }

        bg, fg, border = color_map.get(color, color_map["gray"])
        size_style = size_map.get(size, size_map["medium"])

        html = f'''
        <span style="
            display:inline-block;
            padding:{size_style['padding']};
            border-radius:{size_style['radius']};
            background:{bg};
            color:{fg};
            font-size:{size_style['font_size']};
            font-weight:bold;
            border:1px solid {border};
            margin-right:6px;
        ">{text}</span>
        '''
        return html.strip()

    env.macro(badge)
