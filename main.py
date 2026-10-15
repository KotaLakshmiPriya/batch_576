from fastapi import FastAPI
app=FastAPI(title="Priya")


students=[
    {"id":1,"name":"a","dept":"python"},
    {"id":2,"name":"b","dept":"c"},
    {"id":3,"name":"c","dept":"java"},
    {"id":4,"name":"d","dept":"python"},
    {"id":5,"name":"e","dept":"c"}
]


# Path parameters
@app.get("/students/{student_id}")
def get_student_id(student_id:int):
    print(student_id) # Not necessary to print, but for debugging purposes
    print(type(student_id)) # Not necessary to print, but for debugging purposes
    for student in students:
        if student["id"]==student_id:
            return student
    return {"message":"student not found"}


# If I give the dept name I want all the students in that dept
@app.get("/students")
def get_student_dept(dept:str):
    result=[]
    for student in students:
        if student["dept"]==dept:
            result.append(student)
    return result


@app.get("/")
def home():
    return {"message": "Hello, fastAPI!"}


@app.get("/name")
def name():
    return {"Batch - 576"}