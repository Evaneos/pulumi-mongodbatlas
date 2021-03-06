# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetMaintenanceWindowResult:
    """
    A collection of values returned by getMaintenanceWindow.
    """
    def __init__(__self__, day_of_week=None, hour_of_day=None, number_of_deferrals=None, project_id=None, start_asap=None, id=None):
        if day_of_week and not isinstance(day_of_week, float):
            raise TypeError("Expected argument 'day_of_week' to be a float")
        __self__.day_of_week = day_of_week
        """
        Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.
        """
        if hour_of_day and not isinstance(hour_of_day, float):
            raise TypeError("Expected argument 'hour_of_day' to be a float")
        __self__.hour_of_day = hour_of_day
        """
        Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12  (Time zone is UTC).
        """
        if number_of_deferrals and not isinstance(number_of_deferrals, float):
            raise TypeError("Expected argument 'number_of_deferrals' to be a float")
        __self__.number_of_deferrals = number_of_deferrals
        """
        Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if start_asap and not isinstance(start_asap, bool):
            raise TypeError("Expected argument 'start_asap' to be a bool")
        __self__.start_asap = start_asap
        """
        Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_maintenance_window(project_id=None,opts=None):
    """
    `mongodbatlas_maintenance_window` provides a Maintenance Window entry datasource. Gets information regarding the configured maintenance window for a MongoDB Atlas project.
    
    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
    """
    __args__ = dict()

    __args__['projectId'] = project_id
    __ret__ = await pulumi.runtime.invoke('mongodbatlas:index/getMaintenanceWindow:getMaintenanceWindow', __args__, opts=opts)

    return GetMaintenanceWindowResult(
        day_of_week=__ret__.get('dayOfWeek'),
        hour_of_day=__ret__.get('hourOfDay'),
        number_of_deferrals=__ret__.get('numberOfDeferrals'),
        project_id=__ret__.get('projectId'),
        start_asap=__ret__.get('startAsap'),
        id=__ret__.get('id'))
