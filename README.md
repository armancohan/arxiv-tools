## arXiv-tools

#### Prerequisites 

ArXiv provides [bulk data access](https://github.com/user/repo/blob/branch/other_file.md) through [Amazon S3](https://aws.amazon.com/s3). You need an account with [Amazon AWS](https://aws.amazon.com/free) to be able to download the data. You also need python 2.


#### Downloading arXiv documents
1- Install [s3cmd](https://github.com/s3tools/s3cmd) which is a command line tool for interacting with S3

`pip install s3cmd` (only works on python 2)

2- Configure your s3cmd by entering credentials found in the account management tab of the Amazon AWS website

`s3cmd --configure`

3- Get the manifest files:

The complete set of arXiv files available from Amazon S3 in requester pays buckets. The files are in .tar format each with ~500MB size. You need to have the keys to these chunks to be able to download them. The complete list of these keys is provided in the `manifest` files. First download the manifests:

For PDF documents:

`s3cmd get --requester-pays s3://arxiv/pdf/arXiv_pdf_manifest.xml local-directory/arXiv_pdf_manifest.xml`

For source documents:

`s3cmd get --requester-pays s3://arxiv/src/arXiv_src_manifest.xml local-directory/arXiv_src_manifest.xml`

4- Download the actual pdf and source files using the `download.py` script

Download pdf files:

`python download.py --manifest-file /path/to/pdf-manifest --mode pdf --output-dir /path/to/output`

Download source files:

`python download.py --manifest-file /path/to/src-manifest --mode src --output-dir /path/to/output`

This will download all the files in the directory that you designated as output. 

If you also need the metadata, use [metha](https://github.com/miku/metha) to bulk download the metadata.


