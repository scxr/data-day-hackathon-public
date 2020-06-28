#!/usr/bin/env python3
from app import app
import os

app.run(host="0.0.0.0", port=os.getenv('PORT', '5000'), debug=True) # change in deployment