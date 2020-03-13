# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class CustomDbRole(pulumi.CustomResource):
    actions: pulumi.Output[list]
    inherited_roles: pulumi.Output[list]
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    """
    role_name: pulumi.Output[str]
    """
    Name of the inherited role. This can either be another custom role or a built-in role.
    """
    def __init__(__self__, resource_name, opts=None, actions=None, inherited_roles=None, project_id=None, role_name=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_custom_db_role` provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.
        
        > **IMPORTANT** Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.
        
        
        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] role_name: Name of the inherited role. This can either be another custom role or a built-in role.
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

        if actions is None:
            raise TypeError("Missing required property 'actions'")
        __props__['actions'] = actions

        __props__['inherited_roles'] = inherited_roles

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        if role_name is None:
            raise TypeError("Missing required property 'role_name'")
        __props__['role_name'] = role_name

        super(CustomDbRole, __self__).__init__(
            'mongodbatlas:index/customDbRole:CustomDbRole',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

