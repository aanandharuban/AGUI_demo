import os
import uuid
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

from ag_ui.core import (
    RunAgentInput,
    EventType,
    RunStartedEvent,
    RunFinishedEvent,
    RunErrorEvent,
    TextMessageChunkEvent,
)
from ag_ui.encoder import EventEncoder

app = FastAPI(title="AG-UI Custom Server")


async def custom_agent(messages):
  
    user_message = messages[-1].content if messages else ""

    response = f"You said: {user_message}"

    for word in response.split():
        yield word + " "


@app.post("/")
async def agentic_chat_endpoint(
    input_data: RunAgentInput,
    request: Request,
):
    encoder = EventEncoder(
        accept=request.headers.get("accept")
    )

    async def event_generator():
        try:
            yield encoder.encode(
                RunStartedEvent(
                    type=EventType.RUN_STARTED,
                    thread_id=input_data.thread_id,
                    run_id=input_data.run_id,
                )
            )

            message_id = str(uuid.uuid4())

            async for chunk in custom_agent(
                input_data.messages
            ):
                yield encoder.encode(
                    TextMessageChunkEvent(
                        type=EventType.TEXT_MESSAGE_CHUNK,
                        message_id=message_id,
                        delta=chunk,
                    )
                )

            yield encoder.encode(
                RunFinishedEvent(
                    type=EventType.RUN_FINISHED,
                    thread_id=input_data.thread_id,
                    run_id=input_data.run_id,
                )
            )

        except Exception as e:
            yield encoder.encode(
                RunErrorEvent(
                    type=EventType.RUN_ERROR,
                    message=str(e),
                )
            )

    return StreamingResponse(
        event_generator(),
        media_type=encoder.get_content_type(),
    )


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
    )