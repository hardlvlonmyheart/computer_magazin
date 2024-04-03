from src.server.database import pydantic_models, database_models
from src.server.service import RouterManager


routers = (
    RouterManager(object_name='client', pydantic_model=pydantic_models.Client, database_model=database_models.Client, prefix='/client', tags=['Clients']),
    RouterManager(object_name='manager', pydantic_model=pydantic_models.Manager, database_model=database_models.Manager, prefix='/manager', tags=['Managers']),
    RouterManager(object_name='storekeeper', pydantic_model=pydantic_models.Storekeeper, database_model=database_models.Storekeeper, prefix='/storekeeper', tags=['Storekeepers']),
    RouterManager(object_name='order', pydantic_model=pydantic_models.Order, database_model=database_models.Order, prefix='/order', tags=['Orders']),
    RouterManager(object_name='report', pydantic_model=pydantic_models.Report, database_model=database_models.Report, prefix='/report', tags=['Reports']),
    RouterManager(object_name='supply', pydantic_model=pydantic_models.Supply, database_model=database_models.Supply, prefix='/supply', tags=['Supplies']),
    RouterManager(object_name='master', pydantic_model=pydantic_models.Master, database_model=database_models.Master, prefix='/master', tags=['Masters']),
    RouterManager(object_name='details', pydantic_model=pydantic_models.Details, database_model=database_models.Details, prefix='/detail', tags=['Details']),
    RouterManager(object_name='post', pydantic_model=pydantic_models.Post, database_model=database_models.Post, prefix='/post', tags=['Posts']),
    RouterManager(object_name='user', pydantic_model=pydantic_models.User, database_model=database_models.User, prefix='/user', tags=['Users'])
)
