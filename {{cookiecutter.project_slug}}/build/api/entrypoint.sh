#!/bin/bash

uvicorn {{cookiecutter.api_module_name}}.main:app --host 0.0.0.0 --port 8000