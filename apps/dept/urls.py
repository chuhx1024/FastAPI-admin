from fastapi import APIRouter, Body, Depends, HTTPException
from typing import Dict, List
from sqlalchemy.orm import Session
from sqlalchemy import select, alias, text
from sqlalchemy import column, ARRAY, Integer
from database.database import get_db
from .models import Dept
from schemas.response_models import ResponseModel, CustomHTTPException
from .schemas import *


dept = APIRouter()


@dept.post("/depts", response_model=ResponseModel[DeptResponse], summary="创建部门")
async def create_dept(
    dept: DeptCreate = Body(
        ...,
        title="部门创建信息",
        description="包含部门详细信息的请求体",
        example={
            "name": "技术部",
            "desc": "描述",
            "parent_id": 0,
        },
    ),
    db: Session = Depends(get_db),
):
    """
    :param name: 部门名称
    :param desc: 部门描述
    :param parent_id: 父部门ID
    """
    existing_dept = db.query(Dept).filter(Dept.name == dept.name).first()
    if existing_dept:
        raise HTTPException(status_code=201, detail={"msg": "部门已存在!"})
    dept_data = {
        "name": dept.name,
        "desc": dept.desc,
        "parent_id": dept.parent_id,
    }
    db_dept = Dept(**dept_data)

    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return ResponseModel(
        code=200,
        data={
            "name": db_dept.name,
            "id": db_dept.id,
            "desc": db_dept.desc,
            "parent_id": db_dept.parent_id,
        },
        msg="部门创建成功!",
    )


@dept.get(
    "/depts", response_model=ResponseModel[list[DeptResponse]], summary="查看部门列表"
)
async def list_dept(
    db: Session = Depends(get_db),
):
    all_depts = db.query(Dept).all()

    def build_tree(parent_id):
        return [
            {
                "id": dept.id,
                "name": dept.name,
                "desc": dept.desc,
                "parent_id": dept.parent_id,
                "children": build_tree(dept.id),  # 递归构建子部门
            }
            for dept in all_depts
            if dept.parent_id == parent_id
        ]

        # 从顶级部门（parent_id=0）开始构建部门树
        dept_tree = build_tree(0)
        return dept_tree

    root_nodes = build_tree(0)
    return ResponseModel(
        code=200,
        data=root_nodes,
        msg="部门列表获取成功!",
    )
