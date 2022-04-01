from enum import Enum
from queue import Queue

class States(Enum):
  DETROIT = 1
  ROSEVILLE = 2
  EASTPOINTE = 3
  ANN_ARBOR = 4
  GRAND_RAPIDS = 5

class Actions(Enum):
  DRIVE = 1

transitions = {
  States.DETROIT: [
    {
      "action": Actions.DRIVE,
      "state": States.EASTPOINTE,
      "cost": 10,
    },
    {
      "action": Actions.DRIVE,
      "state": States.ANN_ARBOR,
      "cost": 5,
    }
  ],
  States.EASTPOINTE: [
    {
      "action": Actions.DRIVE,
      "state": States.ROSEVILLE,
      "cost": 5,
    },
    {
      "action": Actions.DRIVE,
      "state": States.DETROIT,
      "cost": 5,
    }
  ],
  States.ROSEVILLE: [
    {
      "action": Actions.DRIVE,
      "state": States.EASTPOINTE,
      "cost": 5,
    }
  ],
  States.ANN_ARBOR: [
    {
      "action": Actions.DRIVE,
      "state": States.DETROIT, 
      "cost": 5,
    },
    {
      "action": Actions.DRIVE,
      "state": States.GRAND_RAPIDS,
      "cost": 7,
    }
  ]
}

def main():
  frontier_queue = Queue()
  frontier_queue.put({
    "state": States.ROSEVILLE,
    "cost": 0,
  })

  print(bfs(frontier_queue, transitions, States.GRAND_RAPIDS))


def bfs(queue, transitions, goal):
  while True:
    node = queue.get()
    if node["state"] == goal:
      return node
    # TODO: attempt other actions?
    child_nodes = expand_node(node, Actions.DRIVE, transitions[node["state"]])
    for child_node in child_nodes:
      queue.put(child_node)

def expand_node(node, action, node_transitions):
  action_transitions = [transition for transition in node_transitions if transition["action"] == action]
  action_transitions_with_running_cost = [{
    **transition,
    "cost": transition["cost"] + node["cost"]
  } for transition in action_transitions]
  return action_transitions_with_running_cost

main()