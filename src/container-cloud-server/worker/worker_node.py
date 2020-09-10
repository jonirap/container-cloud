from psutil import virtual_memory
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Function
from multiprocessing import Process


async def receive_tasks(mongo_client: AsyncIOMotorClient,
                        database_name: str,
                        collection_name: str,
                        task_callback: Function,
                        reserve_mem: float = 32 * 1024 * 1024):
    resume_token = None
    pipeline = [{'$match': {'operationType': 'insert'}}]
    try:
        async with db.collection.watch(pipeline) as stream:
            async for insert_change in stream:
                print(insert_change)
                resume_token = stream.resume_token
    except pymongo.errors.PyMongoError:
        # The ChangeStream encountered an unrecoverable error or the
        # resume attempt failed to recreate the cursor.
        if resume_token is None:
            # There is no usable resume token because there was a
            # failure during ChangeStream initialization.
            logging.error('...')
        else:


async def check_processes(mongo_client: AsyncIOMotorClient,
                          processes: List[Process]):
    pass
