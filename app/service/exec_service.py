from app.schema.exec_command import ExecCommand

import math

def execute(exec_command_body: ExecCommand):
    #safe_list = ['abs', 'math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
    #safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
    safe_dict = {'abs': abs, 'math': math}
    exec_command_body.input_args_as_key_value["__builtins__"] = None

    exec(exec_command_body.command_text, exec_command_body.input_args_as_key_value, safe_dict)

    outputs = {}
    for output_arg in exec_command_body.output_args_keys:
       outputs[output_arg] = safe_dict[output_arg]

    return outputs