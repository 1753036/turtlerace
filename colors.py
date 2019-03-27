color_palette = {
    #COMMON
    "bg": "#101010",
    "fg": "#E0E0E0",
    "base": "#212121",
    "borders": "#F0F0F0",
    "title": "#FF5080",
    "subti": "#00ce97",
    "selected_bg": "#FF5080",
    "selected_fg": "#FFFFFF",
    
    #BUTTON
    "btn_normal_fg": "#7dc3ff",
    "btn_hover_fg": "#a1d7ff",
    "btn_active_fg": "#97afff",

    #LEADERBOARD
    "lead_title_fg": "#FFEE00",
    "lead_bg": "#232323",
    "lead_fg": "#E0E0E0",
    "lead_border": "#FF4040",
    "lead_header": "#66FF44",

    #GAMEMENU
    "menu_title_fg": "#FF5080"
}

def get(widget):
    return color_palette[widget]
