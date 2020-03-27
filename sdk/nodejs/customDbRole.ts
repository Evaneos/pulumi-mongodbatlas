// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_custom_db_role` provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.
 * 
 * > **IMPORTANT** Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.
 * 
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testRole = new mongodbatlas.CustomDbRole("test_role", {
 *     actions: [
 *         {
 *             action: "UPDATE",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *         {
 *             action: "INSERT",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *         {
 *             action: "REMOVE",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *     ],
 *     projectId: "<PROJECT-ID>",
 *     roleName: "myCustomRole",
 * });
 * ```
 * 
 * ## Example Usage with inherited roles
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const inheritedRoleOne = new mongodbatlas.CustomDbRole("inherited_role_one", {
 *     actions: [{
 *         action: "INSERT",
 *         resources: [{
 *             collectionName: "",
 *             databaseName: "anyDatabase",
 *         }],
 *     }],
 *     projectId: "<PROJECT-ID>",
 *     roleName: "insertRole",
 * });
 * const inheritedRoleTwo = new mongodbatlas.CustomDbRole("inherited_role_two", {
 *     actions: [{
 *         action: "SERVER_STATUS",
 *         resources: [{
 *             cluster: true,
 *         }],
 *     }],
 *     projectId: inheritedRoleOne.projectId,
 *     roleName: "statusServerRole",
 * });
 * const testRole = new mongodbatlas.CustomDbRole("test_role", {
 *     actions: [
 *         {
 *             action: "UPDATE",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *         {
 *             action: "REMOVE",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *     ],
 *     inheritedRoles: [
 *         {
 *             databaseName: "admin",
 *             roleName: inheritedRoleOne.roleName,
 *         },
 *         {
 *             databaseName: "admin",
 *             roleName: inheritedRoleTwo.roleName,
 *         },
 *     ],
 *     projectId: inheritedRoleOne.projectId,
 *     roleName: "myCustomRole",
 * });
 * ```
 */
export class CustomDbRole extends pulumi.CustomResource {
    /**
     * Get an existing CustomDbRole resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomDbRoleState, opts?: pulumi.CustomResourceOptions): CustomDbRole {
        return new CustomDbRole(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mongodbatlas:index/customDbRole:CustomDbRole';

    /**
     * Returns true if the given object is an instance of CustomDbRole.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CustomDbRole {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CustomDbRole.__pulumiType;
    }

    public readonly actions!: pulumi.Output<{ action: string, resources: { cluster?: boolean, collectionName?: string, databaseName?: string }[] }[]>;
    public readonly inheritedRoles!: pulumi.Output<{ databaseName: string, roleName: string }[] | undefined>;
    /**
     * The unique ID for the project to create the database user.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Name of the inherited role. This can either be another custom role or a built-in role.
     */
    public readonly roleName!: pulumi.Output<string>;

    /**
     * Create a CustomDbRole resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CustomDbRoleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CustomDbRoleArgs | CustomDbRoleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CustomDbRoleState | undefined;
            inputs["actions"] = state ? state.actions : undefined;
            inputs["inheritedRoles"] = state ? state.inheritedRoles : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["roleName"] = state ? state.roleName : undefined;
        } else {
            const args = argsOrState as CustomDbRoleArgs | undefined;
            if (!args || args.actions === undefined) {
                throw new Error("Missing required property 'actions'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            if (!args || args.roleName === undefined) {
                throw new Error("Missing required property 'roleName'");
            }
            inputs["actions"] = args ? args.actions : undefined;
            inputs["inheritedRoles"] = args ? args.inheritedRoles : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["roleName"] = args ? args.roleName : undefined;
        }
        super(CustomDbRole.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CustomDbRole resources.
 */
export interface CustomDbRoleState {
    readonly actions?: pulumi.Input<pulumi.Input<{ action: pulumi.Input<string>, resources: pulumi.Input<pulumi.Input<{ cluster?: pulumi.Input<boolean>, collectionName?: pulumi.Input<string>, databaseName?: pulumi.Input<string> }>[]> }>[]>;
    readonly inheritedRoles?: pulumi.Input<pulumi.Input<{ databaseName: pulumi.Input<string>, roleName: pulumi.Input<string> }>[]>;
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Name of the inherited role. This can either be another custom role or a built-in role.
     */
    readonly roleName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CustomDbRole resource.
 */
export interface CustomDbRoleArgs {
    readonly actions: pulumi.Input<pulumi.Input<{ action: pulumi.Input<string>, resources: pulumi.Input<pulumi.Input<{ cluster?: pulumi.Input<boolean>, collectionName?: pulumi.Input<string>, databaseName?: pulumi.Input<string> }>[]> }>[]>;
    readonly inheritedRoles?: pulumi.Input<pulumi.Input<{ databaseName: pulumi.Input<string>, roleName: pulumi.Input<string> }>[]>;
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Name of the inherited role. This can either be another custom role or a built-in role.
     */
    readonly roleName: pulumi.Input<string>;
}
