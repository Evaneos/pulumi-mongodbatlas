// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * `mongodbatlas_x509_authentication_database_user` provides a X509 Authentication Database User resource. The mongodbatlas_x509_authentication_database_user resource lets you manage MongoDB users who authenticate using X.509 certificates. You can manage these X.509 certificates or let Atlas do it for you.
 * 
 * | Management  | Description  |
 * |---|---|
 * | Atlas  | Atlas manages your Certificate Authority and can generate certificates for your MongoDB users. No additional X.509 configuration is required.  |
 * | Customer  |  You must provide a Certificate Authority and generate certificates for your MongoDB users. |
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
 * 
 * ## Example Usages
 * 
 * ### Example Usage: Generate an Atlas-managed X.509 certificate for a MongoDB user
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const user = new mongodbatlas.DatabaseUser("user", {
 *     databaseName: "$external",
 *     labels: [{
 *         key: "My Key",
 *         value: "My Value",
 *     }],
 *     projectId: "<PROJECT-ID>",
 *     roles: [{
 *         databaseName: "admin",
 *         roleName: "atlasAdmin",
 *     }],
 *     username: "myUsername",
 *     x509Type: "MANAGED",
 * });
 * const test = new mongodbatlas.X509AuthenticationDatabaseUser("test", {
 *     monthsUntilExpiration: 2,
 *     projectId: user.projectId,
 *     username: user.username,
 * });
 * ```
 * 
 * ### Example Usage: Save a customer-managed X.509 configuration for an Atlas project
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const test = new mongodbatlas.X509AuthenticationDatabaseUser("test", {
 *     customerX509Cas: `  -----BEGIN CERTIFICATE-----
 *   MIICmTCCAgICCQDZnHzklxsT9TANBgkqhkiG9w0BAQsFADCBkDELMAkGA1UEBhMC
 *   VVMxDjAMBgNVBAgMBVRleGFzMQ8wDQYDVQQHDAZBdXN0aW4xETAPBgNVBAoMCHRl
 *   c3QuY29tMQ0wCwYDVQQLDARUZXN0MREwDwYDVQQDDAh0ZXN0LmNvbTErMCkGCSqG
 *   SIb3DQEJARYcbWVsaXNzYS5wbHVua2V0dEBtb25nb2RiLmNvbTAeFw0yMDAyMDQy
 *   MDQ2MDFaFw0yMTAyMDMyMDQ2MDFaMIGQMQswCQYDVQQGEwJVUzEOMAwGA1UECAwF
 *   VGV4YXMxDzANBgNVBAcMBkF1c3RpbjERMA8GA1UECgwIdGVzdC5jb20xDTALBgNV
 *   BAsMBFRlc3QxETAPBgNVBAMMCHRlc3QuY29tMSswKQYJKoZIhvcNAQkBFhxtZWxp
 *   c3NhLnBsdW5rZXR0QG1vbmdvZGIuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB
 *   iQKBgQCf1LRqr1zftzdYx2Aj9G76tb0noMPtj6faGLlPji1+m6Rn7RWD9L0ntWAr
 *   cURxvypa9jZ9MXFzDtLevvd3tHEmfrUT3ukNDX6+Jtc4kWm+Dh2A70Pd+deKZ2/O
 *   Fh8audEKAESGXnTbeJCeQa1XKlIkjqQHBNwES5h1b9vJtFoLJwIDAQABMA0GCSqG
 *   SIb3DQEBCwUAA4GBADMUncjEPV/MiZUcVNGmktP6BPmEqMXQWUDpdGW2+Tg2JtUA
 *   7MMILtepBkFzLO+GlpZxeAlXO0wxiNgEmCRONgh4+t2w3e7a8GFijYQ99FHrAC5A
 *   iul59bdl18gVqXia1Yeq/iK7Ohfy/Jwd7Hsm530elwkM/ZEkYDjBlZSXYdyz
 *   -----END CERTIFICATE-----"
 * `,
 *     projectId: "<PROJECT-ID>",
 * });
 * ```
 */
