from app.schema.exec_command import ExecCommand
from app.schema.eval_command import EvalCommand

import math
import requests
import random
import json

ALLOWED_NAMES = {
    k: v for d in [math.__dict__, requests.__dict__, json.__dict__] for k,v in d.items() if not k.startswith("__")
}
ALLOWED_NAMES['math'] = math
ALLOWED_NAMES['requests'] = requests
ALLOWED_NAMES['random'] = random
ALLOWED_NAMES['json'] = json

def execute(exec_command_body: ExecCommand):
    input_args = exec_command_body.input_args_as_key_value or {}
    #_validate_input("exec", exec_command_body.command_text, input_args)
    safe_dict = ALLOWED_NAMES
    input_args["__builtins__"] = None

    exec(exec_command_body.command_text, input_args, safe_dict)

    outputs = {}
    for output_arg in exec_command_body.output_args_keys:
       outputs[output_arg] = safe_dict[output_arg]

    return outputs


def evaluate(eval_command_body: EvalCommand):
    input_args = eval_command_body.input_args_as_key_value or {}
    #_validate_input("eval", eval_command_body.command_text, input_args)

    input_args["__builtins__"] = None

    return eval(eval_command_body.command_text, input_args, ALLOWED_NAMES)


def _validate_input(type, text, input_args):
    """Evaluate a math expression."""
    # Compile the expression
    _validate_allowed_commands(type, text, input_args)
    for value in input_args.values():
        _validate_allowed_commands(type, value, {})


def _validate_allowed_commands(type, text, input_args):
    code = compile(str(text), "<string>", type)
    for name in code.co_names:
        if name not in ALLOWED_NAMES and name not in input_args:
            raise NameError(f"The use of '{name}' is not allowed")


def _safe_commands():
    #safe_list = ['abs', 'math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
    #safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
    return {'abs': abs, 'math': math}