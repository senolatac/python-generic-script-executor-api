import logging

from fastapi import APIRouter, Depends, Body, HTTPException, status
from app.schema.eval_command import EvalCommand
from app.schema.exec_command import ExecCommand
from app.service import exec_service
from pydantic.v1 import Required

# APIRouter creates path operations for user module
from app.security.role_checker import RoleChecker
from app.security.security_config import USER

logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)

router = APIRouter(
    prefix="/python-scripts",
    tags=["Python Scripts"],
    responses={404: {"description": "Not found"}},
)

allow_create_resource = RoleChecker([USER])

@router.post("/eval", dependencies=[Depends(allow_create_resource)])
async def evaluate_command(eval_command_body: EvalCommand = Body(default=Required)):
    logging.info("Eval-command-request came")
    return exec_service.evaluate(eval_command_body)

@router.post("/exec", dependencies=[Depends(allow_create_resource)])
async def execute_command(exec_command_body: ExecCommand = Body(default=Required)):
    logging.info("Exec-command-request came with %s", "user-mode")
    return exec_service.execute(exec_command_body)

