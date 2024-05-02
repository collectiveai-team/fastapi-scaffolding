FROM {{cookiecutter.base_image}}

COPY ./build/api/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY api /app/api

COPY ./build/api/entrypoint.sh /usr/bin/entrypoint.sh
ENTRYPOINT sh /usr/bin/entrypoint.sh