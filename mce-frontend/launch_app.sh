#!/bin/bash

export PYTHONPATH=/app
streamlit run src/main.py --server.port=8080 --server.address=0.0.0.0