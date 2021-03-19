# Examples
The examples are organized per version folders.

## Versions 1.1 and 1.2
The versions 1.1 and 1.2 relate to the CVRF schema of that version.

## Version 2.0
Inside the version 2.0 folder the file name prefixes group
the surrogates per random schema use selection.

### Positive Testcases
The mappings from prefix to which criterion is in use are as follows:

* `random-` - Full schema
* `document-only` - Full document schema part
* `document-spam` - Mandatory document schema part
* `document-and-product-` - Full document and product schema parts
* `document-and-vulnerability-` - Full document and vulnerabilities schema parts


### Negative Testcases
The mappings from prefix to which criterion is in use are as follows:

* `document-invalid` - as `document-only`, but mandatory document schema parts missing
* `document-and-product-invalid` - as `document-and-product-`, but mandatory document schema parts missing
* `document-and-vulnerability-invalid` - as `document-and-vulnerability-`, but mandatory document schema parts missing

