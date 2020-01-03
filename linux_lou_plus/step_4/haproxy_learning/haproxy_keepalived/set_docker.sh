#!/bin/bash
docker run --privileged --name=HAProxy-master -tid ubuntu > /dev/null
docker run --privileged --name=HAProxy-backup -tid ubuntu > /dev/null
docker run --privileged --name=nginx-server-1 -tid ubuntu > /dev/null
docker run --privileged --name=nginx-server-2 -tid ubuntu > /dev/null
docker run --privileged --name=nginx-server-3 -tid ubuntu > /dev/null
docker ps