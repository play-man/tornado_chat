from tornado import web, ioloop
from tornado.httpserver import HTTPServer
import handlers
from config import settings


class Application(web.Application):
    def __init__(self):
        h = [
            (r"/", handlers.ChannelHandler),
            (r"/channels/(?P<channel>\w+)/", handlers.ChannelHandler),
            (r"/login", handlers.LoginHandler),
            (r"/logout", handlers.LogoutHandler),
            (r"/chatsocket/(?P<channel>\w+)/", handlers.ChatSocketHandler),
        ]
        super(Application, self).__init__(handlers=h, **settings)


def main():
    app = Application()
    server = HTTPServer(app)
    server.listen(8888)

    loop = ioloop.IOLoop.current()

    loop.start()


if __name__ == "__main__":
    main()
