# tornado-multiprocess-websocket-server

An example of a tornado websocket server which accepts cpu heavy work from a client. Using python's multiprocessing Pipe and Process, the server provides feedback in real time back to the client, via websockets.

# Getting started

1. launch the server first.
```
> git clone https://github.com/bkot88/tornado-multicore-websocket-server.git
> cd tornado-multicore-websocket-server
> python server.py
```
2. launch client.html

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
