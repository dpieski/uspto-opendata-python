# -*- coding: utf-8 -*-
# (c) 2017 Andreas Motl <andreas@ip-tools.org>
import celery
from uspto.oac.client import UsptoOfficeActionCitationsClient
from uspto.util.tasks import GenericDownloadTask, AsynchronousDownloader

class UsptoOfficeActionCitationsDownloadTask(GenericDownloadTask):
    name = 'uspto.oac.tasks.UsptoOfficeActionCitationsDownloadTask'
    client_factory = UsptoOfficeActionCitationsClient

@celery.shared_task(bind=True, base=UsptoOfficeActionCitationsDownloadTask)
def download_task(self, query, options=None):
    """
    https://celery.readthedocs.io/en/latest/userguide/tasks.html#basics
    http://docs.celeryproject.org/en/latest/whatsnew-4.0.html#the-task-base-class-no-longer-automatically-register-tasks
    """
    return self.process(query, options)

class UsptoOfficeActionCitationsDownloader(AsynchronousDownloader):
    task_function = download_task
