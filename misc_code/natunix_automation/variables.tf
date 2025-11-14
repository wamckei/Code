variable "ntx_user" {
  type        = string
  description = "Nutanix PC user name"
  default     = "nutanix"
}
variable "ntx_pwd" {
  type        = string
  description = "Nutanix PC user password"
  default     = "nutanix/4u"
}
variable "endpoint" {
  type        = string
  description = "Prism central as the endpoint"
  default     = "prismcentral.lab.nwa.evtcorp.com"
}


variable "template_uuid" {
  type        = string
  description = "The UUID of your template VM/image"
  default     = ""
}
variable "vm_names" {
  type        = string
  description = "initial host name to be used"
  default     = "tf-vm-vm-0"
}
variable "nutanix_cluster_name" {
  type        = string
  description = "Nutanix deployment cluster"
  default     = "?????"
}
variable "nutanix_subnet_name" {
  type        = string
  description = "target subnet name"
  default     = "????"
}