// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_network_container` describes a Network Peering Container. The resource requires your Project ID and container ID.
 * 
 * > **IMPORTANT:** This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
 */
export function getNetworkPeeringContainer(args: GetNetworkPeeringContainerArgs, opts?: pulumi.InvokeOptions): Promise<GetNetworkPeeringContainerResult> {
    return pulumi.runtime.invoke("mongodbatlas:index/getNetworkPeeringContainer:getNetworkPeeringContainer", {
        "containerId": args.containerId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getNetworkPeeringContainer.
 */
export interface GetNetworkPeeringContainerArgs {
    /**
     * The Network Peering Container ID.
     */
    readonly containerId: string;
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getNetworkPeeringContainer.
 */
export interface GetNetworkPeeringContainerResult {
    /**
     * CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
     */
    readonly atlasCidrBlock: string;
    /**
     * Unique identifer of the Azure subscription in which the VNet resides.
     */
    readonly azureSubscriptionId: string;
    readonly containerId: string;
    /**
     * Unique identifier of the GCP project in which the Network Peering connection resides.
     */
    readonly gcpProjectId: string;
    /**
     * Name of the Network Peering connection in the Atlas project.
     */
    readonly networkName: string;
    readonly projectId: string;
    /**
     * Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
     */
    readonly providerName: string;
    /**
     * Indicates whether the project has Network Peering connections deployed in the container.
     */
    readonly provisioned: boolean;
    /**
     * Azure region where the container resides.
     */
    readonly region: string;
    /**
     * AWS region.
     */
    readonly regionName: string;
    /**
     * The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.
     */
    readonly vnetName: string;
    /**
     * Unique identifier of the project’s VPC.
     */
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}