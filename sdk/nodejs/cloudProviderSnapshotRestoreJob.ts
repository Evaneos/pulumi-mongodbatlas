// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_cloud_provider_snapshot_restore_job` provides a resource to create a new restore job from a cloud provider snapshot of a specified cluster. The restore job can be one of two types: 
 * * **automated:** Atlas automatically restores the snapshot with snapshotId to the Atlas cluster with name targetClusterName in the Atlas project with targetGroupId.
 * 
 * * **download:** Atlas provides a URL to download a .tar.gz of the snapshot with snapshotId. The contents of the archive contain the data files for your Atlas cluster.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
 */
export class CloudProviderSnapshotRestoreJob extends pulumi.CustomResource {
    /**
     * Get an existing CloudProviderSnapshotRestoreJob resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CloudProviderSnapshotRestoreJobState, opts?: pulumi.CustomResourceOptions): CloudProviderSnapshotRestoreJob {
        return new CloudProviderSnapshotRestoreJob(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mongodbatlas:index/cloudProviderSnapshotRestoreJob:CloudProviderSnapshotRestoreJob';

    /**
     * Returns true if the given object is an instance of CloudProviderSnapshotRestoreJob.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CloudProviderSnapshotRestoreJob {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CloudProviderSnapshotRestoreJob.__pulumiType;
    }

    /**
     * Indicates whether the restore job was canceled.
     */
    public /*out*/ readonly cancelled!: pulumi.Output<boolean>;
    /**
     * The name of the Atlas cluster whose snapshot you want to restore.
     */
    public readonly clusterName!: pulumi.Output<string>;
    /**
     * UTC ISO 8601 formatted point in time when Atlas created the restore job.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * Type of restore job to create. Possible values are: **download** or **automated**, only one must be set it in ``true``.
     */
    public readonly deliveryType!: pulumi.Output<{ automated?: boolean, download?: boolean, targetClusterName?: string, targetProjectId?: string }>;
    /**
     * One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.
     */
    public /*out*/ readonly deliveryUrls!: pulumi.Output<string[]>;
    /**
     * Indicates whether the restore job expired.
     */
    public /*out*/ readonly expired!: pulumi.Output<boolean>;
    /**
     * UTC ISO 8601 formatted point in time when the restore job expires.
     */
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    /**
     * UTC ISO 8601 formatted point in time when the restore job completed.
     */
    public /*out*/ readonly finishedAt!: pulumi.Output<string>;
    /**
     * The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Unique identifier of the snapshot to restore.
     */
    public readonly snapshotId!: pulumi.Output<string>;
    /**
     * The unique identifier of the restore job.
     */
    public /*out*/ readonly snapshotRestoreJobId!: pulumi.Output<string>;
    /**
     * Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.
     */
    public /*out*/ readonly timestamp!: pulumi.Output<string>;

    /**
     * Create a CloudProviderSnapshotRestoreJob resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CloudProviderSnapshotRestoreJobArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CloudProviderSnapshotRestoreJobArgs | CloudProviderSnapshotRestoreJobState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as CloudProviderSnapshotRestoreJobState | undefined;
            inputs["cancelled"] = state ? state.cancelled : undefined;
            inputs["clusterName"] = state ? state.clusterName : undefined;
            inputs["createdAt"] = state ? state.createdAt : undefined;
            inputs["deliveryType"] = state ? state.deliveryType : undefined;
            inputs["deliveryUrls"] = state ? state.deliveryUrls : undefined;
            inputs["expired"] = state ? state.expired : undefined;
            inputs["expiresAt"] = state ? state.expiresAt : undefined;
            inputs["finishedAt"] = state ? state.finishedAt : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["snapshotId"] = state ? state.snapshotId : undefined;
            inputs["snapshotRestoreJobId"] = state ? state.snapshotRestoreJobId : undefined;
            inputs["timestamp"] = state ? state.timestamp : undefined;
        } else {
            const args = argsOrState as CloudProviderSnapshotRestoreJobArgs | undefined;
            if (!args || args.clusterName === undefined) {
                throw new Error("Missing required property 'clusterName'");
            }
            if (!args || args.deliveryType === undefined) {
                throw new Error("Missing required property 'deliveryType'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            if (!args || args.snapshotId === undefined) {
                throw new Error("Missing required property 'snapshotId'");
            }
            inputs["clusterName"] = args ? args.clusterName : undefined;
            inputs["deliveryType"] = args ? args.deliveryType : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["snapshotId"] = args ? args.snapshotId : undefined;
            inputs["cancelled"] = undefined /*out*/;
            inputs["createdAt"] = undefined /*out*/;
            inputs["deliveryUrls"] = undefined /*out*/;
            inputs["expired"] = undefined /*out*/;
            inputs["expiresAt"] = undefined /*out*/;
            inputs["finishedAt"] = undefined /*out*/;
            inputs["snapshotRestoreJobId"] = undefined /*out*/;
            inputs["timestamp"] = undefined /*out*/;
        }
        super(CloudProviderSnapshotRestoreJob.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CloudProviderSnapshotRestoreJob resources.
 */
export interface CloudProviderSnapshotRestoreJobState {
    /**
     * Indicates whether the restore job was canceled.
     */
    readonly cancelled?: pulumi.Input<boolean>;
    /**
     * The name of the Atlas cluster whose snapshot you want to restore.
     */
    readonly clusterName?: pulumi.Input<string>;
    /**
     * UTC ISO 8601 formatted point in time when Atlas created the restore job.
     */
    readonly createdAt?: pulumi.Input<string>;
    /**
     * Type of restore job to create. Possible values are: **download** or **automated**, only one must be set it in ``true``.
     */
    readonly deliveryType?: pulumi.Input<{ automated?: pulumi.Input<boolean>, download?: pulumi.Input<boolean>, targetClusterName?: pulumi.Input<string>, targetProjectId?: pulumi.Input<string> }>;
    /**
     * One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.
     */
    readonly deliveryUrls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Indicates whether the restore job expired.
     */
    readonly expired?: pulumi.Input<boolean>;
    /**
     * UTC ISO 8601 formatted point in time when the restore job expires.
     */
    readonly expiresAt?: pulumi.Input<string>;
    /**
     * UTC ISO 8601 formatted point in time when the restore job completed.
     */
    readonly finishedAt?: pulumi.Input<string>;
    /**
     * The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Unique identifier of the snapshot to restore.
     */
    readonly snapshotId?: pulumi.Input<string>;
    /**
     * The unique identifier of the restore job.
     */
    readonly snapshotRestoreJobId?: pulumi.Input<string>;
    /**
     * Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.
     */
    readonly timestamp?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a CloudProviderSnapshotRestoreJob resource.
 */
export interface CloudProviderSnapshotRestoreJobArgs {
    /**
     * The name of the Atlas cluster whose snapshot you want to restore.
     */
    readonly clusterName: pulumi.Input<string>;
    /**
     * Type of restore job to create. Possible values are: **download** or **automated**, only one must be set it in ``true``.
     */
    readonly deliveryType: pulumi.Input<{ automated?: pulumi.Input<boolean>, download?: pulumi.Input<boolean>, targetClusterName?: pulumi.Input<string>, targetProjectId?: pulumi.Input<string> }>;
    /**
     * The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Unique identifier of the snapshot to restore.
     */
    readonly snapshotId: pulumi.Input<string>;
}
