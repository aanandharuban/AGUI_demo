import {
  HttpAgent,
  randomUUID,
} from "@ag-ui/client";

const agent = new HttpAgent({
  url: "http://127.0.0.1:8000/langgraph-agent",
  headers: {
    "Content-Type": "application/json",
  },
});

async function executeAgentCall() {
  try {
    agent.messages.push({
      id: randomUUID(),
      role: "user",
      content: "Hello, Agent! Can you tell me a joke?",
    })
    await agent.runAgent({}, {
      onTextMessageStartEvent() {
        console.log("Text message started");
      }, 

      onTextMessageContentEvent({ event }) {
        console.log(event.delta)
      },

      onTextMessageEndEvent() {
        console.log("\n")
      }
    });
  } catch (error) {
    console.error("Execution failed:", error);
  }
}

executeAgentCall();