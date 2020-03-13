# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class PrivateIpMode(pulumi.CustomResource):
    enabled: pulumi.Output[bool]
    """
    Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to enable Only Private IP Mode.
    """
    def __init__(__self__, resource_name, opts=None, enabled=None, project_id=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_private_ip_mode` provides a Private IP Mode resource. This allows one to enable/disable Connect via Peering Only mode for a MongoDB Atlas Project.
        
        
        > **IMPORTANT**: <br>**What is Connect via Peering Only Mode?** <br>Connect via Peering Only mode prevents clusters in an Atlas project from connecting to any network destination other than an Atlas Network Peer. Connect via Peering Only mode applies only to **GCP** and **Azure-backed** dedicated clusters. This setting disables the ability to: <br><br>• Deploy non-GCP or Azure-backed dedicated clusters in an Atlas project, and
        <br>• Use MongoDB Stitch with dedicated clusters in an Atlas project.
        
        
        > **NOTE:** You should create one private_ip_mode per project.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project.
        :param pulumi.Input[str] project_id: The unique ID for the project to enable Only Private IP Mode.
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

        if enabled is None:
            raise TypeError("Missing required property 'enabled'")
        __props__['enabled'] = enabled

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        super(PrivateIpMode, __self__).__init__(
            'mongodbatlas:index/privateIpMode:PrivateIpMode',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

