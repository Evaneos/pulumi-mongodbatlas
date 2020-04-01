# MongoDB Atlas Resource Provider

The MongoDB Atlas resource provider for Pulumi lets you manage MongoDB Atlas resources in your cloud programs. To use
this package, please [install the Pulumi CLI first](https://pulumi.io/).

## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @evaneos/pulumi-mongodbatlas

or `yarn`:

    $ yarn add @evaneos/pulumi-mongodbatlas

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/Evaneos/pulumi-mongodbatlas/sdk/go/...

## Configuration

The following configuration points are available for the `mongodbatlas` provider:

- `mongodbatlas:privateKey` (environment: `MONGODB_ATLAS_PRIVATE_KEY`) -  the MongoDB Atlas API private_key
- `mongodbatlas:publicKey` (environment: `MONGODB_ATLAS_PUBLIC_KEY`) -  the MongoDB Atlas API public_key

## Reference

For detailed reference documentation, please visit [the API docs][1].


[1]: https://pulumi.io/reference/pkg/nodejs/pulumi/x/
