variable "agent_name" {
  type    = string
  default = "claims"
}

variable "model_name" {
  type    = string
  default = "anthropic.claude-v2:1"
}

variable "instruction" {
  type    = string
  default = "You are an insurance agent that has access to domain-specific insurance knowledge. You can get insurance claims status."
}

variable "action_groups" {
  type = list(object({
    name = string
    dir_name      = string
    memory_size   = number
    timeout       = number
  }))
  default = [
    {
      name          = "get_claim",
      dir_name      = "get_claim_function",
      memory_size   = 1024,
      timeout       = 900
    }
  ]
}