# Instance access and security

The security and accessibility of your cloud resources is governed by a
few different aspects, which we discuss more detail in the following
sections:

-   Instances must connect to the project's internal network in order to get
    external internet access (see section
    [Networking](#Networking)).

-   Each cloud project can use one floating IP, a public IP address
    which you'll need to link to the resources you want to access.
    Optionally, if the project has requested access to VSC network it
    will receive also three VSC floating IPs (see section
    [floating IP addresses](#floating-ip-addresses)).

-   By default, the UGent firewall blocks most IP addresses and ports.
    Only the port (TCP) range **50000-60000** and ports **80** and **443** 
    are open by default for the public floating IP addresses. Contact <cloud@vscentrum.be> if you need to access other ports from
    the outside world.

-   You can use one or more SSH keys from your VSC account to access
    your instances (see section
    [SSH key pairs](#ssh-key-pairs)).

For other access methods, or SSH authentication for a wider set of
users, you'll need to set up some form of identity management yourself.
This system administration task is beyond the scope of our tutorial.

## Networking
Each project will need **exactly** one public router to access the internet.
This router will be created for you if you use the [OpenTofu module](opentofu.md).
Through this router you can set up port-forwarding rules to your VMs.

A project may also use a VSC router if they have VSC network access.


## SSH key pairs
:::{note}
WIP, needs updating
:::


When an instance is launched, OpenStack can automatically install a
public SSH key on it, so as to give anyone with the corresponding
private key admin access. For this "key pair injection[^1]" to work, the
image that the instance is based on must contain the **cloud-init**
package, or have in place another mechanism in place that will interact
with the OpenStack metadata server to install the appropriate key. For
general instructions on SSH keys, we refer to the section
[Security Keys](/accounts/generating_keys.rst) of this documentation.

If you have generated a key pair with an external tool, you can import
it into OpenStack. The key pair can be used for multiple instances that
belong to a project. For more information, see section
[import a key pair]](#import-a-key-pair).

The public keys from your VSC account are automatically available in
your VSC Cloud projects, so you can immediately inject one of your
existing into your instances. Of course, you can also import new keys
into OpenStack, which are not coupled to your VSC account. If you want
to give other parties SSH access to VM's, you must manage the keys using
some other method. upload SSH keys for other users to your VSC account.

Every OpenStack user account has its own collection of SSH keys for
every project. To share a public key between multiple users of the same
project, each user needs to import it in the OpenStack project.

### Add a key pair

1. Open the Compute tab.

2. Click the Key Pairs tab, which shows the key pairs that are
   available for this project.

3. Click Create Key Pair.

4. In the Create Key Pair dialog box, enter a name for your key pair,
   and click Create Key Pair.

5. Respond to the prompt to download the key pair.

6. Save the **\*.pem** file locally.

7. To change its permissions so that only you can read and write to the
   file, run the following command:

   ```shell
   chmod 0600 yourPrivateKey.pem
   ```

:::{note}
If you are using the OpenStack Dashboard from a Windows computer, use PuTTYgen
to load the `\*.pem` file and convert and save it as `\*.ppk`.
For more information see our documentation on
[Generating keys with PuTTY](/accounts/generating_keys_putty.rst) and also
the [*WinSCP web page for PuTTYgen*](https://winscp.net/eng/docs/ui_puttygen).
:::

* To make the key pair known to SSH, run the `ssh-add` command

  ```shell
  ssh-add yourPrivateKey.pem
  ```

### Import a key pair

1.  Open the Compute tab.

2.  Click the Key Pairs tab, which shows the key pairs that are
    available for this project.

3.  Click Import Key Pair.

4.  In the Import Key Pair dialog box, enter the name of your key pair,
    copy the public key into the Public Key box, and then click Import
    Key Pair.

The Compute database registers the public key of the key pair.

The OpenStack Dashboard lists the key pair on the Key Pairs tab.

[^1]: The OpenStack documentation and interfaces consistently refer to
    "SSH pairs", but of course only the public key of each pair is
    stored in the OpenStack environment, while the private key should be
    kept secure by the owner.

