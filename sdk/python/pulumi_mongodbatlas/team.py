# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Team(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    The name of the team you want to create.
    """
    org_id: pulumi.Output[str]
    """
    The unique identifier for the organization you want to associate the team with.
    """
    team_id: pulumi.Output[str]
    """
    The unique identifier for the team.
    """
    usernames: pulumi.Output[list]
    """
    You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.
    """
    def __init__(__self__, resource_name, opts=None, name=None, org_id=None, usernames=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_teams` provides a Team resource. The resource lets you create, edit and delete Teams. Also, Teams can be assigned to multiple projects, and team members’ access to the project is determined by the team’s project role.
        
        > **IMPORTANT:** MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.
        
        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        
        MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the team you want to create.
        :param pulumi.Input[str] org_id: The unique identifier for the organization you want to associate the team with.
        :param pulumi.Input[list] usernames: You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.
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

        __props__['name'] = name

        if org_id is None:
            raise TypeError("Missing required property 'org_id'")
        __props__['org_id'] = org_id

        if usernames is None:
            raise TypeError("Missing required property 'usernames'")
        __props__['usernames'] = usernames

        __props__['team_id'] = None

        super(Team, __self__).__init__(
            'mongodbatlas:index/team:Team',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

