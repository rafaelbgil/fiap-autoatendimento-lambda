variable "iam" {
  type        = string
  description = "Variavel utilizada para informar o iam"
}
terraform {

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

data "archive_file" "criarUsuarioCognitoZip" {
  type        = "zip"
  source_file = "src/criarUsuarioCognito/lambda_function.py"
  output_path = "criarUsuarioCognito.py.zip"
}

resource "aws_lambda_function" "criarUsuarioCognito" {
  function_name    = "criarUsuario"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"
  filename         = "criarUsuarioCognito.py.zip"
  source_code_hash = data.archive_file.criarUsuarioCognitoZip.output_base64sha256
  role             = var.iam
}


