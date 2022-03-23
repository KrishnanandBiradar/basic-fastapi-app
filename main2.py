from typing import Optional, Text
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# simple paths
@app.get("/")
def base():
    return {"message": "Hello from FastAPI"}

@app.get("/about")
def about():
    return {"data": "this is about page"}

# query parameters default, optional
@app.get("/blogs")
def blogs(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blog list from db by default"}
    else:
        return {"data": f"all blog list from db"}



@app.get("/blog/unpublished")
def unpublished():
    # fetch all blogs
    return {"data": "unpublished blog list"}

# path parameters
@app.get("/blog/{blog_id}")
def blog_id(blog_id: int):
    # fetch blog with id = blog_id
    return {"data": blog_id}

@app.get("/blog/{blog_id}/comments")
def comments(blog_id):
    # fetch comments for blog with id = blog_id
    return {"comments": [{1: 'first-comment'}, {2: 'second-comment'}]}

# pydantic model examples
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(newblog: Blog):
    # fetch comments for blog with id = blog_id
    return {"data": {f'blog is created with title: {newblog.title}'}}


