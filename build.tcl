#!/usr/bin/tclsh

set arch "noarch"
set base "naviserver-mod_nsshell-0.2b"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsshell.spec]
exec >@stdout 2>@stderr {*}$buildit

