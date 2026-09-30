from pythonds3.basic import Queue
import random
randomNum = int(random.randint(1,50))

def hot_potato(name_list, randomNum):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)

    while sim_queue.size() > 1:
        for i in range(randomNum):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()


print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], randomNum))
print(f'Hot potato was iterated {randomNum} times')