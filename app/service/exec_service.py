from app.schema.exec_command import ExecCommand

def execute(exec_command_body: ExecCommand):
   local_vars = {}
   exec(exec_command_body.command_text, exec_command_body.input_args_as_key_value, local_vars)

   outputs = {}
   for output_arg in exec_command_body.output_args_keys:
      outputs[output_arg] = local_vars[output_arg]

   return outputs