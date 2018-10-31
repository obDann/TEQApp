class OutputQueue():
    '''
    A Queue that contains output for a console
    '''

    def __init__(self):
        '''
        (OutputQueue) -> None

        Initializes an OuputQueue
        '''
        # REPRESENTATION INVARIANT
        # self._q is a list
        #
        # The output queue is empty when self._q == []
        #
        # objects are held in the form of FIFO
        # For objects that are enqueued:
        #     self._q[0] is the earliest object that was enqueued
        #     self._q[-1] is the lastest object that was enqueued
        # If the Output Queue is not empty and an object is dequeued:
        #     self._q[0] is returned, and self._q[0] = self._q[1:]
        self._q = []

    def is_empty(self):
        '''
        (OutputQueue) -> bool

        Returns true iff the OutputQueue is empty
        '''
        return self._q == []

    def enqueue(self, obj):
        '''
        (OutputQueue, str or a dataframe) -> None

        Enqueues an object to the queue
        '''
        self._q.append(obj)

    def dequeue(self):
        '''
        (OutputQueue) -> str or a dataframe

        Dequeues an object from the queue if the queue is not empty.

        Returns none if the queue is empty
        '''
        # check if the queue is empty
        if self.is_empty():
            # if it is, return None
            return None
        # otherwise dequeue the first object
        return self._q.pop(0)

    def how_many(self):
        '''
        (OutputQueue) -> int

        Returns the number of objects in the queue
        '''
        # just return the length of the queue
        return len(self._q)