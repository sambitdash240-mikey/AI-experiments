from collections import deque

# function to solve water jug problem using BFS
def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    # initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        # skip if the state has been visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # add current state to the path
        path = path + [(jug1, jug2)]

        # check if target is reached
        if jug1 == target or jug2 == target:
            return path

        next_states = [
            # fill jug 1
            (capacity1, jug2),

            # fill jug 2
            (jug1, capacity2),

            # empty jug 1
            (0, jug2),

            # empty jug 2
            (jug1, 0),

            # pour jug 1 -> jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            # pour jug 2 -> jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        # add unvisited states to the queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    # No solution found
    return None


# main program
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")

    for step in solution:
        print(step)
else:
    print("No solution exists.")
