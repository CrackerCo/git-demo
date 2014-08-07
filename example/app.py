from example import app

from time import sleep

@app.route('/process')
def process():
    """
    Does a lot of processing.
    """
    sleep(3)
    return 'Processing Complete!'
