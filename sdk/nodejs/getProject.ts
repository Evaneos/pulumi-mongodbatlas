// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_project` describes a MongoDB Atlas Project. This represents a project that has been created.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
 * 
 * ## Example Usage
 * 
 * ### Using project_id attribute to query
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testMongodbatlasProject = new mongodbatlas.Project("test", {
 *     orgId: "<ORG_ID>",
 *     teams: [
 *         {
 *             roleNames: ["GROUP_OWNER"],
 *             teamId: "5e0fa8c99ccf641c722fe645",
 *         },
 *         {
 *             roleNames: [
 *                 "GROUP_READ_ONLY",
 *                 "GROUP_DATA_ACCESS_READ_WRITE",
 *             ],
 *             teamId: "5e1dd7b4f2a30ba80a70cd4rw",
 *         },
 *     ],
 * });
 * const testProject = testMongodbatlasProject.id.apply(id => mongodbatlas.getProject({
 *     projectId: id,
 * }));
 * ```
 * 
 * ### Using name attribute to query
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testMongodbatlasProject = new mongodbatlas.Project("test", {
 *     orgId: "<ORG_ID>",
 *     teams: [
 *         {
 *             roleNames: ["GROUP_OWNER"],
 *             teamId: "5e0fa8c99ccf641c722fe645",
 *         },
 *         {
 *             roleNames: [
 *                 "GROUP_READ_ONLY",
 *                 "GROUP_DATA_ACCESS_READ_WRITE",
 *             ],
 *             teamId: "5e1dd7b4f2a30ba80a70cd4rw",
 *         },
 *     ],
 * });
 * const testProject = testMongodbatlasProject.name.apply(name => mongodbatlas.getProject({
 *     name: name,
 * }));
 * ```
 */
export function getProject(args?: GetProjectArgs, opts?: pulumi.InvokeOptions): Promise<GetProjectResult> {
    args = args || {};
    return pulumi.runtime.invoke("mongodbatlas:index/getProject:getProject", {
        "name": args.name,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getProject.
 */
export interface GetProjectArgs {
    /**
     * The unique ID for the project.
     */
    readonly name?: string;
    /**
     * The unique ID for the project.
     */
    readonly projectId?: string;
}

/**
 * A collection of values returned by getProject.
 */
export interface GetProjectResult {
    readonly clusterCount: number;
    readonly created: string;
    /**
     * The name of the project you want to create. (Cannot be changed via this Provider after creation.)
     */
    readonly name?: string;
    /**
     * The ID of the organization you want to create the project within.
     * *`cluster_count` - The number of Atlas clusters deployed in the project.
     * *`created` - The ISO-8601-formatted timestamp of when Atlas created the project.
     * * `teams.#.team_id` - The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.
     * * `teams.#.role_names` - Each string in the array represents a project role assigned to the team. Every user associated with the team inherits these roles.
     * The following are valid roles:
     * * `GROUP_OWNER`
     * * `GROUP_READ_ONLY`
     * * `GROUP_DATA_ACCESS_ADMIN`
     * * `GROUP_DATA_ACCESS_READ_WRITE`
     * * `GROUP_DATA_ACCESS_READ_ONLY`
     * * `GROUP_CLUSTER_MANAGER`
     */
    readonly orgId: string;
    readonly projectId?: string;
    readonly teams: { roleNames: string[], teamId: string }[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}