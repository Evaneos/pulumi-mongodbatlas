# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class PrivateEndpoint(pulumi.CustomResource):
    endpoint_service_name: pulumi.Output[str]
    """
    Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
    """
    error_message: pulumi.Output[str]
    """
    Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
    """
    interface_endpoints: pulumi.Output[list]
    """
    Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
    """
    private_link_id: pulumi.Output[str]
    """
    Unique identifier of the AWS PrivateLink connection.
    """
    project_id: pulumi.Output[str]
    """
    Required 	Unique identifier for the project.
    """
    provider_name: pulumi.Output[str]
    region: pulumi.Output[str]
    """
    Cloud provider region in which you want to create the private endpoint connection.
    Accepted values are:
    * `us-east-1`
    * `us-east-2`
    * `us-west-1`
    * `us-west-2`
    * `ca-central-1`
    * `sa-east-1`
    * `eu-north-1`
    * `eu-west-1`
    * `eu-west-2`
    * `eu-west-3`
    * `eu-central-1`
    * `me-south-1`
    * `ap-northeast-1`
    * `ap-northeast-2`
    * `ap-south-1`
    * `ap-southeast-1`
    * `ap-southeast-2`
    * `ap-east-1`
    """
    status: pulumi.Output[str]
    """
    Status of the AWS PrivateLink connection.
    Returns one of the following values:
    """
    def __init__(__self__, resource_name, opts=None, project_id=None, provider_name=None, region=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_private_endpoint` provides a Private Endpoint resource. This represents a Private Endpoint Connection that can be created in an Atlas project.
        
        > **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
          * Organization Owner
          * Project Owner
        
        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: Required 	Unique identifier for the project.
        :param pulumi.Input[str] region: Cloud provider region in which you want to create the private endpoint connection.
               Accepted values are:
               * `us-east-1`
               * `us-east-2`
               * `us-west-1`
               * `us-west-2`
               * `ca-central-1`
               * `sa-east-1`
               * `eu-north-1`
               * `eu-west-1`
               * `eu-west-2`
               * `eu-west-3`
               * `eu-central-1`
               * `me-south-1`
               * `ap-northeast-1`
               * `ap-northeast-2`
               * `ap-south-1`
               * `ap-southeast-1`
               * `ap-southeast-2`
               * `ap-east-1`
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

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        if provider_name is None:
            raise TypeError("Missing required property 'provider_name'")
        __props__['provider_name'] = provider_name

        if region is None:
            raise TypeError("Missing required property 'region'")
        __props__['region'] = region

        __props__['endpoint_service_name'] = None
        __props__['error_message'] = None
        __props__['interface_endpoints'] = None
        __props__['private_link_id'] = None
        __props__['status'] = None

        super(PrivateEndpoint, __self__).__init__(
            'mongodbatlas:index/privateEndpoint:PrivateEndpoint',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
