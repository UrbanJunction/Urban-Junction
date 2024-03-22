terraform {
  required_providers {
    # declare aws required provider as requirement for configuration 
    aws = {
      source = "hashicorp/aws"
    }
  }
}
#configuration for aws provider 
provider "aws" {
  #define service region 
  region = var.region
}