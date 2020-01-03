# Using puppet to automate a custom HTTP header response

exec {'install-nginx':
  command  =>
  provider =>
  before   =>
}
