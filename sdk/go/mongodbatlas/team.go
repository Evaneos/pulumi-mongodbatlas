// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_teams` provides a Team resource. The resource lets you create, edit and delete Teams. Also, Teams can be assigned to multiple projects, and team members’ access to the project is determined by the team’s project role.
// 
// > **IMPORTANT:** MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
// 
// MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.
type Team struct {
	s *pulumi.ResourceState
}

// NewTeam registers a new resource with the given unique name, arguments, and options.
func NewTeam(ctx *pulumi.Context,
	name string, args *TeamArgs, opts ...pulumi.ResourceOpt) (*Team, error) {
	if args == nil || args.OrgId == nil {
		return nil, errors.New("missing required argument 'OrgId'")
	}
	if args == nil || args.Usernames == nil {
		return nil, errors.New("missing required argument 'Usernames'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["name"] = nil
		inputs["orgId"] = nil
		inputs["usernames"] = nil
	} else {
		inputs["name"] = args.Name
		inputs["orgId"] = args.OrgId
		inputs["usernames"] = args.Usernames
	}
	inputs["teamId"] = nil
	s, err := ctx.RegisterResource("mongodbatlas:index/team:Team", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Team{s: s}, nil
}

// GetTeam gets an existing Team resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTeam(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TeamState, opts ...pulumi.ResourceOpt) (*Team, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["name"] = state.Name
		inputs["orgId"] = state.OrgId
		inputs["teamId"] = state.TeamId
		inputs["usernames"] = state.Usernames
	}
	s, err := ctx.ReadResource("mongodbatlas:index/team:Team", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Team{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Team) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Team) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The name of the team you want to create.
func (r *Team) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The unique identifier for the organization you want to associate the team with.
func (r *Team) OrgId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["orgId"])
}

// The unique identifier for the team.
func (r *Team) TeamId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["teamId"])
}

// You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.
func (r *Team) Usernames() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["usernames"])
}

// Input properties used for looking up and filtering Team resources.
type TeamState struct {
	// The name of the team you want to create.
	Name interface{}
	// The unique identifier for the organization you want to associate the team with.
	OrgId interface{}
	// The unique identifier for the team.
	TeamId interface{}
	// You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.
	Usernames interface{}
}

// The set of arguments for constructing a Team resource.
type TeamArgs struct {
	// The name of the team you want to create.
	Name interface{}
	// The unique identifier for the organization you want to associate the team with.
	OrgId interface{}
	// You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.
	Usernames interface{}
}
