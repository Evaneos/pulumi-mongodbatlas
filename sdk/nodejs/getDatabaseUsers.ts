// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_database_users` describe all Database Users. This represents a database user which will be applied to all clusters within the project.
 * 
 * Each user has a set of roles that provide access to the project’s databases. User's roles apply to all the clusters in the project: if two clusters have a `products` database and a user has a role granting `read` access on the products database, the user has that access on both clusters.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testDatabaseUser = new mongodbatlas.DatabaseUser("test", {
 *     authDatabaseName: "admin",
 *     labels: [
 *         {
 *             key: "key 1",
 *             value: "value 1",
 *         },
 *         {
 *             key: "key 2",
 *             value: "value 2",
 *         },
 *     ],
 *     password: "test-acc-password",
 *     projectId: "<PROJECT-ID>",
 *     roles: [
 *         {
 *             databaseName: "admin",
 *             roleName: "readWrite",
 *         },
 *         {
 *             databaseName: "admin",
 *             roleName: "atlasAdmin",
 *         },
 *     ],
 *     username: "test-acc-username",
 * });
 * const testDatabaseUsers = mongodbatlas.getDatabaseUsers({
 *     "mongodbatlas_database_user.test.project_id": [{}],
 *     projectId: "",
 * });
 * ```
 */
export function getDatabaseUsers(args: GetDatabaseUsersArgs, opts?: pulumi.InvokeOptions): Promise<GetDatabaseUsersResult> {
    return pulumi.runtime.invoke("mongodbatlas:index/getDatabaseUsers:getDatabaseUsers", {
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatabaseUsers.
 */
export interface GetDatabaseUsersArgs {
    /**
     * The unique ID for the project to get all database users.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getDatabaseUsers.
 */
export interface GetDatabaseUsersResult {
    /**
     * ID of the Atlas project the user belongs to.
     */
    readonly projectId: string;
    /**
     * A list where each represents a Database user.
     */
    readonly results: { authDatabaseName: string, labels: { key: string, value: string }[], projectId: string, roles: { collectionName: string, databaseName: string, roleName: string }[], username: string, x509Type: string }[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
