from collections import deque
from random import randrange
import time
from abc import ABC, abstractmethod


class Queue:
    def __init__(self):
        self._queue = deque([])

    # Adds an item (In this case a shopper) to the queue
    def enqueue(self, item):
        self._queue.append(item)

    # Removes an item (In this case a shopper) from the beginning of the queue
    def dequeue(self):
        return self._queue.popleft()

    # Shows the item (Or shopper) at the beginning of the queue
    def peek(self):
        return self._queue[0]

    # Wipes the entire queue
    def wipe(self):
        return not self._queue

    # Returns the length of the queue
    def length(self):
        return len(self._queue)


class Shopper:
    def __init__(self):
        # Randomly generates a number between 60 and 500
        self._checkout_time = randrange(60, 500)

    @property
    def checkout_time(self):
        return self._checkout_time

    @checkout_time.setter
    def checkout_time(self, checkout_time):
        # Sets the random number as the shoppers checkout checkout_checkout_time
        self._checkout_time = checkout_time


class SuperMarket:
    def __init__(self, num_queues, num_eQueues):
        self._queues = self.appendQueues(num_queues)
        self._eQueues = self.appendQueues(num_eQueues)

    def appendQueues(self, num_queues):
        queues = list()
        for i in range(num_queues):
            queues.append(Queue())
        return queues

    @property
    def queues(self):
        return self._queues

    @queues.setter
    def queues(self, queues):
        self._queues = queues

    @property
    def eQueues(self):
        return self._eQueues

    @eQueues.setter
    def eQueues(self, eQueues):
        self._eQueues = eQueues


class IVersion(ABC):
    @abstractmethod
    def enqueueShopper(self):
        pass


class Version1(IVersion):
    @staticmethod
    def enqueueShopper(SM, shopper):
        SM.queues[randrange(len(SM.queues))].enqueue(
            shopper)  # Enqueue a shopper to a random queue


class Version2(IVersion):
    @staticmethod
    def enqueueShopper(SM, shopper):
        shortestQueueIndex = getShortestQueueIndex(
            SM.queues)  # Get shortest queue index
        # Enqueue a shopper to a shortest queue
        SM.queues[shortestQueueIndex].enqueue(shopper)


class Version3(IVersion):
    @staticmethod
    def enqueueShopper(SM, shopper):
        if shopper.checkout_time <= 90:
            # Picks a random express queue
            SM.eQueues[randrange(len(SM.eQueues))].enqueue(shopper)
        else:
            SM.queues[randrange(len(SM.queues))].enqueue(
                shopper)  # Picks a random queue


class Version4(IVersion):
    @staticmethod
    def enqueueShopper(SM, shopper):
        if shopper.checkout_time <= 90:  # Express queue
            shortestQueueIndex = getShortestQueueIndex(
                SM.eQueues)  # Get shortest queue index
            # Enqueue a shopper to the shortest queue
            SM.eQueues[shortestQueueIndex].enqueue(shopper)
        else:  # Normal queue
            shortestQueueIndex = getShortestQueueIndex(
                SM.queues)  # Get shortest queue index
            # Enqueue a shopper to the shortest queue
            SM.queues[shortestQueueIndex].enqueue(shopper)


def getShortestQueueIndex(list_of_queues):
    shortestLength = min([queue.length() for queue in list_of_queues])
    for i in range(len(list_of_queues)):
        if list_of_queues[i].length() == shortestLength:
            return i


def checkAllQueueswipe(SM):
    return all([queue.wipe() for queue in SM.queues]) and all([queue.wipe() for queue in SM.eQueues])


def checkShoppersTime(list_of_queues):
    # Decrements and removes shopper if checkout_time is 0
    for queue in list_of_queues:
        if not queue.wipe():
            queue.peek().checkout_time -= 1
            if queue.peek().checkout_time == 0:  # Removed the shopper once their checkout checkout_time is 0
                queue.dequeue()


def runShopping(SM, new_shopper_rate, max_shopper_number, enqueueShopper):
    seconds = 0  # Counts the seconds it takes to complete the run
    while True:
        # Adding a new shopper every 10 seconds
        if seconds % new_shopper_rate == 0 and seconds < (new_shopper_rate)*(max_shopper_number):
            enqueueShopper(SM, Shopper())

        # Removes one second from the shoppers checking out
        for i in [SM.queues, SM.eQueues]:
            checkShoppersTime(i)

        seconds += 1
        if checkAllQueueswipe(SM):
            minutes = seconds / 60
            minutes = str(round(minutes)) #Rounded to whole minutes as a sample this large it wont have a significant effect
            return minutes


def main():

    NO_EQ = SuperMarket(num_queues=8, num_eQueues=0)
    EQ = SuperMarket(num_queues=6, num_eQueues=2)

    print('======================================================================')
    print('Shoppers randomly selecting queues: ')
    print('')
    print(f'It took {runShopping(NO_EQ, new_shopper_rate = 10, max_shopper_number = 1000, enqueueShopper = Version1.enqueueShopper)} minutes to complete the run.')
    print('======================================================================')
    time.sleep(2)
    print('Shoppers selecting shortest queues: ')
    print('')
    print(f'It took {runShopping(NO_EQ, new_shopper_rate = 10, max_shopper_number = 1000, enqueueShopper = Version2.enqueueShopper)} minutes to complete the run.')
    print('======================================================================')
    time.sleep(2)
    print('Shoppers randomly selecting queues with two express lanes: ')
    print('')
    print(f'It took {runShopping(EQ, new_shopper_rate = 10, max_shopper_number = 1000, enqueueShopper = Version3.enqueueShopper)} minutes to complete the run.')
    print('======================================================================')
    time.sleep(2)
    print('Shoppers selecting shortest queues with two express lanes: ')
    print('')
    print(f'It took {runShopping(EQ, new_shopper_rate = 10, max_shopper_number = 1000, enqueueShopper = Version4.enqueueShopper)} minutes to complete the run.')
    print('======================================================================')


if __name__ == '__main__':
    main()
