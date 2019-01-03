def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    #home controller
    config.add_route('home', '/')

    #account controller
    config.add_route('account_home', '/account')
    config.add_route('login', '/account/login')
    config.add_route('register', '/account/register')
    config.add_route('logout', '/account/logout')

    # role controllers
    config.add_route('diner', '/diner')
