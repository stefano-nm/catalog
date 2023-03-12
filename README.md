# Catalog

## Objects

**Service**

- `name` (str): Name of the service.
- `endpoint` (str): Uri endpoint of the service.

## Methods

**GET** /catalog

Returns a list of `Service` objects.

No Parameters.

**GET** /service

Returns a `Service` object.

Parameters:

- `name` (str): Name of the service.

**POST** /register

Appends a service to the catalog.

Parameters:

- `name` (str): Name of the service.
- `endpoint` (str): Endpoint uri of the service.
- `token` (str, Optional): A secret token which can be used to update or unregister the service.

**DELETE** /unregister

Removes a service from the catalog.

Parameters:

- `name` (str): Name of the service.
- `token` (str, Optional): Same token used in the register method.
