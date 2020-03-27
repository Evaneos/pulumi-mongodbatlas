# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetNetworkPeeringContainerResult:
    """
    A collection of values returned by getNetworkPeeringContainer.
    """
    def __init__(__self__, atlas_cidr_block=None, azure_subscription_id=None, container_id=None, gcp_project_id=None, network_name=None, project_id=None, provider_name=None, provisioned=None, region=None, region_name=None, vnet_name=None, vpc_id=None, id=None):
        if atlas_cidr_block and not isinstance(atlas_cidr_block, str):
            raise TypeError("Expected argument 'atlas_cidr_block' to be a str")
        __self__.atlas_cidr_block = atlas_cidr_block
        """
        CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
        """
        if azure_subscription_id and not isinstance(azure_subscription_id, str):
            raise TypeError("Expected argument 'azure_subscription_id' to be a str")
        __self__.azure_subscription_id = azure_subscription_id
        """
        Unique identifer of the Azure subscription in which the VNet resides.
        """
        if container_id and not isinstance(container_id, str):
            raise TypeError("Expected argument 'container_id' to be a str")
        __self__.container_id = container_id
        if gcp_project_id and not isinstance(gcp_project_id, str):
            raise TypeError("Expected argument 'gcp_project_id' to be a str")
        __self__.gcp_project_id = gcp_project_id
        """
        Unique identifier of the GCP project in which the Network Peering connection resides.
        """
        if network_name and not isinstance(network_name, str):
            raise TypeError("Expected argument 'network_name' to be a str")
        __self__.network_name = network_name
        """
        Name of the Network Peering connection in the Atlas project.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        __self__.provider_name = provider_name
        """
        Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
        """
        if provisioned and not isinstance(provisioned, bool):
            raise TypeError("Expected argument 'provisioned' to be a bool")
        __self__.provisioned = provisioned
        """
        Indicates whether the project has Network Peering connections deployed in the container.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        Azure region where the container resides.
        """
        if region_name and not isinstance(region_name, str):
            raise TypeError("Expected argument 'region_name' to be a str")
        __self__.region_name = region_name
        """
        AWS region.
        """
        if vnet_name and not isinstance(vnet_name, str):
            raise TypeError("Expected argument 'vnet_name' to be a str")
        __self__.vnet_name = vnet_name
        """
        The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.
        """
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        __self__.vpc_id = vpc_id
        """
        Unique identifier of the project’s VPC.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_network_peering_container(container_id=None,project_id=None,opts=None):
    """
    `mongodbatlas_network_container` describes a Network Peering Container. The resource requires your Project ID and container ID.
    
    > **IMPORTANT:** This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.
    
    > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
    """
    __args__ = dict()

    __args__['containerId'] = container_id
    __args__['projectId'] = project_id
    __ret__ = await pulumi.runtime.invoke('mongodbatlas:index/getNetworkPeeringContainer:getNetworkPeeringContainer', __args__, opts=opts)

    return GetNetworkPeeringContainerResult(
        atlas_cidr_block=__ret__.get('atlasCidrBlock'),
        azure_subscription_id=__ret__.get('azureSubscriptionId'),
        container_id=__ret__.get('containerId'),
        gcp_project_id=__ret__.get('gcpProjectId'),
        network_name=__ret__.get('networkName'),
        project_id=__ret__.get('projectId'),
        provider_name=__ret__.get('providerName'),
        provisioned=__ret__.get('provisioned'),
        region=__ret__.get('region'),
        region_name=__ret__.get('regionName'),
        vnet_name=__ret__.get('vnetName'),
        vpc_id=__ret__.get('vpcId'),
        id=__ret__.get('id'))