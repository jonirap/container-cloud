from ..base_server import endpoint
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectID
from typing import Union


class API:
    def __init__(self, mongo_client: AsyncIOMotorClient, mongo_database_name: str = 'ContainerCloud'):
        super().__init__()
        self._mongo_client = mongo_client
        self._database = self._mongo_client[mongo_database_name]

    @property
    def tasks(self):
        return self._database.tasks

    @endpoint('v1')
    async def add_task(self, docker_image_name: str,
                       required_mem: float = 128,
                       required_cpu: float = 1,
                       environment_variables: dict = None,
                       command: str = '',
                       ) -> str:
        return str(await self.tasks.insert_one(dict(
            docker_image_name=docker_image_name,
            required_mem=required_mem,
            required_cpu=required_cpu,
            environment_variables=environment_variables,
            has_run=False,
            is_running=False,
            cancelled=False,
            exit_code=None,
            executor=None,
        )).inserted_id)

    @endpoint('v1')
    async def cancel_task(self, container_id: Union[str, ObjectID]) -> bool:
        return (await self.tasks.update_one(dict(_id=ObjectID(str(container_id))),
                                            {'$set': dict(cancelled=True)})).modified_count == 1

    @endpoint('v1')
    async def get_task(self, container_id: Union[str, ObjectID]) -> dict:
        return await self.tasks.find_one(dict(_id=ObjectID(str(container_id))))

    @endpoint('v1')
    async def is_task_running(self, container_id: Union[str, ObjectID]) -> bool:
        return (await self.get_task(container_id))['is_running']

    @endpoint('v1')
    async def is_task_completed(self, container_id: Union[str, ObjectID]) -> bool:
        return (await self.get_task(container_id))['has_run']

    @endpoint('v1')
    async def was_task_cancelled(self, container_id: Union[str, ObjectID]) -> bool:
        return (await self.get_task(container_id))['cancelled']
