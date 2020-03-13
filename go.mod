module github.com/Evaneos/pulumi-mongodbatlas

go 1.12

replace (
	github.com/Nvveen/Gotty => github.com/ijc25/Gotty v0.0.0-20170406111628-a8b993ba6abd
	github.com/golang/glog => github.com/pulumi/glog v0.0.0-20180820174630-7eaa6ffb71e4
)

require (
	github.com/hashicorp/terraform v0.12.1
	github.com/pkg/errors v0.8.0
	github.com/pulumi/pulumi v0.17.10
	github.com/pulumi/pulumi-terraform v0.18.3
	github.com/stretchr/testify v1.4.0
	github.com/terraform-providers/terraform-provider-mongodbatlas v0.4.1
)
