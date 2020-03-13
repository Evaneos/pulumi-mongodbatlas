// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_network_container` describes a Network Peering Container. The resource requires your Project ID and container ID.
// 
// > **IMPORTANT:** This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
func LookupNetworkPeeringContainer(ctx *pulumi.Context, args *GetNetworkPeeringContainerArgs) (*GetNetworkPeeringContainerResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["containerId"] = args.ContainerId
		inputs["projectId"] = args.ProjectId
	}
	outputs, err := ctx.Invoke("mongodbatlas:index/getNetworkPeeringContainer:getNetworkPeeringContainer", inputs)
	if err != nil {
		return nil, err
	}
	return &GetNetworkPeeringContainerResult{
		AtlasCidrBlock: outputs["atlasCidrBlock"],
		AzureSubscriptionId: outputs["azureSubscriptionId"],
		ContainerId: outputs["containerId"],
		GcpProjectId: outputs["gcpProjectId"],
		NetworkName: outputs["networkName"],
		ProjectId: outputs["projectId"],
		ProviderName: outputs["providerName"],
		Provisioned: outputs["provisioned"],
		Region: outputs["region"],
		RegionName: outputs["regionName"],
		VnetName: outputs["vnetName"],
		VpcId: outputs["vpcId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getNetworkPeeringContainer.
type GetNetworkPeeringContainerArgs struct {
	// The Network Peering Container ID.
	ContainerId interface{}
	// The unique ID for the project to create the database user.
	ProjectId interface{}
}

// A collection of values returned by getNetworkPeeringContainer.
type GetNetworkPeeringContainerResult struct {
	// CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
	AtlasCidrBlock interface{}
	// Unique identifer of the Azure subscription in which the VNet resides.
	AzureSubscriptionId interface{}
	ContainerId interface{}
	// Unique identifier of the GCP project in which the Network Peering connection resides.
	GcpProjectId interface{}
	// Name of the Network Peering connection in the Atlas project.
	NetworkName interface{}
	ProjectId interface{}
	// Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
	ProviderName interface{}
	// Indicates whether the project has Network Peering connections deployed in the container.
	Provisioned interface{}
	// Azure region where the container resides.
	Region interface{}
	// AWS region.
	RegionName interface{}
	// The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.
	VnetName interface{}
	// Unique identifier of the project’s VPC.
	VpcId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
