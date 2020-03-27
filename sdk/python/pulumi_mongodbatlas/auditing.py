# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class Auditing(pulumi.CustomResource):
    audit_authorization_success: pulumi.Output[bool]
    """
    JSON-formatted audit filter used by the project
    """
    audit_filter: pulumi.Output[str]
    """
    Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
    """
    configuration_type: pulumi.Output[str]
    """
    Denotes the configuration method for the audit filter. Possible values are: 
    * NONE - auditing not configured for the project.
    * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
    * FILTER_JSON - auditing configured via Atlas custom filter or API.
    """
    enabled: pulumi.Output[bool]
    """
    Denotes whether or not the project associated with the {project_id} has database auditing enabled.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to configure auditing.
    """
    def __init__(__self__, resource_name, opts=None, audit_authorization_success=None, audit_filter=None, enabled=None, project_id=None, __name__=None, __opts__=None):
        """
        `mongodbatlas_auditing` provides an Auditing resource. This allows auditing to be created.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_authorization_success: JSON-formatted audit filter used by the project
        :param pulumi.Input[str] audit_filter: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['audit_authorization_success'] = audit_authorization_success

        __props__['audit_filter'] = audit_filter

        __props__['enabled'] = enabled

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['configuration_type'] = None

        super(Auditing, __self__).__init__(
            'mongodbatlas:index/auditing:Auditing',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
