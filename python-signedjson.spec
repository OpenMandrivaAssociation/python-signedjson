Name:		python-signedjson
Version:	1.1.4
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/signedjson/signedjson-%{version}.tar.gz
Summary:	Sign JSON with Ed25519 signatures
URL:		https://pypi.org/project/signedjson/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Sign JSON with Ed25519 signatures

%prep
%autosetup -p1 -n signedjson-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/signedjson
%{py_sitedir}/signedjson-*.*-info
