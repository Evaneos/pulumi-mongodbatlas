// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_teams` describes a Team. The resource requires your Organization ID, Project ID and Team ID.
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
func LookupTeam(ctx *pulumi.Context, args *GetTeamArgs) (*GetTeamResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["orgId"] = args.OrgId
		inputs["teamId"] = args.TeamId
	}
	outputs, err := ctx.Invoke("mongodbatlas:index/getTeam:getTeam", inputs)
	if err != nil {
		return nil, err
	}
	return &GetTeamResult{
		Name: outputs["name"],
		OrgId: outputs["orgId"],
		TeamId: outputs["teamId"],
		Usernames: outputs["usernames"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getTeam.
type GetTeamArgs struct {
	// The unique identifier for the organization you want to associate the team with.
	OrgId interface{}
	// The unique identifier for the team.
	TeamId interface{}
}

// A collection of values returned by getTeam.
type GetTeamResult struct {
	// The name of the team you want to create.
	Name interface{}
	OrgId interface{}
	TeamId interface{}
	// The users who are part of the organization.
	Usernames interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}