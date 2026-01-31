""" HANDLING PATH PARAMETERS"""
from fastapi import FastAPI, Path

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

@app.get("/all")
def get_all_students():
    return students

@app.get("/student/{id}")
                            #  Path() is used to declare, validate, and document path parameters.
def get_student_by_id(id:int = Path(description="The ID of the student you want to view",ge=0)):
    return students.get(id,"Student Not Found")

"""
    2️⃣ Why use Path() instead of just id: int?
        from fastapi import FastAPI, Path
        def get_student_by_id(id: int):
        ...
        
    With out Path():
        . Basic type conversion (str → int)
        . No validation rules
        . Minimal OpenAPI docs
    With Path():
        . Validation (min, max, regex, etc.)    <-- ge =
        . Swagger documentation                 <-- description = 
        . Better error messages
"""

"""
| Parameter     | Meaning                                         |
| ------------- | ----------------------------------------------- |
| `...`         | Required parameter                              |
| `default`     | Default value (not recommended for path params) |
| `description` | Swagger documentation                           |
| `ge`          | Greater than or equal                           |
| `gt`          | Greater than                                    |
| `le`          | Less than or equal                              |
| `lt`          | Less than                                       |
| `min_length`  | Min string length                               |
| `max_length`  | Max string length                               |
| `regex`       | Pattern matching                                |
| `example`     | Sample value                                    |

"""


