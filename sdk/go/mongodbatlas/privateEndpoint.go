// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_private_endpoint` provides a Private Endpoint resource. This represents a Private Endpoint Connection that can be created in an Atlas project.
// 
// > **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
//   * Organization Owner
//   * Project Owner
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
type PrivateEndpoint struct {
	s *pulumi.ResourceState
}

// NewPrivateEndpoint registers a new resource with the given unique name, arguments, and options.
func NewPrivateEndpoint(ctx *pulumi.Context,
	name string, args *PrivateEndpointArgs, opts ...pulumi.ResourceOpt) (*PrivateEndpoint, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.ProviderName == nil {
		return nil, errors.New("missing required argument 'ProviderName'")
	}
	if args == nil || args.Region == nil {
		return nil, errors.New("missing required argument 'Region'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["projectId"] = nil
		inputs["providerName"] = nil
		inputs["region"] = nil
	} else {
		inputs["projectId"] = args.ProjectId
		inputs["providerName"] = args.ProviderName
		inputs["region"] = args.Region
	}
	inputs["endpointServiceName"] = nil
	inputs["errorMessage"] = nil
	inputs["interfaceEndpoints"] = nil
	inputs["privateLinkId"] = nil
	inputs["status"] = nil
	s, err := ctx.RegisterResource("mongodbatlas:index/privateEndpoint:PrivateEndpoint", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &PrivateEndpoint{s: s}, nil
}

// GetPrivateEndpoint gets an existing PrivateEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivateEndpoint(ctx *pulumi.Context,
	name string, id pulumi.ID, state *PrivateEndpointState, opts ...pulumi.ResourceOpt) (*PrivateEndpoint, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["endpointServiceName"] = state.EndpointServiceName
		inputs["errorMessage"] = state.ErrorMessage
		inputs["interfaceEndpoints"] = state.InterfaceEndpoints
		inputs["privateLinkId"] = state.PrivateLinkId
		inputs["projectId"] = state.ProjectId
		inputs["providerName"] = state.ProviderName
		inputs["region"] = state.Region
		inputs["status"] = state.Status
	}
	s, err := ctx.ReadResource("mongodbatlas:index/privateEndpoint:PrivateEndpoint", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &PrivateEndpoint{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *PrivateEndpoint) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *PrivateEndpoint) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
func (r *PrivateEndpoint) EndpointServiceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["endpointServiceName"])
}

// Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
func (r *PrivateEndpoint) ErrorMessage() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["errorMessage"])
}

// Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
func (r *PrivateEndpoint) InterfaceEndpoints() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["interfaceEndpoints"])
}

// Unique identifier of the AWS PrivateLink connection.
func (r *PrivateEndpoint) PrivateLinkId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateLinkId"])
}

// Required 	Unique identifier for the project.
func (r *PrivateEndpoint) ProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["projectId"])
}

func (r *PrivateEndpoint) ProviderName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["providerName"])
}

// Cloud provider region in which you want to create the private endpoint connection.
// Accepted values are:
// * `us-east-1`
// * `us-east-2`
// * `us-west-1`
// * `us-west-2`
// * `ca-central-1`
// * `sa-east-1`
// * `eu-north-1`
// * `eu-west-1`
// * `eu-west-2`
// * `eu-west-3`
// * `eu-central-1`
// * `me-south-1`
// * `ap-northeast-1`
// * `ap-northeast-2`
// * `ap-south-1`
// * `ap-southeast-1`
// * `ap-southeast-2`
// * `ap-east-1`
func (r *PrivateEndpoint) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// Status of the AWS PrivateLink connection.
// Returns one of the following values:
func (r *PrivateEndpoint) Status() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["status"])
}

// Input properties used for looking up and filtering PrivateEndpoint resources.
type PrivateEndpointState struct {
	// Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
	EndpointServiceName interface{}
	// Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
	ErrorMessage interface{}
	// Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
	InterfaceEndpoints interface{}
	// Unique identifier of the AWS PrivateLink connection.
	PrivateLinkId interface{}
	// Required 	Unique identifier for the project.
	ProjectId interface{}
	ProviderName interface{}
	// Cloud provider region in which you want to create the private endpoint connection.
	// Accepted values are:
	// * `us-east-1`
	// * `us-east-2`
	// * `us-west-1`
	// * `us-west-2`
	// * `ca-central-1`
	// * `sa-east-1`
	// * `eu-north-1`
	// * `eu-west-1`
	// * `eu-west-2`
	// * `eu-west-3`
	// * `eu-central-1`
	// * `me-south-1`
	// * `ap-northeast-1`
	// * `ap-northeast-2`
	// * `ap-south-1`
	// * `ap-southeast-1`
	// * `ap-southeast-2`
	// * `ap-east-1`
	Region interface{}
	// Status of the AWS PrivateLink connection.
	// Returns one of the following values:
	Status interface{}
}

// The set of arguments for constructing a PrivateEndpoint resource.
type PrivateEndpointArgs struct {
	// Required 	Unique identifier for the project.
	ProjectId interface{}
	ProviderName interface{}
	// Cloud provider region in which you want to create the private endpoint connection.
	// Accepted values are:
	// * `us-east-1`
	// * `us-east-2`
	// * `us-west-1`
	// * `us-west-2`
	// * `ca-central-1`
	// * `sa-east-1`
	// * `eu-north-1`
	// * `eu-west-1`
	// * `eu-west-2`
	// * `eu-west-3`
	// * `eu-central-1`
	// * `me-south-1`
	// * `ap-northeast-1`
	// * `ap-northeast-2`
	// * `ap-south-1`
	// * `ap-southeast-1`
	// * `ap-southeast-2`
	// * `ap-east-1`
	Region interface{}
}
