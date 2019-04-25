from webapp import app

def startWebServer():
    """This function start a Flask webserver for SmartMTk control
    """

    # Run flask webserver
    app.run(host="0.0.0.0")

if __name__ == '__main__':
    # Run webserver when this file is called by command line
    startWebServer()
