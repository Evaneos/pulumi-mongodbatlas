// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_network_peerings` describes all Network Peering Connections.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
 * 
 * 
 * ## Example Usage
 * 
 * ### Basic Example (AWS).
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testNetworkPeeringConnection = new mongodbatlas.NetworkPeeringConnection("test", {
 *     accepterRegionName: "us-east-1",
 *     awsAccountId: "abc123abc123",
 *     containerId: "507f1f77bcf86cd799439011",
 *     projectId: "<YOUR-PROJEC-ID>",
 *     providerName: "AWS",
 *     routeTableCidrBlock: "192.168.0.0/24",
 *     vpcId: "vpc-abc123abc123",
 * });
 * const testNetworkPeeringConnections = mongodbatlas.getNetworkPeeringConnections({
 *     "mongodbatlas_network_peering.test.project_id": [{}],
 *     projectId: "",
 * });
 * ```
 */
export function getNetworkPeeringConnections(args: GetNetworkPeeringConnectionsArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkPeeringConnectionsResult> {
    return pulumi.runtime.invoke("mongodbatlas:index/getNetworkPeeringConnections:getNetworkPeeringConnections", {
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getNetworkPeeringConnections.
 */
export interface GetNetworkPeeringConnectionsArgs {
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getNetworkPeeringConnections.
 */
export interface GetNetworkPeeringConnectionsResult {
    readonly projectId: string;
    /**
     * A list where each represents a Network Peering Connection.
     */
    readonly results: { accepterRegionName: string, atlasCidrBlock: string, awsAccountId: string, azureDirectoryId: string, azureSubscriptionId: string, connectionId: string, containerId: string, errorMessage: string, errorState: string, errorStateName: string, gcpProjectId: string, networkName: string, peeringId: string, providerName: string, resourceGroupName: string, routeTableCidrBlock: string, status: string, statusName: string, vnetName: string, vpcId: string }[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
