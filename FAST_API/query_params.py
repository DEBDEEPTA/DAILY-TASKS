""" HANDLING Query PARAMETERS"""
from fastapi import FastAPI, Path, HTTPException,Query
from typing import Optional

app = FastAPI()
students = {
    1: {
        "name":"DEV",
        "age":23
    },

    2:{
        "name":"AVI",
        "age":25
    },

    3:{
        "name":"SID",
        "age":22
    }
}

"""************** NORMAL QUERY PARAMETER (DEFAULT REQUIRED) ************"""

@app.get("/student/")
                     # here id will act as query parameter
                     # as no corresponding path variable in the url is mentioned
def get_student_by_id(id:int):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return students[id]

"""************** Optional QUERY PARAMETER ************"""
@app.get("/student/name/")                        # as default -> None Swagger UI marks it as required field
def get_student_by_name(name:Optional[str] = Query(None,description="Enter Student Name")):
    flag = True
    for s_id in students:
        if students[s_id]["name"] == name:
            return students[s_id]
            flag = False
            break
    if flag:
        raise HTTPException(
            status_code=404,
            detail= "Student not found"
        )
"""************** REQUIRED QUERY PARAMETER ************"""

@app.get("/students/required/")
def get_student_by_id_req(id:int = Query(..., description="Required Filed Student ID")):
    if not id in students:
        raise HTTPException(
            status_code= 404,
            detail="Student Not Found"
        )
    else:
        return students[id]

# @app.get("/student/combined_params/{name}")
#
# def get_student_by_id_or_name(*,
#                               name:Optional[str] = Path(None,description="Enter Student Name"),
#                               id:Optional[int] = Query(description="Enter the student id"),
#                               meta:Optional[str] = Query(..., description="non required field")):
#
#     # DEFAULT SEARCH BY NAME
#     if not name == None:
#         pass
