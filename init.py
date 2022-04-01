from enum import Enum
from queue import PriorityQueue, Queue
from dataclasses import dataclass, field
from typing import Any

class States(Enum):
  DETROIT = 1
  ROSEVILLE = 2
  EASTPOINTE = 3
  ANN_ARBOR = 4
  GRAND_RAPIDS = 5

class Actions(Enum):
  DRIVE = 1

@dataclass(order=True)
class Node:
    state: States = field(compare=False)
    cost: int = field(compare=False)
    action: Actions = field(compare=False)
    priority: int = field(compare=True, default=0)
    prev: Any = field(compare=False, default=None)

transitions = {
  States.DETROIT: [
    Node(
      action = Actions.DRIVE,
      state = States.EASTPOINTE,
      cost = 10
    ),
    Node(
      action = Actions.DRIVE,
      state = States.ANN_ARBOR,
      cost = 5,
    )
  ],
  States.EASTPOINTE: [
    Node(
      action = Actions.DRIVE,
      state = States.ROSEVILLE,
      cost = 5,
    ),
    Node(
      action = Actions.DRIVE,
      state = States.DETROIT,
      cost = 5,
    )
  ],
  States.ROSEVILLE: [
    Node(
      action = Actions.DRIVE,
      state = States.EASTPOINTE,
      cost = 5,
    )
  ],
  States.ANN_ARBOR: [
    Node(
      action = Actions.DRIVE,
      state = States.DETROIT, 
      cost = 5,
    ),
    Node(
      action = Actions.DRIVE,
      state = States.GRAND_RAPIDS,
      cost = 7,
    )
  ]
}

def main():
  # frontier_queue = Queue()
  frontier_queue = PriorityQueue()
  frontier_queue.put(
    Node(States.ROSEVILLE, 0, Actions.DRIVE)
  )

  result = bfs(frontier_queue, transitions, States.GRAND_RAPIDS)
  print(result.state);
  while result.prev != None:
    print(result.prev.state)
    result = result.prev



def bfs(queue, transitions, goal):
  visited = []
  while True:
    node = queue.get()
    if node.state == goal:
      return node
    # TODO: attempt other actions?
    visited.append(node.state)
    child_nodes = expand_node(node, Actions.DRIVE, transitions[node.state], visited)
    for child_node in child_nodes:
      queue.put(child_node)

def expand_node(node, action, node_transitions, visited):
  action_transitions = [
    transition for transition in node_transitions
    if transition.action == action and not transition.state in visited
  ]
  action_transitions_with_running_cost = [
    Node(
      transition.state,
      transition.cost,
      transition.action,
      transition.cost + node.cost,
      node
    ) for transition in action_transitions]
  return action_transitions_with_running_cost

main()