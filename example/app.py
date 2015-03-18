from example import app

from time import sleep

@app.route('/process')
def does_stuff():
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

@app.route('/meaning-of-life')
def meaning_of_life():
    return 42 
