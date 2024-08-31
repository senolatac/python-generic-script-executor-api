from pydantic import BaseModel

class ExecCommand(BaseModel):
    command_text: str
    input_args_as_key_value: dict = {}
    output_args_keys: list = []