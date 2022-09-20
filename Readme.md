# Django and Ninja

Quick tutorial on the Ninja package for Django to give FastAPI like development for REST apis.

## Official Documentation
https://django-ninja.rest-framework.com

## YouTube Tutorial
https://www.youtube.com/playlist?list=PL-2EBeDYMIbS7bXwkMOS_ajeTdNRnhApX

## Postgres

Because we manually insert we need the following

https://stackoverflow.com/questions/9108833/postgres-autoincrement-not-updated-on-explicit-id-inserts

```SELECT setval('tracks_track_id_seq', (SELECT MAX(id) from "tracks_track"));```


### Setup data

```shell
make run-shell
python manage.py ingest_tracks

```

go to datagrip:
```SELECT setval('tracks_track_id_seq', (SELECT MAX(id) from "tracks_track"));```

