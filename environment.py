import subprocess

def before_all(context):

    def open_proc():
        return subprocess.Popen(['gcalccmd'],
                                stdin=subprocess.PIPE, 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

    def handle_response(x):
        resp = x.decode('utf-8').replace('>','').strip()
        if chr(8722) in resp: 
            resp = resp.replace(chr(8722),chr(45))
        return resp

    context.open_proc = open_proc
    context.handle_response = handle_response

# def after_all(context):
#     context.calc.kill()

def after_scenario(context, scenario):
    context.calc.terminate()