import os

settings = {
    'cookie_secret': 'b5bc816699d0a36c6be59398ce69dd85',
    'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'login_url': '/login',
    'xsrf_cookies': True,
    'debug': True,
    'autoreload': True,
    'server_traceback': True,
}