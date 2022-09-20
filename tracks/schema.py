from ninja import ModelSchema, Schema
from tracks.models import Track
from ninja.orm import create_schema

# alternate way to cerate a Schema class
# TrackSchema = create_schema(Track, fields = ['title', 'last_play', 'artist', 'duration'])

class TrackSchema(ModelSchema):
    class Config:
        model = Track
        model_fields = ['title', 'last_play', 'artist', 'duration']

class NotFoundSchema(Schema):
    message: str

