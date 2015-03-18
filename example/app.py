from example import app

from time import sleep

@app.route('/process')
def process():
    """
    Does a lot of processing.
    """
    sleep(3)
    return 'Processing Complete!'

@app.route('/process-efficiently')
def process_efficiently():
    """
    Does a lot of processing, but more efficiently than process().
    """
    sleep(2)
    return 'Efficient Processing Complete!'
