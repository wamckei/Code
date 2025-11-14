terraform {
  required_providers {
    nutanix = {
      source  = "nutanix/nutanix"
      version = ">= 1.5.0"
    }
  }
}

provider "nutanix" {
  username = var.ntx_user
  password = var.ntx_pwd
  endpoint = var.endpoint
  insecure = true
}

# Retrieve cluster information
data "nutanix_cluster" "cluster" {
  name = var.nutanix_cluster_name
  cluster_id  = data.nutanix_cluster.cluster.id
}

# Retrieve subnet information
data "nutanix_subnet" "subnet" {
  subnet_name = var.nutanix_subnet_name
  subnet_uuid = data.nutanix_subnet.subnet.id
}

resource "nutanix_deploy_template_v2" "vm_from_template" {
  name        = "temp_name"   # optional var.vm_names
  template_id = var.template_uuid  # UUID of the image/template to clone from
  num_vms     = 1

 /*config {
    sysprep {
      unattend_xml = base64encode(templatefile("${path.module}/unattend.xml"
    }
 } */

  /*# Per-VM configuration override block
  guest_customization {
    cloud_init {
      user_data = templatefile("${path.module}/cloud_init.yaml", {
        hostname   = var.vm_names[count.index],
        #ssh_key    = file("${path.module}/id_rsa.pub"),
        #custom_var = ... # Any other customizations per VM
      })
    }
  }*/
}
