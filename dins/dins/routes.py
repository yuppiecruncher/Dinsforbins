def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    #home controller
    config.add_route('home', '/')

    #diner controller
    config.add_route('diner', '/diner')
