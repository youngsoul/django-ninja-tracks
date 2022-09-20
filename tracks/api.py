from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from django.http import HttpRequest
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema
from typing import List, Optional

api = NinjaAPI()

@api.get("/test")
def test(request: HttpRequest):
    print(request.path)
    return {'test': "success", "type": f"{type(request)}"}

@api.get("/tracks", response=List[TrackSchema])
def tracks(request: HttpRequest, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    else:
        return Track.objects.all()

@api.get("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request: HttpRequest, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

@api.post("/tracks", response={201: TrackSchema})
def create_track(request: HttpRequest, track: TrackSchema):
    Track.objects.create(**track.dict())
    return 201, track


@api.put("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request:HttpRequest, track_id: int, data: TrackSchema):
    try:
        track_from_db = Track.objects.get(pk=track_id)
        for attribute, value in data.dict().items():
            setattr(track_from_db, attribute, value)
            track_from_db.save()
        return 200, track_from_db
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

@api.delete("/tracks/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def delete_track(request:HttpRequest, track_id:int):
    try:
        track_from_db = Track.objects.get(pk=track_id)
        track_from_db.delete()
        return 200, track_from_db
    except Track.DoesNotExist as e:
        return 404, {"message": "Track does not exist"}

@api.post('/upload', url_name='upload')
def update(request: HttpRequest, file: UploadedFile = File(...)):
    data = file.read().decode()
    return {'name': file.name,
            'data': data,
            'len': len(data)}
