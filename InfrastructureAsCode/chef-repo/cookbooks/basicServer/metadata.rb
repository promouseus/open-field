name 'basicServer'
maintainer 'user'
maintainer_email 'user@example.com'
license 'Apache-2.0'
description 'Installs/Configures basicServer'
long_description 'Installs/Configures basicServer'
version '0.1.0'
chef_version '>= 13.0'

# The `issues_url` points to the location where issues for this cookbook are
# tracked.  A `View Issues` link will be displayed on this cookbook's page when
# uploaded to a Supermarket.
#
issues_url 'https://github.com/<insert_org_here>/basicServer/issues'

# The `source_url` points to the development repository for this cookbook.  A
# `View Source` link will be displayed on this cookbook's page when uploaded to
# a Supermarket.
#
source_url 'https://github.com/<insert_org_here>/basicServer'

# depends 'snmp', '~> 4.0.0'

%w[debian ubuntu redhat centos].each do |os|
  supports os
end

# chef_version '>= 12.10' if respond_to?(:chef_version)
