Name:           oomcprun
Version:        0.1.0
Release:        1%{?dist}
Summary:        Executes MCP tool calls inside capability-bounded transient systemd scopes.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomcprun
Source0:        oomcprun-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomcprun is a sovereign, capability-bounded MCP TASK RUNNER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomcprun
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomcprun-uninstall

%files
/usr/bin/oomcprun
/usr/bin/oomcprun-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
