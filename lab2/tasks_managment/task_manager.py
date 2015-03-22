__author__ = 'mandriy'

from threading import Lock


class TaskIdError(Exception):

    def __init__(self, message, task_id):
        Exception.__init__(self)
        self.task_id = task_id
        self.message = 'Handle error with id %s. Reason: %s.' % (task_id, message)

    def get_task_id(self):
        return self.task_id


class EmptyTaskStack(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class TaskSystem:

    def __init__(self):
        self.__max_task_id__ = 0
        self.__available_tasks__ = {}
        self.__active_tasks__ = {}
        self.__done_tasks__ = {}
        self.__mutex__ = Lock()

    def __submit_task__(self, task_id, result):
        raise Exception('Abstract method call.')

    def __rollback_task__(self, task_id):
        raise Exception('Abstract method call.')

    def __get_task__(self):
        raise Exception('Abstract method call.')

    def __cover__(self, cover_func, *args):
        try:
            self.__mutex__.acquire()
            return cover_func(*args)
        finally:
            self.__mutex__.release()

    def system_snapshot(self):
        return self.__cover__(lambda: {"active": len(self.__active_tasks__),
                                       "available": len(self.__available_tasks__),
                                       "done": len(self.__done_tasks__)})

    def submit_task(self, task_id, result):
        return self.__cover__(self.__submit_task__, task_id, result)

    def rollback_task(self, task_id):
        return self.__cover__(self.__rollback_task__, task_id)

    def get_task(self):
        return self.__cover__(self.__get_task__)


class TextTaskSystem(TaskSystem):

    def __init__(self):
        TaskSystem.__init__(self)

    def load_tasks(self, texts):
        self.__mutex__.acquire()
        for text in texts:
            self.__active_tasks__[self.__max_task_id__] = text
            self.__max_task_id__ += 1
        self.__mutex__.release()

    def __get_task__(self):
        if self.__available_tasks__.keys():
            task_id = self.__available_tasks__.keys()[0]
            self.__active_tasks__[task_id] = self.__available_tasks__[task_id]
            del self.__available_tasks__[task_id]
            return task_id, self.__active_tasks__[task_id]
        else:
            raise EmptyTaskStack("There is no available tasks.")

    def __submit_task__(self, task_id, result):
        if not self.__done_tasks__[task_id]:
            if self.__active_tasks__[task_id]:
                del self.__active_tasks__[task_id]
                self.__done_tasks__[task_id] = result
            else:
                raise TaskIdError("Trying to submit result of task which is inactive.", task_id)
        else:
            raise TaskIdError("Trying to submit result of already done task.", task_id)

    def __rollback_task__(self, task_id):
        if task_id in self.__active_tasks__:
            self.__available_tasks__[task_id] = self.__active_tasks__[task_id]
            del self.__active_tasks__[task_id]
        else:
            raise TaskIdError("Trying to rollback inactive task.", task_id)