export class X509AuthenticationDatabaseUser extends pulumi.CustomResource {
    /**
     * Get an existing X509AuthenticationDatabaseUser resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: X509AuthenticationDatabaseUserState, opts?: pulumi.CustomResourceOptions): X509AuthenticationDatabaseUser {
        return new X509AuthenticationDatabaseUser(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mongodbatlas:index/x509AuthenticationDatabaseUser:X509AuthenticationDatabaseUser';

    /**
     * Returns true if the given object is an instance of X509AuthenticationDatabaseUser.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is X509AuthenticationDatabaseUser {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === X509AuthenticationDatabaseUser.__pulumiType;
    }

    /**
     * Array of objects where each details one unexpired database user certificate.
     */
    public /*out*/ readonly certificates!: pulumi.Output<{ createdAt: string, groupId: string, id: number, notAfter: string, subject: string }[]>;
    /**
     * Contains the last X.509 certificate and private key created for a database user.
     */
    public /*out*/ readonly currentCertificate!: pulumi.Output<string>;
    /**
     * PEM string containing one or more customer CAs for database user authentication.
     */
    public readonly customerX509Cas!: pulumi.Output<string | undefined>;
    /**
     * A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.
     */
    public readonly monthsUntilExpiration!: pulumi.Output<number | undefined>;
    /**
     * Identifier for the Atlas project associated with the X.509 configuration.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Username of the database user to create a certificate for.
     */
    public readonly username!: pulumi.Output<string | undefined>;

    /**
     * Create a X509AuthenticationDatabaseUser resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: X509AuthenticationDatabaseUserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: X509AuthenticationDatabaseUserArgs | X509AuthenticationDatabaseUserState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as X509AuthenticationDatabaseUserState | undefined;
            inputs["certificates"] = state ? state.certificates : undefined;
            inputs["currentCertificate"] = state ? state.currentCertificate : undefined;
            inputs["customerX509Cas"] = state ? state.customerX509Cas : undefined;
            inputs["monthsUntilExpiration"] = state ? state.monthsUntilExpiration : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as X509AuthenticationDatabaseUserArgs | undefined;
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["customerX509Cas"] = args ? args.customerX509Cas : undefined;
            inputs["monthsUntilExpiration"] = args ? args.monthsUntilExpiration : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["certificates"] = undefined /*out*/;
            inputs["currentCertificate"] = undefined /*out*/;
        }
        super(X509AuthenticationDatabaseUser.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering X509AuthenticationDatabaseUser resources.
 */
export interface X509AuthenticationDatabaseUserState {
    /**
     * Array of objects where each details one unexpired database user certificate.
     */
    readonly certificates?: pulumi.Input<pulumi.Input<{ createdAt?: pulumi.Input<string>, groupId?: pulumi.Input<string>, id?: pulumi.Input<number>, notAfter?: pulumi.Input<string>, subject?: pulumi.Input<string> }>[]>;
    /**
     * Contains the last X.509 certificate and private key created for a database user.
     */
    readonly currentCertificate?: pulumi.Input<string>;
    /**
     * PEM string containing one or more customer CAs for database user authentication.
     */
    readonly customerX509Cas?: pulumi.Input<string>;
    /**
     * A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.
     */
    readonly monthsUntilExpiration?: pulumi.Input<number>;
    /**
     * Identifier for the Atlas project associated with the X.509 configuration.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Username of the database user to create a certificate for.
     */
    readonly username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a X509AuthenticationDatabaseUser resource.
 */
export interface X509AuthenticationDatabaseUserArgs {
    /**
     * PEM string containing one or more customer CAs for database user authentication.
     */
    readonly customerX509Cas?: pulumi.Input<string>;
    /**
     * A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.
     */
    readonly monthsUntilExpiration?: pulumi.Input<number>;
    /**
     * Identifier for the Atlas project associated with the X.509 configuration.
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Username of the database user to create a certificate for.
     */
    readonly username?: pulumi.Input<string>;
}
