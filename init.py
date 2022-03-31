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
      "cost": 5,
    }
  ]
}

def main():
  start_state = States.ROSEVILLE
  frontier_queue = Queue()
  frontier_queue.put(start_state)

  bfs(frontier_queue, States, transitions)


def bfs(queue, states, transitions):
  item = queue.get()
  while item:
    nodes = expand_node(item, states, transitions[item])
    // TODO: add new items to queue?
    item = queue.get()
  return 0

def expand_node(node, states, transitions):
  return 0