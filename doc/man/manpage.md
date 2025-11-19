# NAME

`git-ipfs` - Git IPFS helper programs

# SYNOPSIS
*git ipfs* [-h | -\-help]  
*git ipfs release* [-h | -\-help] [-\-prefix [PREFIX]] [-p] [-z] \<tag\> [ipns_key]  
*git ipfs clone* [-h | -\-help] [-t TIMEOUT] [-r [REMOTE_NAME]] [-b [BRANCH]] [-n [USERNAME]] [-p [PASSWORD]] \<ipfs_id\> \<directory\> \<api_url\> [api_port]  
*git ipfs install* [-h | -\-help] [-t TIMEOUT] [-r [REMOTE_NAME]] [-n [USERNAME]] [-p [PASSWORD]] [-\-check-ipfs] \<api_url\> [api_port] [ipfs_id]  
*git ipfs uninstall* [-h | -\-help] [-p] [-r [REMOTE_NAME]]  
*git ipfs config* [-h | -\-help] \<configuration_command\>  
*git ipfs config print*  
*git ipfs config generate* [-h | -\-help] [-s] [-c] [-f [FILENAME]] [-y] [-\-url [URL]] [-\-port [PORT]] [-\-api-version-prefix [API_VERSION_PREFIX]] [-t [TIMEOUT]] [-\-unpin-old] [-r] [-\-ttl [TTL]] [-v [{0,1}]] [-n [USERNAME]] [-p [PASSWORD]]  
*git ipfs config manage* [-h | -\-help] [-\-dry-run] [-\-reset] [-\-url [URL]] [-\-port [PORT]] [-\-api-version-prefix [API_VERSION_PREFIX]] [-t [TIMEOUT]] [-\-unpin-old [UNPIN_OLD]] [-r [REPUBLISH]] [-\-ttl [TTL]] [-v [{0,1}]] [-n [USERNAME]] [-p [PASSWORD]]  
*git ipfs config edit*

# DESCRIPTION 

Git IPFS helper programs add `ipfs://` protocol prefix and backend to **git-remote**(1) management pipeline. It is the set of programs written in Python 3 which allow Git user to clone, push, fetch, self-host or release Git repositories over IPFS decentralized data storage system.

# COMMANDS

Key principle: *git ipfs* \<command\> \<mode\> \[options\] \<arguments\>

The **-\-help** option exists everywhere, and it prints the help message and/or all available options of the given command or mode.

## CLONE

*git ipfs clone* \[options\] \<ipfs_id\> \<directory\> \<api_url\> [api_port]

Clones the given IPFS repository from the network. The *directory* argument is mandatory as the IPFS key is ganderous when used as a directory name as an ordinary Git does.

### Arguments

*ipfs_id*

:   IPFS CID or IPNS key hash to use as remote ID

*directory*

:   Relative directory to clone the repository into

*api_url*

:   IPFS node API URL (the API must be active to view the remote Git database!), default is http://127.0.0.1

*api_port*

:   IPFS node API port (will be attached to URL), the default is 5001

### Options

**-t** TIMEOUT, **-\-timeout** TIMEOUT

:   Network timeout for API communications, sec (float)

*-r* [REMOTE_NAME], *-\-remote-name* [REMOTE_NAME]

:   Gives the remote name to make an IPFS remote, default is origin

**-b** [BRANCH], **-\-branch** [BRANCH]

:   Gives name of the branch to checkout

**-n** [USERNAME], **-\-username** [USERNAME]

:   HTTP authentication username

**-p** [PASSWORD], **-\-password** [PASSWORD]

:   HTTP authentication password

## CHECK

*git ipfs check*

Checks the accessibility of IPFS API and validity of credentials.

## INSTALL

*git ipfs install* \[options\] \<api_url\> [api_port] [ipfs_id]

Installs infrastructure scripts to enable remote IPFS directory as remote repository (`ipfs://` pseudo-protocol).

### Arguments

*api_url*

:   IPFS node API URL (the API endpoint must be active to view the remote Git database!)

*api_port*

:   IPFS node API port (will be attached to URL). The default is 5001

*ipfs_id*

:   IPFS CID or IPNS peer key hash to use as a remote ID. The immutable CID is required to be a baremetal Git repository to be valid.

### Options

**-t** TIMEOUT, **-\-timeout** TIMEOUT

:   Network timeout for API communications, sec (float), the default is 30.0

**-r** [REMOTE_NAME], **-\-remote-name** [REMOTE_NAME]

:   Gives the remote name to make an IPFS remote, the default is `origin`

**-n** [USERNAME], **-\-username** [USERNAME]

:   HTTP authentication username

**-p** [PASSWORD], **-\-password** [PASSWORD]

:   HTTP authentication password

**-\-check-ipfs**

:   Check IPFS API and authentication after installation

## UNINSTALL

*git ipfs uninstall* \[options\]

Uninstalls the IPFS infrastructure scripts from the local repository.

### Options

