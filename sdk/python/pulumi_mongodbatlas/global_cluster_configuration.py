# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GlobalClusterConfiguration(pulumi.CustomResource):
    cluster_name: pulumi.Output[str]
    custom_zone_mapping: pulumi.Output[dict]
    """
    A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
    """
    custom_zone_mappings: pulumi.Output[list]
    """
    Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
    """
    managed_namespaces: pulumi.Output[list]
    """
    Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    * `cluster_name - (Required) The name of the Global Cluster.
    """
    def __init__(__self__, resource_name, opts=None, cluster_name=None, custom_zone_mappings=None, managed_namespaces=None, project_id=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_global_cluster_config` provides a Global Cluster Configuration resource.
        
        
        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] custom_zone_mappings: Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
        :param pulumi.Input[list] managed_namespaces: Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
               * `cluster_name - (Required) The name of the Global Cluster.
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

        if cluster_name is None:
            raise TypeError("Missing required property 'cluster_name'")
        __props__['cluster_name'] = cluster_name

        __props__['custom_zone_mappings'] = custom_zone_mappings

        __props__['managed_namespaces'] = managed_namespaces

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['custom_zone_mapping'] = None

        super(GlobalClusterConfiguration, __self__).__init__(
            'mongodbatlas:index/globalClusterConfiguration:GlobalClusterConfiguration',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

