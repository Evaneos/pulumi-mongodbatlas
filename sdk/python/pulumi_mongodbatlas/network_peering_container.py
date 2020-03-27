# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class NetworkPeeringContainer(pulumi.CustomResource):
    atlas_cidr_block: pulumi.Output[str]
    """
    CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
    """
    azure_subscription_id: pulumi.Output[str]
    """
    Unique identifer of the Azure subscription in which the VNet resides.
    """
    container_id: pulumi.Output[str]
    """
    The Network Peering Container ID.
    """
    gcp_project_id: pulumi.Output[str]
    """
    Unique identifier of the GCP project in which the Network Peering connection resides.
    """
    network_name: pulumi.Output[str]
    """
    Name of the Network Peering connection in the Atlas project.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    """
    provider_name: pulumi.Output[str]
    """
    Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
    """
    provisioned: pulumi.Output[bool]
    """
    Indicates whether the project has Network Peering connections deployed in the container.
    """
    region: pulumi.Output[str]
    """
    Azure region where the container resides.
    """
    region_name: pulumi.Output[str]
    """
    AWS region.
    """
    vnet_name: pulumi.Output[str]
    """
    The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.
    """
    vpc_id: pulumi.Output[str]
    """
    Unique identifier of the project’s VPC.
    """
    def __init__(__self__, resource_name, opts=None, atlas_cidr_block=None, project_id=None, provider_name=None, region=None, region_name=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_network_container` provides a Network Peering Container resource. The resource lets you create, edit and delete network peering containers. The resource requires your Project ID.
        
        > **IMPORTANT:** This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.
        
        The following table outlines the maximum number of Network Peering containers per cloud provider:
        * Cloud Provider:  GCP - Container Limit: One container per project.
        * Cloud Provider:  AWS and Azure - Container Limit: One container per cloud provider region.
        
        > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] atlas_cidr_block: CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] provider_name: Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
        :param pulumi.Input[str] region: Azure region where the container resides.
        :param pulumi.Input[str] region_name: AWS region.
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

        if atlas_cidr_block is None:
            raise TypeError("Missing required property 'atlas_cidr_block'")
        __props__['atlas_cidr_block'] = atlas_cidr_block

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['provider_name'] = provider_name

        __props__['region'] = region

        __props__['region_name'] = region_name

        __props__['azure_subscription_id'] = None
        __props__['container_id'] = None
        __props__['gcp_project_id'] = None
        __props__['network_name'] = None
        __props__['provisioned'] = None
        __props__['vnet_name'] = None
        __props__['vpc_id'] = None

        super(NetworkPeeringContainer, __self__).__init__(
            'mongodbatlas:index/networkPeeringContainer:NetworkPeeringContainer',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

