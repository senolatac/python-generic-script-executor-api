from pydantic import BaseModel

class EvalCommand(BaseModel):
    command_text: str
    input_args_as_key_value: dict = {}