# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetCloudProviderSnapshotsResult:
    """
    A collection of values returned by getCloudProviderSnapshots.
    """
    def __init__(__self__, cluster_name=None, project_id=None, results=None, total_count=None, id=None):
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        __self__.cluster_name = cluster_name
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        __self__.results = results
        """
        Includes cloudProviderSnapshot object for each item detailed in the results array section.
        """
        if total_count and not isinstance(total_count, float):
            raise TypeError("Expected argument 'total_count' to be a float")
        __self__.total_count = total_count
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_cloud_provider_snapshots(cluster_name=None,project_id=None,opts=None):
    """
    `mongodbatlas_cloud_provider_snapshots` provides an Cloud Provider Snapshot entry datasource. Atlas Cloud Provider Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service provider.
    
    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
    """
    __args__ = dict()

    __args__['clusterName'] = cluster_name
    __args__['projectId'] = project_id
    __ret__ = await pulumi.runtime.invoke('mongodbatlas:index/getCloudProviderSnapshots:getCloudProviderSnapshots', __args__, opts=opts)

    return GetCloudProviderSnapshotsResult(
        cluster_name=__ret__.get('clusterName'),
        project_id=__ret__.get('projectId'),
        results=__ret__.get('results'),
        total_count=__ret__.get('totalCount'),
        id=__ret__.get('id'))