# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Cluster(pulumi.CustomResource):
    advanced_configuration: pulumi.Output[dict]
    auto_scaling_disk_gb_enabled: pulumi.Output[bool]
    """
    Specifies whether disk auto-scaling is enabled. The default is true.
    - Set to `true` to enable disk auto-scaling.
    - Set to `false` to disable disk auto-scaling.
    """
    backing_provider_name: pulumi.Output[str]
    """
    Cloud service provider on which the server for a multi-tenant cluster is provisioned.
    """
    backup_enabled: pulumi.Output[bool]
    """
    Set to true to enable Atlas continuous backups for the cluster.
    """
    bi_connector: pulumi.Output[dict]
    """
    Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.
    """
    cluster_id: pulumi.Output[str]
    """
    The cluster ID.
    """
    cluster_type: pulumi.Output[str]
    """
    Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.
    """
    disk_size_gb: pulumi.Output[float]
    """
    The size in gigabytes of the server’s root volume. You can add capacity by increasing this number, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
    """
    encryption_at_rest_provider: pulumi.Output[str]
    """
    Set the Encryption at Rest parameter.  Possible values are AWS, GCP, AZURE or NONE.  Requires M10 or greater and for backup_enabled to be false or omitted.
    """
    labels: pulumi.Output[list]
    mongo_db_major_version: pulumi.Output[str]
    """
    Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: `3.6`, `4.0`, or `4.2`. You must set this value to `4.2` if `provider_instance_size_name` is either M2 or M5.
    """
    mongo_db_version: pulumi.Output[str]
    """
    Version of MongoDB the cluster runs, in `major-version`.`minor-version` format.
    """
    mongo_uri: pulumi.Output[str]
    """
    Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.
    """
    mongo_uri_updated: pulumi.Output[str]
    """
    Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.
    """
    mongo_uri_with_options: pulumi.Output[str]
    """
    connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.
    """
    name: pulumi.Output[str]
    """
    Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.
    """
    num_shards: pulumi.Output[float]
    """
    Number of shards to deploy in the specified zone.
    """
    paused: pulumi.Output[bool]
    """
    Flag that indicates whether the cluster is paused or not.
    """
    pit_enabled: pulumi.Output[bool]
    """
    - Flag that indicates if the cluster uses Point-in-Time backups. If set to true, provider_backup_enabled must also be set to true.
    """
    plugin: pulumi.Output[dict]
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    """
    provider_backup_enabled: pulumi.Output[bool]
    """
    Flag indicating if the cluster uses Cloud Provider Snapshots for backups.
    """
    provider_disk_iops: pulumi.Output[float]
    """
    The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.
    """
    provider_disk_type_name: pulumi.Output[str]
    """
    Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: PP4 - 32GB, P6 - 64GB, P10 - 128GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at https://docs.atlas.mongodb.com/reference/api/clusters-create-one/.
    """
    provider_encrypt_ebs_volume: pulumi.Output[bool]
    """
    If enabled, the Amazon EBS encryption feature encrypts the server’s root volume for both data at rest within the volume and for data moving between the volume and the instance.
    """
    provider_instance_size_name: pulumi.Output[str]
    """
    Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See [Create a Cluster](https://docs.atlas.mongodb.com/reference/api/clusters-create-one/) `providerSettings.instanceSizeName` for valid values and default resources.  
    """
    provider_name: pulumi.Output[str]
    """
    Cloud service provider on which the servers are provisioned.
    """
    provider_region_name: pulumi.Output[str]
    """
    Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).
    Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.
    """
    provider_volume_type: pulumi.Output[str]
    """
    The type of the volume. The possible values are: `STANDARD` and `PROVISIONED`.  `PROVISIONED` required if setting IOPS higher than the default instance IOPS.
    """
    replication_factor: pulumi.Output[float]
    """
    Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.
    """
    replication_specs: pulumi.Output[list]
    """
    Configuration for cluster regions.  See Replication Spec below for more details.
    """
    srv_address: pulumi.Output[str]
    """
    Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.
    """
    state_name: pulumi.Output[str]
    """
    Current state of the cluster. The possible states are:
    - IDLE
    - CREATING
    - UPDATING
    - DELETING
    - DELETED
    - REPAIRING
    """
    def __init__(__self__, resource_name, opts=None, advanced_configuration=None, auto_scaling_disk_gb_enabled=None, backing_provider_name=None, backup_enabled=None, bi_connector=None, cluster_type=None, disk_size_gb=None, encryption_at_rest_provider=None, labels=None, mongo_db_major_version=None, name=None, num_shards=None, pit_enabled=None, project_id=None, provider_backup_enabled=None, provider_disk_iops=None, provider_disk_type_name=None, provider_encrypt_ebs_volume=None, provider_instance_size_name=None, provider_name=None, provider_region_name=None, provider_volume_type=None, replication_factor=None, replication_specs=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_cluster` provides a Cluster resource. The resource lets you create, edit and delete clusters. The resource requires your Project ID.
        
        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        
        > **IMPORTANT:**
        <br> &#8226; Free tier cluster creation (M0) is not supported via API or by this Provider.
        <br> &#8226; Shared tier clusters (M2, M5) cannot be upgraded to higher tiers via API or by this Provider. 
        <br> &#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
        <br> &#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_scaling_disk_gb_enabled: Specifies whether disk auto-scaling is enabled. The default is true.
               - Set to `true` to enable disk auto-scaling.
               - Set to `false` to disable disk auto-scaling.
        :param pulumi.Input[str] backing_provider_name: Cloud service provider on which the server for a multi-tenant cluster is provisioned.
        :param pulumi.Input[bool] backup_enabled: Set to true to enable Atlas continuous backups for the cluster.
        :param pulumi.Input[dict] bi_connector: Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.
        :param pulumi.Input[str] cluster_type: Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.
        :param pulumi.Input[float] disk_size_gb: The size in gigabytes of the server’s root volume. You can add capacity by increasing this number, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
        :param pulumi.Input[str] encryption_at_rest_provider: Set the Encryption at Rest parameter.  Possible values are AWS, GCP, AZURE or NONE.  Requires M10 or greater and for backup_enabled to be false or omitted.
        :param pulumi.Input[str] mongo_db_major_version: Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: `3.6`, `4.0`, or `4.2`. You must set this value to `4.2` if `provider_instance_size_name` is either M2 or M5.
        :param pulumi.Input[str] name: Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.
        :param pulumi.Input[float] num_shards: Number of shards to deploy in the specified zone.
        :param pulumi.Input[bool] pit_enabled: - Flag that indicates if the cluster uses Point-in-Time backups. If set to true, provider_backup_enabled must also be set to true.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[bool] provider_backup_enabled: Flag indicating if the cluster uses Cloud Provider Snapshots for backups.
        :param pulumi.Input[float] provider_disk_iops: The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.
        :param pulumi.Input[str] provider_disk_type_name: Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: PP4 - 32GB, P6 - 64GB, P10 - 128GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at https://docs.atlas.mongodb.com/reference/api/clusters-create-one/.
        :param pulumi.Input[bool] provider_encrypt_ebs_volume: If enabled, the Amazon EBS encryption feature encrypts the server’s root volume for both data at rest within the volume and for data moving between the volume and the instance.
        :param pulumi.Input[str] provider_instance_size_name: Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See [Create a Cluster](https://docs.atlas.mongodb.com/reference/api/clusters-create-one/) `providerSettings.instanceSizeName` for valid values and default resources.  
        :param pulumi.Input[str] provider_name: Cloud service provider on which the servers are provisioned.
        :param pulumi.Input[str] provider_region_name: Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).
               Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.
        :param pulumi.Input[str] provider_volume_type: The type of the volume. The possible values are: `STANDARD` and `PROVISIONED`.  `PROVISIONED` required if setting IOPS higher than the default instance IOPS.
        :param pulumi.Input[float] replication_factor: Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.
        :param pulumi.Input[list] replication_specs: Configuration for cluster regions.  See Replication Spec below for more details.
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

        __props__['advanced_configuration'] = advanced_configuration

        __props__['auto_scaling_disk_gb_enabled'] = auto_scaling_disk_gb_enabled

        __props__['backing_provider_name'] = backing_provider_name

        __props__['backup_enabled'] = backup_enabled

        __props__['bi_connector'] = bi_connector

        __props__['cluster_type'] = cluster_type

        __props__['disk_size_gb'] = disk_size_gb

        __props__['encryption_at_rest_provider'] = encryption_at_rest_provider

        __props__['labels'] = labels

        __props__['mongo_db_major_version'] = mongo_db_major_version

        __props__['name'] = name

        __props__['num_shards'] = num_shards

        __props__['pit_enabled'] = pit_enabled

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['provider_backup_enabled'] = provider_backup_enabled

        __props__['provider_disk_iops'] = provider_disk_iops

        __props__['provider_disk_type_name'] = provider_disk_type_name

        __props__['provider_encrypt_ebs_volume'] = provider_encrypt_ebs_volume

        if provider_instance_size_name is None:
            raise TypeError("Missing required property 'provider_instance_size_name'")
        __props__['provider_instance_size_name'] = provider_instance_size_name

        if provider_name is None:
            raise TypeError("Missing required property 'provider_name'")
        __props__['provider_name'] = provider_name

        __props__['provider_region_name'] = provider_region_name

        __props__['provider_volume_type'] = provider_volume_type

        __props__['replication_factor'] = replication_factor

        __props__['replication_specs'] = replication_specs

        __props__['cluster_id'] = None
        __props__['mongo_db_version'] = None
        __props__['mongo_uri'] = None
        __props__['mongo_uri_updated'] = None
        __props__['mongo_uri_with_options'] = None
        __props__['paused'] = None
        __props__['plugin'] = None
        __props__['srv_address'] = None
        __props__['state_name'] = None

        super(Cluster, __self__).__init__(
            'mongodbatlas:index/cluster:Cluster',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

