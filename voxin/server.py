import argparse
import logging

import tornado.ioloop
import tornado.web

from voxin.handlers import MainHandler

application = tornado.web.Application([
    (r"/(.*)", MainHandler),
])

def main():
    try:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

        parser = argparse.ArgumentParser(description='Start the server.')
        parser.add_argument('-p', '--port', help='The port the server should be started on.',
                            default='8888', type=int)
        args = parser.parse_args()
        
        logging.info("Started listening on port %d" % args.port)
        
        application.listen(args.port)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
