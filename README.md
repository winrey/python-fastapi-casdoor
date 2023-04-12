# fastAPI Casdoor
Integration Casdoor with FastAPI

## Installation

```bash
pip install fastapi-casdoor
```

## Usage

```python
from typing import Annotated, Depends
from fastapi import FastAPI
from fastapi_casdoor.deps import get_current_user
from fastapi_casdoor.models import User


@app.get("/")
async def root(user: Annotated[User, Depends(get_current_user)]):
    return {
        "user": user,
    }
```
