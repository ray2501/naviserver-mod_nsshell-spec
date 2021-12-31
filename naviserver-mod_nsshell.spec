#
# spec file for package naviserver nsshell module
#

Summary:        NaviServer nsshell module
Name:           naviserver-mod_nsshell
Version:        0.2b
Release:        1
License:        MPL-2.0
Group:          Productivity/Networking/Web/Servers
Url:            https://bitbucket.org/naviserver/nsshell
BuildRequires:  make
BuildRequires:  naviserver
BuildRequires:  naviserver-devel
Requires:       naviserver
Requires:       naviserver-mod_websocket
Requires:       nsf
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a NaviServer module that implements an interactive shell for NaviServer.
The shell can be used via XMLHttpRequests (XHR) or via the WebSocket interface,
which requires that the websocket module is installed.

%prep
%setup -q %{name}-%{version}

%build

%install
mkdir -p %buildroot/var/lib/naviserver/tcl/nsshell
make DESTDIR=%buildroot install NAVISERVER=/var/lib/naviserver

%clean
rm -rf %buildroot

%files
%defattr(-,nsadmin,nsadmin,-)
/var/lib/naviserver/tcl/nsshell

%changelog

