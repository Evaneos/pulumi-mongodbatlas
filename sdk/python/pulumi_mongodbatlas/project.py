# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Project(pulumi.CustomResource):
    cluster_count: pulumi.Output[float]
    """
    The number of Atlas clusters deployed in the project..
    """
    created: pulumi.Output[str]
    """
    The ISO-8601-formatted timestamp of when Atlas created the project..
    """
    name: pulumi.Output[str]
    """
    The name of the project you want to create. (Cannot be changed via this Provider after creation.)
    """
    org_id: pulumi.Output[str]
    """
    The ID of the organization you want to create the project within.
    """
    teams: pulumi.Output[list]
    def __init__(__self__, resource_name, opts=None, name=None, org_id=None, teams=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_project` provides a Project resource. This allows project to be created.
        
        > **IMPORTANT WARNING:**  Changing the name of an existing Project in your Terraform configuration will result the destruction of that Project and related resources (including Clusters) and the re-creation of those resources.  Terraform will inform you of the destroyed/created resources before applying so be sure to verify any change to your environment before applying.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the project you want to create. (Cannot be changed via this Provider after creation.)
        :param pulumi.Input[str] org_id: The ID of the organization you want to create the project within.
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

        __props__['teams'] = teams

        __props__['cluster_count'] = None
        __props__['created'] = None

        super(Project, __self__).__init__(
            'mongodbatlas:index/project:Project',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

