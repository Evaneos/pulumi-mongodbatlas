// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package mongodbatlas

import (
	"unicode"

	tfhelperschema "github.com/hashicorp/terraform/helper/schema"
	"github.com/hashicorp/terraform/terraform"
	"github.com/pulumi/pulumi-terraform/pkg/tfbridge"
	"github.com/pulumi/pulumi/pkg/resource"
	"github.com/pulumi/pulumi/pkg/tokens"
	"github.com/terraform-providers/terraform-provider-mongodbatlas/mongodbatlas"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "mongodbatlas"
	// modules:
	mainMod = "index" // the y module
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c *terraform.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := mongodbatlas.Provider().(*tfhelperschema.Provider)

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "mongodbatlas",
		Description: "A Pulumi package for creating and managing mongodbatlas cloud resources.",
		Keywords:    []string{"pulumi", "mongodbatlas"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		Repository:  "https://github.com/Evaneos/pulumi-mongodbatlas",
		Config: map[string]*tfbridge.SchemaInfo{
			"publicKey": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"MONGODB_ATLAS_PUBLIC_KEY"},
				},
			},
			"privateKey": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"MONGODB_ATLAS_PRIVATE_KEY"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. Two examples
			// are below - the single line form is the common case. The multi-line form is
			// needed only if you wish to override types or other default options.
			//
			"mongodbatlas_database_user":           {Tok: makeResource(mainMod, "DatabaseUser")},
			"mongodbatlas_project_ip_whitelist":    {Tok: makeResource(mainMod, "ProjectIpWhitelist")},
			"mongodbatlas_cluster":                 {Tok: makeResource(mainMod, "Cluster")},
			"mongodbatlas_network_container":       {Tok: makeResource(mainMod, "NetworkPeeringContainer")},
			"mongodbatlas_project":                 {Tok: makeResource(mainMod, "Project")},
			"mongodbatlas_cloud_provider_snapshot": {Tok: makeResource(mainMod, "CloudProviderSnapshot")},
			"mongodbatlas_cloud_provider_snapshot_restore_job": {
				Tok: makeResource(mainMod, "CloudProviderSnapshotRestoreJob"),
			},
			"mongodbatlas_encryption_at_rest":    {Tok: makeResource(mainMod, "EncryptionAtRest")},
			"mongodbatlas_network_peering":       {Tok: makeResource(mainMod, "NetworkPeeringConnection")},
			"mongodbatlas_private_ip_mode":       {Tok: makeResource(mainMod, "PrivateIpMode")},
			"mongodbatlas_maintenance_window":    {Tok: makeResource(mainMod, "MaintenanceWindow")},
			"mongodbatlas_auditing":              {Tok: makeResource(mainMod, "Auditing")},
			"mongodbatlas_team":                  {Tok: makeResource(mainMod, "Team")},
			"mongodbatlas_custom_db_role":        {Tok: makeResource(mainMod, "CustomDbRole")},
			"mongodbatlas_global_cluster_config": {Tok: makeResource(mainMod, "GlobalClusterConfiguration")},
			"mongodbatlas_alert_configuration":   {Tok: makeResource(mainMod, "AlertConfiguration")},
			"mongodbatlas_private_endpoint":      {Tok: makeResource(mainMod, "PrivateEndpoint")},
			"mongodbatlas_private_endpoint_interface_link": {
				Tok: makeResource(mainMod, "PrivateEndpointInterfaceLink"),
			},
			"mongodbatlas_x509_authentication_database_user": {
				Tok: makeResource(mainMod, "X509AuthenticationDatabaseUser"),
			},
			//
			// "aws_acm_certificate": {
			// 	Tok: makeResource(mainMod, "Certificate"),
			// 	Fields: map[string]*tfbridge.SchemaInfo{
			// 		"tags": {Type: makeType(mainPkg, "Tags")},
			// 	},
			// },
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			"mongodbatlas_database_user":            {Tok: makeDataSource(mainMod, "getDatabaseUser")},
			"mongodbatlas_database_users":           {Tok: makeDataSource(mainMod, "getDatabaseUsers")},
			"mongodbatlas_project":                  {Tok: makeDataSource(mainMod, "getProject")},
			"mongodbatlas_projects":                 {Tok: makeDataSource(mainMod, "getProjects")},
			"mongodbatlas_cluster":                  {Tok: makeDataSource(mainMod, "getCluster")},
			"mongodbatlas_clusters":                 {Tok: makeDataSource(mainMod, "getClusters")},
			"mongodbatlas_cloud_provider_snapshot":  {Tok: makeDataSource(mainMod, "getCloudProviderSnapshot")},
			"mongodbatlas_cloud_provider_snapshots": {Tok: makeDataSource(mainMod, "getCloudProviderSnapshots")},
			"mongodbatlas_cloud_provider_snapshot_restore_job": {
				Tok: makeDataSource(mainMod, "getCloudProviderSnapshotRestoreJob"),
			},
			"mongodbatlas_cloud_provider_snapshot_restore_jobs": {
				Tok: makeDataSource(mainMod, "getCloudProviderSnapshotRestoreJobs"),
			},
			"mongodbatlas_network_container":   {Tok: makeDataSource(mainMod, "getNetworkPeeringContainer")},
			"mongodbatlas_network_containers":  {Tok: makeDataSource(mainMod, "getNetworkPeeringContainers")},
			"mongodbatlas_network_peering":     {Tok: makeDataSource(mainMod, "getNetworkPeeringConnection")},
			"mongodbatlas_network_peerings":    {Tok: makeDataSource(mainMod, "getNetworkPeeringConnections")},
			"mongodbatlas_maintenance_window":  {Tok: makeDataSource(mainMod, "getMaintenanceWindow")},
			"mongodbatlas_auditing":            {Tok: makeDataSource(mainMod, "getAuditing")},
			"mongodbatlas_custom_db_roles":     {Tok: makeDataSource(mainMod, "getCustomDbRoles")},
			"mongodbatlas_custom_db_role":      {Tok: makeDataSource(mainMod, "getCustomDbRole")},
			"mongodbatlas_alert_configuration": {Tok: makeDataSource(mainMod, "getAlertConfiguration")},
			"mongodbatlas_team":                {Tok: makeDataSource(mainMod, "getTeam")},
			"mongodbatlas_private_endpoint":    {Tok: makeDataSource(mainMod, "getPrivateEndpoint")},
			"mongodbatlas_private_endpoint_interface_link": {
				Tok: makeDataSource(mainMod, "getPrivateEndpointInterfaceLink"),
			},
			"mongodbatlas_x509_authentication_database_user": {
				Tok: makeDataSource(mainMod, "getX509AuthenticationDatabaseUser"),
			},
			"mongodbatlas_global_cluster_config": {Tok: makeDataSource(mainMod, "getGlobalClusterConfig")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "latest",
			},
			DevDependencies: map[string]string{
				"@types/node": "^8.0.25", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			//Overlay: &tfbridge.OverlayInfo{},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=0.17.28",
			},
		},
	}

	// For all resources with name properties, we will add an auto-name property.  Make sure to skip those that
	// already have a name mapping entry, since those may have custom overrides set above (e.g., for length).
	const nameProperty = "name"
	for resname, res := range prov.Resources {
		if schema := p.ResourcesMap[resname]; schema != nil {
			// Only apply auto-name to input properties (Optional || Required) named `name`
			if tfs, has := schema.Schema[nameProperty]; has && (tfs.Optional || tfs.Required) {
				if _, hasfield := res.Fields[nameProperty]; !hasfield {
					if res.Fields == nil {
						res.Fields = make(map[string]*tfbridge.SchemaInfo)
					}
					res.Fields[nameProperty] = tfbridge.AutoName(nameProperty, 255)
				}
			}
		}
	}

	return prov
}
