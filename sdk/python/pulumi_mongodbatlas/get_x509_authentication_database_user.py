# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class GetX509AuthenticationDatabaseUserResult:
    """
    A collection of values returned by getX509AuthenticationDatabaseUser.
    """
    def __init__(__self__, certificates=None, customer_x509_cas=None, project_id=None, username=None, id=None):
        if certificates and not isinstance(certificates, list):
            raise TypeError("Expected argument 'certificates' to be a list")
        __self__.certificates = certificates
        """
        Array of objects where each details one unexpired database user certificate.
        """
        if customer_x509_cas and not isinstance(customer_x509_cas, str):
            raise TypeError("Expected argument 'customer_x509_cas' to be a str")
        __self__.customer_x509_cas = customer_x509_cas
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        __self__.username = username
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_x509_authentication_database_user(project_id=None,username=None,opts=None):
    """
    `mongodbatlas_x509_authentication_database_user` describe a X509 Authentication Database User. This represents a X509 Authentication Database User.
    
    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
    """
    __args__ = dict()

    __args__['projectId'] = project_id
    __args__['username'] = username
    __ret__ = await pulumi.runtime.invoke('mongodbatlas:index/getX509AuthenticationDatabaseUser:getX509AuthenticationDatabaseUser', __args__, opts=opts)

    return GetX509AuthenticationDatabaseUserResult(
        certificates=__ret__.get('certificates'),
        customer_x509_cas=__ret__.get('customerX509Cas'),
        project_id=__ret__.get('projectId'),
        username=__ret__.get('username'),
        id=__ret__.get('id'))
