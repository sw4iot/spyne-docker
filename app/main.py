import logging
import os

from spyne import ServiceBase, Unicode, Integer, Iterable, Application, rpc
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield 'Hello, %s' % name


application = Application([HelloWorldService],
                          tns='spyne.examples.hello',
                          in_protocol=HttpRpc(validator='soft'),
                          out_protocol=JsonDocument()
                          )
if __name__ == '__main__':
    # You can use any Wsgi server. Here, we chose
    # Python's built-in wsgi server but you're not
    # supposed to use it in production.
    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)

    port = int(os.getenv('SW4IOT_AGENT_PORT', 9091))
    logging.info("Start server port {}".format(port))

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', port, wsgi_app)
    server.serve_forever()
