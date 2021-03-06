// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_private_endpoint` describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testMongodbatlasPrivateEndpoint = new mongodbatlas.PrivateEndpoint("test", {
 *     projectId: "<PROJECT-ID>",
 *     providerName: "AWS",
 *     region: "us-east-1",
 * });
 * const testPrivateEndpoint = pulumi.all([testMongodbatlasPrivateEndpoint.privateLinkId, testMongodbatlasPrivateEndpoint.projectId]).apply(([privateLinkId, projectId]) => mongodbatlas.getPrivateEndpoint({
 *     privateLinkId: privateLinkId,
 *     projectId: projectId,
 * }));
 * ```
 */
export function getPrivateEndpoint(args: GetPrivateEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetPrivateEndpointResult> {
    return pulumi.runtime.invoke("mongodbatlas:index/getPrivateEndpoint:getPrivateEndpoint", {
        "privateLinkId": args.privateLinkId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getPrivateEndpoint.
 */
export interface GetPrivateEndpointArgs {
    /**
     * Unique identifier of the AWS PrivateLink connection.
     */
    readonly privateLinkId: string;
    /**
     * Unique identifier for the project.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getPrivateEndpoint.
 */
export interface GetPrivateEndpointResult {
    /**
     * Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
     */
    readonly endpointServiceName: string;
    /**
     * Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
     */
    readonly errorMessage: string;
    /**
     * Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
     */
    readonly interfaceEndpoints: string[];
    readonly privateLinkId: string;
    readonly projectId: string;
    /**
     * Status of the AWS PrivateLink connection.
     * Returns one of the following values:
     */
    readonly status: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
