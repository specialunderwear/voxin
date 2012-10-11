import tornado

class MainHandler(tornado.web.RequestHandler):

    def get(self, url):
        self.write("It seems you tried to visit %s" % url)
