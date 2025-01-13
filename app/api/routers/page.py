from fastapi import APIRouter, Request, Depends, HTTPException, status, Path
from starlette.responses import HTMLResponse

from app.models import Product, User
from app.api.dependencies import Session_DP, Auth_DP
from app.schemas import ProductSchema, DBProductSchema
from app.utils import make_response


page_r = APIRouter(tags=['pages'])



# @page_r.get('/')
# async def main_page(request: Request):
#     with open('app/frontend/index.html', 'r') as file:
#         html = file.read()

#     return HTMLResponse(html)

# @page_r.get('/{url}')
# async def page(request: Request, url: str = Path()):
    
#     with open(f'app/frontend/{url}.html', 'r') as file:
#         html = file.read()

#     return HTMLResponse(html)
