def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    #home controller
    config.add_route('index', '/')
    config.add_route('about', '/about')

    #account controller
    config.add_route('account_home', '/account')
    config.add_route('login', '/account/login')
    config.add_route('register', '/account/register')
    config.add_route('logout', '/account/logout')

    # role controllers
    config.add_route('diner', '/diner')
    config.add_route('diner_request', '/diner/request')
    config.add_route('chef', '/chef')
    # config.add_route('chef_add', '/chef/add')
    # config.add_route('chef_diners', '/chef/diners')
    config.add_route('analyst', '/analyst')

    #API controllers
    #POST
    config.add_route('api_diner', '/api/diner')
    config.add_route('api_chef', '/api/chef')
    config.add_route('api_analyst', '/api/analyst')
    #GET
    config.add_route('api_diner_get', '/api/diner/{uid}')
    config.add_route('api_chef_get', '/api/chef/data')
    config.add_route('api_analyst_get', '/api/analyst/data')
