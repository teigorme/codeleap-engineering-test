from datetime import datetime
from ninja import Schema
from typing import Optional
from ninja import NinjaAPI
from .models import Posts
from django.shortcuts import get_object_or_404

class PostIn(Schema):
    title: str
    content: Optional[str] = None
    username: str

class PostOut(Schema):
    id: int
    username: str
    created_at: datetime
    updated_at: datetime
    title: str
    content: Optional[str] = None


api = NinjaAPI()


@api.post("/", response={201: PostOut})
def create_post(request, payload: PostIn):
    post = Posts.objects.create(**payload.dict())
    return post

@api.get("/", response=list[PostOut])
def list_posts(request):
    return Posts.objects.all().order_by('-created_at')

@api.get("/{post_id}/", response=PostOut)
def get_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    return post


@api.put("/{post_id}/", response=PostOut)
def update_post(request, post_id: int, payload: PostIn):
    post = get_object_or_404(Posts, id=post_id)
    for attr, value in payload.dict().items():
        setattr(post, attr, value)
    post.save()
    return post

@api.delete("/{post_id}/")
def delete_post(request, post_id: int):
    post = get_object_or_404(Posts, id=post_id)
    post.delete()
    