**-p**, **-\-purge**

:   Purge all additional IPFS infrastructure from the repository's *.git* subdirectory

**-r** [REMOTE_NAME], **-\-remote-name** [REMOTE_NAME]

:   Gives the remote name to restore or remove

## RELEASE

*git ipfs release* \[options\] \<tag\> [ipns_key]

Invokes **git-archive**(1) to create a Git-compatible backup source archive and publish it on the IPFS network.

### Arguments

*tag*

:   Tag or commit ID to release from

*ipns_key*

:   IPNS key hash to publish the release

### Options

**-\-prefix** [PREFIX]

:   Version prefix for being used as a name for the archive

**-p**, **-\-publish**

:   Publish the release via the specified IPNS key [ipns_key] after uploading to IPFS network

**-z**, **-\-zip**

:   Use ZIP archive format instead of .tar.gz

## CONFIG

*git ipfs config* \<mode\> \[options\]

### Modes

*git ipfs config print*

Prints the current configuration as it exists in the repository.

*git ipfs config generate* \[options\]

**-s**, **-\-stdout**

:   Print the generated configuration file to the standard output instead of overwriting the existing one

**-c**, **-\-default**

:   Generate new configuration file overriding all other values set up in this command with their defaults

**-f** [FILENAME], **-\-filename** [FILENAME]

:   Optional filename to store the generated configuration (the default is **.git/ipfs/config**)

**-y**, **-\-overwrite**

:   Overwrite existing configuration

**-\-url** [URL]

:   IPFS node API URL to locate, the default is 'http://127.0.0.1'

**-\-port** [PORT]

:   IPFS node API TCP port (will be attached to URL), the default is 5001

**-\-api-version-prefix** [API_VERSION_PREFIX]

:   IPFS node API version prefix (CAUTION! It is NOT RECOMMENDED to change the default value 'api/v0'!!!)

**-t** [TIMEOUT], **-\-timeout** [TIMEOUT]

:   Network timeout for API communications, sec (float), the default is 30.0

**-\-unpin-old**

:   Instructs the IPFS node whether it is needed to unpin the old immutable repository state from the drive or not

**-r**, **-\-republish**

:   Instructs the IPFS node whether it is needed to republish the freshly pushed commits under the given IPNS name (if it is available)

**-\-ttl** [TTL]

:   Period description string for IPNS republisher, the default is '24h'

**-v**, **-\-cid-version**

:   CID version used to create immutable entries, 0 or 1, the default is 1 (URL-compatible Base32-encoded CID)

**-n** [USERNAME], **-\-username** [USERNAME]

:   HTTP authentication username

**-p** [PASSWORD], **-\-password** [PASSWORD]

:   HTTP authentication password

*git ipfs config manage* \[options\]

Adjusts the existing IPFS remote config.

**NOTE**: for thw most options leaving it without a value on the CLI resets the corresponding parameter to default!

All the options from **generate** mode are available also here, except **-f**, **-c**, and **-y**. The exclusive options of this mode are described below.

**-\-dry-run**

:   Show the regenerated configuration on standard output instead of overwriting the config file

**-\-reset**

:   Resets the entire configuration to defaults, overrides any other option here

### Configuration parameters

The following table contains descriptions of all configuration parameters that could be specified for the repository with IPFS infrastructure installed, via the configuration file **.git/ipfs/config**.

|Parameter|Default value|Description|
|---------|-------------|-----------|
| `URL` | `http://127.0.0.1` | Host URL of IPFS API endpoint |
| `Port` | `5001` | API server's TCP port to connect |
| `VersionPrefix` | `api/v0` | API URI prefix to stay compatible with future changes of the IPFS HTTP API |
| `Timeout` | `30.0` | HTTP timeout for I/O operatons. Increase this parameter if the repository is big or you see the timeout messages during push operations |
| `UnpinOld` | **false** | If this flag is set, the bridge will instruct the IPFS node to unpin the previous state of the repository from the IPFS network. Useful for large repositories shared over IPFS only using tags |
| `Republish` | **true** | Attends to change the addressed immutable CID if an IPNS node is specified as the remote address in the Git repository |
| `IPNSTTLString` | `24h` | String respresenting the duration of IPNS key ownership announcing after republishing |
| `CIDVersion` | `1` | CID version used to generate for the obtained immutable entries. Due the CIDs of version 0 are case-sensitive and incompatible with URI specs, it is recommended to use `0` value only if IPNS node is used in the remote |
| `UserName` | | Username to tell to HTTP API endpoint in case it is remote and _Basic_ or _Digest_ HTTP authentication is used. **This option is commented by default** |
| `UserPassword` | | Username to tell to HTTP API endpoint in case it is remote and _Basic_ or _Digest_ HTTP authentication is used. **This option is commented by default** |
| `IPFSChunker` | `size-65536` | Chunker routine name for being used to generate DHT data blocks for IPFS. Default is a linear chunker routine with 64KB block size |

