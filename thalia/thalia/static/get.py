
def get_show(wid):
    # how can i get all the shows and check them for wid
    shows = []
    for s in shows:
        if s.check_id(wid):
            return s.make()


def get_all_shows():
    shows = []
    show_list = []
    for s in shows:
        show_list.append(s.make())
    return show_list
