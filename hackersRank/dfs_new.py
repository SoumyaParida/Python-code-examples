def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print "graph[vertex]",graph[vertex]
            print "visited",visited
            stack.extend(graph[vertex] - visited)
            print stack
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]

    while stack:
        print "print stack",stack
        (vertex, path) = stack.pop()
        print "graph[vertex]",graph[vertex]
        print "set(path)",set(path)
        print "graph[vertex] - set(path)",graph[vertex] - set(path)
        for next in graph[vertex] - set(path):
            print "next",next
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))




graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#print dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

print list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]