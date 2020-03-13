# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetClustersResult:
    """
    A collection of values returned by getClusters.
    """
    def __init__(__self__, plugin=None, project_id=None, results=None, id=None):
        if plugin and not isinstance(plugin, dict):
            raise TypeError("Expected argument 'plugin' to be a dict")
        __self__.plugin = plugin
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        __self__.results = results
        """
        A list where each represents a Cluster. See Cluster below for more details.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_clusters(project_id=None,opts=None):
    """
    `mongodbatlas_cluster` describes all Clusters by the provided project_id. The data source requires your Project ID.
    
    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
    
    > **IMPORTANT:**
    <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
    <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.
    """
    __args__ = dict()

    __args__['projectId'] = project_id
    __ret__ = await pulumi.runtime.invoke('mongodbatlas:index/getClusters:getClusters', __args__, opts=opts)

    return GetClustersResult(
        plugin=__ret__.get('plugin'),
        project_id=__ret__.get('projectId'),
        results=__ret__.get('results'),
        id=__ret__.get('id'))
