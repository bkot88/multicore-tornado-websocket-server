# tornado-multicore-websocket-server

An example of a tornado websocket server which accepts cpu heavy work from a client. Using python's multiprocessing Pipe and Process, the server provides feedback in real time back to the client, via websockets.

# Getting started

1. Launch the server first.
```
> git clone https://github.com/bkot88/tornado-multicore-websocket-server.git
> cd tornado-multicore-websocket-server
> python server.py
```
2. Run client.html from a browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
