# Upload and manage images

A virtual machine image, referred to in this document simply as an
image, is a single file that contains a virtual disk that has a bootable
operating system installed on it. Images are used to create virtual
machine instances within the cloud. The image files themselves are never
modified, but you can copy the image into a persistent instance.

As a user of the VSC cloud, you can upload and manage your own virtual
machine images. For information about creating image files, see the
[Opennebula Docs](https://docs.opennebula.io/7.2/product/virtual_machines_operation/virtual_machines/images/).

You can upload your own image on the [Dashboard](https://cloudpr4.ugent.be/fireedge/sunstone/image/create).
You can also import images from the [Marketplace] (recommended).

:::{warn}
Your custom image must include the opennebula [contextualization packages](https://github.com/OpenNebula/one-apps/wiki/linux_installation).
:::


## Adding images

### Uploading
1) Go to [Dashboard](https://cloudpr4.ugent.be/fireedge/sunstone/image/create).
2) Fill in the name, description, **Turn off** "make persistant".
3) Click "upload" and select the image file on your filesystem (you can also enter a direct download URL).
4) Click "Next".
5) Select the "ceph.steelix" datastore.
6) Click "Next". Skip the advanced options by clicking "Next" again.
7) Click "Finish".

### Setting permissions
After uploading, you will see the images overview.
By default an image can only be used by the user that created them. You can change this by clicking on the image and going to the "info" tab. You likely want to allow your group to "use" the image.