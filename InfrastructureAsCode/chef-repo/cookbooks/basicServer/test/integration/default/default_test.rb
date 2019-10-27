# Inspec test for recipe basicServer::default

# The Inspec reference, with examples and extensive documentation, can be
# found at http://inspec.io/docs/reference/resources/

describe service 'snmpd' do
  it { should be_installed }
  it { should be_enabled }
  it { should be_running }
end

describe port(161) do
  it { should be_listening }
  its('protocols') { should include 'udp' }
end
