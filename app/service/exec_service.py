from app.schema.exec_command import ExecCommand
from app.schema.eval_command import EvalCommand

import math

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
ALLOWED_NAMES['math'] = math

def execute(exec_command_body: ExecCommand):
    safe_dict = _safe_commands()
    exec_command_body.input_args_as_key_value["__builtins__"] = None

    exec(exec_command_body.command_text, exec_command_body.input_args_as_key_value, safe_dict)

    outputs = {}
    for output_arg in exec_command_body.output_args_keys:
       outputs[output_arg] = safe_dict[output_arg]

    return outputs


def evaluate(eval_command_body: EvalCommand):
    """Evaluate a math expression."""
    # Compile the expression
    code = compile(eval_command_body.command_text, "<string>", "eval")

    # Validate allowed names
    #for name in code.co_names:
    #    if name not in ALLOWED_NAMES:
    #        raise NameError(f"The use of '{name}' is not allowed")

    safe_dict = ALLOWED_NAMES
    eval_command_body.input_args_as_key_value["__builtins__"] = None

    return eval(eval_command_body.command_text, eval_command_body.input_args_as_key_value, safe_dict)


def _safe_commands():
    #safe_list = ['abs', 'math','acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
    #safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
    return {'abs': abs, 'math': math}