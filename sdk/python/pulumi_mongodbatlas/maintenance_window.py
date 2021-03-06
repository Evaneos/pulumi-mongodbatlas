# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class MaintenanceWindow(pulumi.CustomResource):
    day_of_week: pulumi.Output[float]
    """
    Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.
    """
    defer: pulumi.Output[bool]
    """
    Defer maintenance for the given project for one week.
    """
    hour_of_day: pulumi.Output[float]
    """
    Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).
    """
    number_of_deferrals: pulumi.Output[float]
    """
    Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.
    """
    project_id: pulumi.Output[str]
    """
    The unique identifier of the project for the Maintenance Window.
    """
    start_asap: pulumi.Output[bool]
    """
    Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.
    """
    def __init__(__self__, resource_name, opts=None, day_of_week=None, defer=None, hour_of_day=None, number_of_deferrals=None, project_id=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_maintenance_window` provides a resource to schedule a maintenance window for your MongoDB Atlas Project and/or set to defer a scheduled maintenance up to two times.
        
        > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
        
        ## Maintenance Window Considerations:
        
        - Urgent Maintenance Activities Cannot Wait: Urgent maintenance activities such as security patches cannot wait for your chosen window. Atlas will start those maintenance activities when needed.
        
        Once maintenance is scheduled for your cluster, you cannot change your maintenance window until the current maintenance efforts have completed.
        - Maintenance Requires Replica Set Elections: Atlas performs maintenance the same way as the manual maintenance procedure. This requires at least one replica set election during the maintenance window per replica set.
        - Maintenance Starts As Close to the Hour As Possible: Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or expected system issues could delay the start time.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] day_of_week: Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.
        :param pulumi.Input[bool] defer: Defer maintenance for the given project for one week.
        :param pulumi.Input[float] hour_of_day: Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).
        :param pulumi.Input[float] number_of_deferrals: Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.
        :param pulumi.Input[str] project_id: The unique identifier of the project for the Maintenance Window.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['day_of_week'] = day_of_week

        __props__['defer'] = defer

        __props__['hour_of_day'] = hour_of_day

        __props__['number_of_deferrals'] = number_of_deferrals

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['start_asap'] = None

        super(MaintenanceWindow, __self__).__init__(
            'mongodbatlas:index/maintenanceWindow:MaintenanceWindow',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

