### **1. Fast API**
1. _FastAPI is a modern, high-performance **Python web framework for building APIs**_
2. _Built for **speed**, **type safety**, and developer productivity_

### 2. **Why Fast API ? :**
 * ASGI (Asynchronous Server Gateway Interface)
 * async / await
 * Non-blocking I/O
### 3. **Performance Comparison**
```
    FastAPI ≈ NodeJS ≈ Go
    Flask < Django < FastAPI
```

### 4. **Key Components :**

| Component     | Role                                              |
| ------------- | ------------------------------------------------- |
| **Starlette** | Web handling (routing, middleware, async support) |
| **Pydantic**  | Data validation, parsing, serialization           |
| **Uvicorn**   | ASGI server (runs the app)                        |
| **OpenAPI**   | Automatic API documentation                       |

### 5. **Work Flow**

```         
        Client
          ↓
        Uvicorn (ASGI Server)
          ↓
        FastAPI App
          ↓
        Router
          ↓
        Path Operation Function
          ↓
        Pydantic Validation
          ↓
        Response Serialization
          ↓
        Client
```
### 6. Installation
    # UVICORN ACTS AS A SERVER TO RUN FAST API APPLICATIONS
```commandline
    pip install fastapi uvicorn
```

### HANDLING PARAMETERS
1. **Path params**     
2. **Query params**
   * _Normal Query Params_                    
   * _Optional Query Params_                
   * _Required Query Params_                
3. **Combining query & path Params**
#### Path Params

```python
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
    
    @app.get("/student/{id}")
                                #  Path() is used to declare, validate, and document path parameters.
    def get_student_by_id(id:int = Path(description="The ID of the student you want to view",ge=0)):
        return students.get(id,"Student Not Found")
```
| Aspect                     | Without `Path()`                      | With `Path()`                                       |
| -------------------------- | ------------------------------------- | --------------------------------------------------- |
| Validation rules           | ❌ Not supported                       | ✅ Supported (`ge`, `gt`, `le`, `lt`, `regex`, etc.) |
| Example validation         | ❌ Not possible                        | `ge=1`, `le=100`, `regex="^[A-Z]+$"`                |
| Swagger / OpenAPI docs     | ❌ Minimal                             | ✅ Rich documentation                                |
| Description support        | ❌ Not available                       | ✅ `description="..."`                               |
| Error messages             | ⚠️ Generic                            | ✅ Clear & detailed                                  |
| Constraints enforcement    | ❌ No                                  | ✅ Yes                                               |
| Metadata (examples, title) | ❌ No                                  | ✅ Yes                                               |
| Best use case              | Simple, quick routes                  | Production-grade APIs                               |

    ```
    note -> If a parameter appears in the URL path → it is REQUIRED, you can't make it Optional
         -> thats why default value for path can't be null
         
    e.g  -> id: int = Path(...)              # ✅ Required
         -> id: int                          # ✅ Required
         -> id: Optional[int] = Path(None)   # ❌ INVALID
         -> id: int = Path(10)               # ❌ INVALID -> DOESN'T SUPPORTS DEFAULT VALUE
         -> id: Optional[int]                # ❌ Still required
    ```
### Query Params
*  **_Normal Query Params (Default Required)_**
    ```python
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
    ```
  * **_Optional Query Params_**
    ```python
    from typing import Optional
    
    @app.get("/student/name/")                      
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
        
      ```
  * **_Required Query Params_**
    ```python
    from fastapi import FastAPI,Query
    
    @app.get("/students/required/")
    def get_student_by_id_req(id:int = Query(..., description="Required Filed Student ID")):
        if not id in students:
            raise HTTPException(
                status_code= 404,
                detail="Student Not Found"
            )
        else:
            return students[id]
    ```
    ```
    e.g  -> id: int = Path(...)              # ✅ Required
         -> id: int                          # ✅ Required
         -> id: Optional[int] = Path(None)   # ✅ Optional
         -> id: int = Path(10)               # ✅ Default Value is considered if no value is provided
         -> id: Optional[int]                # ❌ Still required
    ```
  * **_Combining query & path Params_**
    * _Key Concept_
      > All parameters WITHOUT default values must come BEFORE parameters WITH default values.
      
      > In simple terms:
        * Required parameters → first
        * Optional (defaulted) parameters → last
      
    ```python
        def get_student(name: Optional[str] = None, test: int): # ❌ SyntaxError: non-default argument follows default argument
        def get_student(name: Optional[str] = None, test: int): # ✅ valid
    ``` 