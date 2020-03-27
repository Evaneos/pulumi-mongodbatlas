// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_global_cluster_config` describes all managed namespaces and custom zone mappings associated with the specified Global Cluster.
// 
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
func LookupGlobalClusterConfig(ctx *pulumi.Context, args *GetGlobalClusterConfigArgs) (*GetGlobalClusterConfigResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["clusterName"] = args.ClusterName
		inputs["managedNamespaces"] = args.ManagedNamespaces
		inputs["projectId"] = args.ProjectId
	}
	outputs, err := ctx.Invoke("mongodbatlas:index/getGlobalClusterConfig:getGlobalClusterConfig", inputs)
	if err != nil {
		return nil, err
	}
	return &GetGlobalClusterConfigResult{
		ClusterName: outputs["clusterName"],
		CustomZoneMapping: outputs["customZoneMapping"],
		ManagedNamespaces: outputs["managedNamespaces"],
		ProjectId: outputs["projectId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getGlobalClusterConfig.
type GetGlobalClusterConfigArgs struct {
	ClusterName interface{}
	ManagedNamespaces interface{}
	// The unique ID for the project to create the database user.
	// * `cluster_name - (Required) The name of the Global Cluster.
	ProjectId interface{}
}

// A collection of values returned by getGlobalClusterConfig.
type GetGlobalClusterConfigResult struct {
	ClusterName interface{}
	// A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
	CustomZoneMapping interface{}
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces interface{}
	ProjectId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}