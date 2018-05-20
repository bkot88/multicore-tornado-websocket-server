
import json
import logging
from multiprocessing import Pipe, Process
from threading import Thread

import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
from tornado.options import define, options


define("port", default=9001, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/", MainHandler)]
        settings = dict(debug=True)
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        logging.info("A client connected.")

    def on_close(self):
        logging.info("A client disconnected")

    def on_message(self, message):
        logging.info("message: {}".format(message))
        # self.write_message('you said' + message)
        job = json.loads(message)
        if 'doWork' in job and job['doWork'] is True:
            r, w = Pipe(duplex=False)
            Process(target=doWork, args=(w,)).start()
            Thread(target=reader, args=(self, r)).start()
            # We close the writable end of the pipe now to be sure that
            # p is the only process which owns a handle for it.  This
            # ensures that when p closes its handle for the writable end,
            # wait() will promptly report the readable end as being ready.
            w.close()


def reader(client, pipe):
    alive = True
    while alive:
        try:
            # retrieve msgs from the pipe and send to client
            msg = pipe.recv()
            client.write_message(msg)
        except EOFError:
            alive = False


def doWork(conn):
    # emulate a long task
    conn.send('work process starting...')
    for i in range(10):
        msg = '{}/100%'.format((i+1)*10)
        # send msg to the pipe
        conn.send(msg)
    conn.send('work process finished')
    conn.close()


def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
