resource "aws_ecr_repository" "main" {
  name                 = "jsonbin-clone"
  force_delete         = true
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }

  tags {
    Name = "jsonbin-clone"
    Project = "ecosystem"
  }
}

