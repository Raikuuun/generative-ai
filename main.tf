provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "app_server" {
    ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu 20.04
    instance_type = "g4dn.xlarge"  # GPU instance
    key_name      = "raiku"
    security_groups = [aws_security_group.app_sg.name]
    user_data = <<-EOF
                #!/bin/bash
                apt update
                apt install -y python3-pip python3-venv
                EOF
    tags = { Name = "GenAI-Server" }
}

resource "aws_security_group" "app_sg" {
    name = "genai-sg"
    ingress {
        from_port   = 5000
        to_port     = 5000
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_s3_bucket" "media" {
    bucket = "genai-media-bucket-${random_id.suffix.hex}"
}

resource "random_id" "suffix" {
    byte_length = 4
}

output "ec2_public_ip" {
    value = aws_instance.app_server.public_ip
}