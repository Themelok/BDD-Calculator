import subprocess

def before_all(context):

    def open_proc():
        return subprocess.Popen(['gcalccmd'],
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    def handle_response(response):
        handled = response.decode('utf-8').replace('>','').strip()
        if chr(8722) in handled: 
            handled = handled.replace(chr(8722),chr(45))
        if ',' in handled:
            handled = handled.replace(',','.')
            handled = str(round(float(handled),1))
        return handled

    context.open_proc = open_proc
    context.handle_response = handle_response

def after_scenario(context, scenario):
    context.calc.terminate()