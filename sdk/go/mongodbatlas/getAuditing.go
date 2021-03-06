// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// `mongodbatlas_auditing` describes a Auditing.
// 
// > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
func LookupAuditing(ctx *pulumi.Context, args *GetAuditingArgs) (*GetAuditingResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["projectId"] = args.ProjectId
	}
	outputs, err := ctx.Invoke("mongodbatlas:index/getAuditing:getAuditing", inputs)
	if err != nil {
		return nil, err
	}
	return &GetAuditingResult{
		AuditAuthorizationSuccess: outputs["auditAuthorizationSuccess"],
		AuditFilter: outputs["auditFilter"],
		ConfigurationType: outputs["configurationType"],
		Enabled: outputs["enabled"],
		ProjectId: outputs["projectId"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getAuditing.
type GetAuditingArgs struct {
	// The unique ID for the project to create the database user.
	ProjectId interface{}
}

// A collection of values returned by getAuditing.
type GetAuditingResult struct {
	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess interface{}
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter interface{}
	// Denotes the configuration method for the audit filter. Possible values are: NONE - auditing not configured for the project.m FILTER_BUILDER - auditing configured via Atlas UI filter builderm FILTER_JSON - auditing configured via Atlas custom filter or API.
	ConfigurationType interface{}
	// Denotes whether or not the project associated with the {GROUP-ID} has database auditing enabled.
	Enabled interface{}
	ProjectId interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
