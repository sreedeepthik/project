#example for request
import json
from watson_developer_cloud import ConversationV1

conversation = watson_developer_cloud.ConversationV1(
    username='{username}',
    password='{password}',
    version='2018-07-10'
)

response = conversation.message(
    workspace_id='6bad7d51-c6c2-4768-a5cc-7f37a96571e0',
    input={
        'text': 'Hello'
    }
)

print(json.dumps(response, indent=2))

#example request

import json
import watson_developer_cloud

conversation = watson_developer_cloud.ConversationV1(
    username='{e77a223e-bcf3-4a0f-b36b-b7ed93661210}',
    password='{avTW2Gldzzt5}',
    version='2018-07-10'
)

response = conversation.list_workspaces()

print(json.dumps(response, indent=2))

#example response

{
  "workspaces" : [ {
    "name" : "coffeebot",
    "language" : "en",
    "metadata" : {
      "runtime_version" : "2018-07-10"
    },
    "description" : "Coffee bot which allows you to oder coffee",
    "workspace_id" : "6bad7d51-c6c2-4768-a5cc-7f37a96571e0",
    "learning_opt_out" : false
  } ],
  "pagination" : {
    "refresh_url" : "/v1/workspaces?version=2018-07-10"
  }
}



