# py_http_server

## about the project
    - A very simple web server 

## Overview

* **PyHTTPServer Class**: A Class that handles all server methods.
* **_creaate_req_handler**: A method to add the req handling class to and make a instance of it when called.
* **PyReqHandler**: A class to handle crud type operations.
* **start_server**: A method that create a instance of PyReqHandler then it tries to start the server using a method from http.server.HTTPServer. If that fails an error will show.
* **stop_server**: A method that stops the server instance.

