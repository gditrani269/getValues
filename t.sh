podman run -it -v /mnt/c/Users/papa/n/desa/python/getValues:/home/desa/python -p 8084:8000  --name python-dockerfile debian-python-1.0

podman exec -it python-dockerfile /bin/bash